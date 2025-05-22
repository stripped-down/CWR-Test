#!/usr/bin/env python
"""
Script to extract lookup tables from CWR CSV files.

This script extracts lookup tables from CWR CSV files and saves them
as separate CSV files in the lookup tables directory.
"""
import os
import sys
import argparse

from src.lookup.lookup_manager import LookupManager


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Extract lookup tables from CWR CSV files')
    parser.add_argument('csv_file', help='Path to the CWR lookup CSV file')
    parser.add_argument('--output-dir', help='Directory to save the extracted tables to')
    parser.add_argument('--table', help='Specific table to extract (default: all tables)')
    
    args = parser.parse_args()
    
    try:
        # Initialize the lookup manager
        lookup_manager = LookupManager(tables_dir=args.output_dir)
        
        # Extract the tables
        if args.table:
            lookup_manager.extract_lookup_table(args.csv_file, args.table)
            print(f"Extracted table: {args.table}")
        else:
            tables = lookup_manager.extract_all_lookup_tables(args.csv_file)
            print(f"Extracted {len(tables)} tables:")
            for table in tables:
                print(f"  - {table}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main() 