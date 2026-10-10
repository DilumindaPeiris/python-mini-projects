"""Encode or decode text using Base64."""
import argparse
import base64
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encode", action="store_true", help="Encode text")
    group.add_argument("-d", "--decode", action="store_true", help="Decode text")
    parser.add_argument("text", help="Text to process")
    
    args = parser.parse_args()
    
    try:
        if args.encode:
            result = base64.b64encode(args.text.encode('utf-8')).decode('utf-8')
            print(result)
        elif args.decode:
            result = base64.b64decode(args.text.encode('utf-8')).decode('utf-8')
            print(result)
    except Exception as e:
        print(f"Error processing text: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
