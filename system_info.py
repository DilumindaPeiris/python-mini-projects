"""Display basic system information."""
import platform
import os
import sys

def main():
    print("--- System Information ---")
    print(f"System:    {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release:   {platform.release()}")
    print(f"Version:   {platform.version()}")
    print(f"Machine:   {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python:    {sys.version.split()[0]}")
    
    if hasattr(os, 'cpu_count'):
        print(f"CPU Cores: {os.cpu_count()}")

if __name__ == "__main__":
    main()
