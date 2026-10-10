# Python Mini Projects
A collection of small command-line applications using Python's standard library only.

## Projects Included

1. **Expense Tracker** (`expense_tracker.py`)
   - Manages expenses using a local SQLite database (stores amounts in integer cents).
   - Supports adding categories, filtering, deletion, and exporting to CSV.
2. **Monte Carlo Pi Estimator** (`monte_carlo_pi.py`)
   - Estimates the value of Pi using random sampling.
   - Supports multiple trials to calculate mean and standard deviation.
3. **Password Generator** (`password_generator.py`)
   - Generates cryptographically secure random passwords.
   - Options to toggle uppercase, lowercase, numbers, and symbols.
4. **To-Do List CLI** (`todo_cli.py`)
   - Simple task manager utilizing JSON for storage.
   - Add, list, complete, and delete tasks quickly from the terminal.
5. **Text Analyzer** (`text_analyzer.py`)
   - Analyzes a text file to count lines, words, and characters.
   - Displays the top most common words.
6. **System Information** (`system_info.py`)
   - Displays basic OS and hardware information using the `platform` module.
7. **Base64 Encoder/Decoder** (`base64_encoder.py`)
   - Quickly encode or decode text strings to and from Base64.

## Run
Requires Python 3.10+.

```sh
# Expense Tracker
python expense_tracker.py add "Lunch" 450.50 --category Food
python expense_tracker.py list --category Food
python expense_tracker.py export my_expenses.csv

# Monte Carlo Pi
python monte_carlo_pi.py --samples 100000 --trials 5

# Password Generator
python password_generator.py --length 16
python password_generator.py --no-symbols

# To-Do List CLI
python todo_cli.py add "Finish GitHub setup"
python todo_cli.py list
python todo_cli.py done 1

# Text Analyzer
python text_analyzer.py README.md --top 3

# System Information
python system_info.py

# Base64 Encoder
python base64_encoder.py -e "Hello World"
python base64_encoder.py -d "SGVsbG8gV29ybGQ="
```

Note: Local databases (`*.db`), generated exports (`*.csv`), and JSON data files (`*.json`) should be excluded from version control.
