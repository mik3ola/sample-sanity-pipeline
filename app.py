#!/usr/bin/env python3
"""
A simple CLI tool that demonstrates basic functionality for sanity testing.
"""

import argparse
import sys

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Sample CLI tool for sanity testing")
    parser.add_argument("--greet", action="store_true", help="Display a greeting message")
    return parser.parse_args()

def greet():
    """Return a greeting message."""
    return "Hello, World!"

def main():
    """Main entry point for the CLI tool."""
    args = parse_arguments()
    
    if args.greet:
        print(greet())
        return 0
    else:
        print("No arguments provided. Use --greet to display a greeting message.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
