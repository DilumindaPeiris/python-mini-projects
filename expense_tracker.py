"""Local expense tracker using SQLite and integer cents."""
import argparse
import sqlite3
from decimal import Decimal, InvalidOperation
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add")
    add.add_argument("description")
    add.add_argument("amount", help="Positive amount with at most two decimal places")
    add.add_argument("--category", default="Uncategorized", help="Category for the expense")
    list_cmd = commands.add_parser("list")
    list_cmd.add_argument("--category", help="Filter by category")
    commands.add_parser("total")
    delete = commands.add_parser("delete")
    delete.add_argument("id", type=int, help="Expense ID to delete")
    export = commands.add_parser("export")
    export.add_argument("filename", help="CSV filename to export to")
    args = parser.parse_args()
    if args.command == "add":
        try:
            amount = Decimal(args.amount)
            if not amount.is_finite() or amount <= 0 or amount * 100 != (amount * 100).to_integral_value():
                raise ValueError()
            cents = int(amount * 100)
            if cents > 9223372036854775807:
                raise ValueError()
        except (InvalidOperation, ValueError):
            parser.error("Use a positive amount with at most two decimal places.")
        if not args.description.strip():
            parser.error("Description cannot be blank.")
    with sqlite3.connect(Path(__file__).with_name("expenses.db")) as db:
        db.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, description TEXT, cents INTEGER)")
        try:
            db.execute("ALTER TABLE expenses ADD COLUMN category TEXT")
        except sqlite3.OperationalError:
            pass
        if args.command == "add":
            db.execute("INSERT INTO expenses (description, cents, category) VALUES (?, ?, ?)", (args.description, cents, args.category))
            print("Expense saved.")
        elif args.command == "list":
            query = "SELECT id, description, cents, category FROM expenses"
            params = ()
            if args.category:
                query += " WHERE category = ?"
                params = (args.category,)
            query += " ORDER BY id"
            for row in db.execute(query, params):
                category = row[3] if row[3] else "Uncategorized"
                print(f"{row[0]} | {row[1]} | {Decimal(row[2]) / 100:.2f} | {category}")
        elif args.command == "total":
            total = sum(row[0] for row in db.execute("SELECT cents FROM expenses"))
            print(f"Total: {Decimal(total) / 100:.2f}")
        elif args.command == "delete":
            db.execute("DELETE FROM expenses WHERE id = ?", (args.id,))
            print(f"Deleted expense {args.id}.")
        elif args.command == "export":
            import csv
            with open(args.filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Description", "Amount", "Category"])
                for row in db.execute("SELECT id, description, cents, category FROM expenses ORDER BY id"):
                    category = row[3] if row[3] else "Uncategorized"
                    writer.writerow([row[0], row[1], f"{Decimal(row[2]) / 100:.2f}", category])
            print(f"Exported to {args.filename}.")

if __name__ == "__main__":
    main()

