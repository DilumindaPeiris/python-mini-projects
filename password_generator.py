"""Generate secure random passwords."""
import argparse
import secrets
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character set must be selected.")

    return "".join(secrets.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--length", type=int, default=12, help="Length of the password")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude numbers")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    
    args = parser.parse_args()
    
    try:
        pwd = generate_password(
            args.length,
            not args.no_upper,
            not args.no_lower,
            not args.no_digits,
            not args.no_symbols
        )
        print(pwd)
    except ValueError as e:
        parser.error(str(e))

if __name__ == "__main__":
    main()
