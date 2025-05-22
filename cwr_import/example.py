#!/usr/bin/env python
"""
Example script demonstrating the usage of the CWR import module.
"""
import os
import sys
import json
from src.main import CWRImport


def main():
    """Main entry point for the script."""
    # Check if a file path was provided
    if len(sys.argv) < 2:
        print("Usage: example.py <cwr_file>")
        sys.exit(1)
    
    # Get the file path
    file_path = sys.argv[1]
    
    try:
        # Initialize the CWR import module
        cwr_import = CWRImport()
        
        # Parse the file
        print(f"Parsing file: {file_path}")
        result = cwr_import.parse_file(file_path)
        
        # Display validation results
        print(f"Validation: {'Success' if result.get('is_valid', False) else 'Failed'}")
        
        if not result.get('is_valid', False):
            print("\nValidation Errors:")
            for error in result.get('validation_errors', []):
                print(f"  - {error}")
            
            print("\nValidation Warnings:")
            for warning in result.get('validation_warnings', []):
                print(f"  - {warning}")
        
        # Display parsed data
        print("\nParsed Data:")
        
        # Header
        header = result.get('header', {})
        print(f"  Header:")
        print(f"    Sender Type: {header.get('sender_type', '')}")
        print(f"    Sender ID: {header.get('sender_id', '')}")
        print(f"    Sender Name: {header.get('sender_name', '')}")
        print(f"    Creation Date: {header.get('creation_date', '')}")
        
        # Transactions
        transactions = result.get('transactions', [])
        print(f"\n  Transactions: {len(transactions)}")
        
        for i, transaction in enumerate(transactions):
            print(f"\n    Transaction {i+1}:")
            print(f"      Type: {transaction.get('transaction_type', '')}")
            print(f"      Records: {len(transaction.get('records', []))}")
            
            # Print first few records
            records = transaction.get('records', [])
            for j, record in enumerate(records[:5]):
                print(f"        Record {j+1}: {record.get('record_type', '')}")
            
            if len(records) > 5:
                print(f"        ... and {len(records) - 5} more records")
        
        # Save the result to a JSON file
        output_file = os.path.splitext(file_path)[0] + ".json"
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        
        print(f"\nFull result saved to: {output_file}")
    
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main() 