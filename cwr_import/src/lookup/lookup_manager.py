"""
CWR Lookup Manager - Manages lookup tables for CWR data validation.
"""
import os
import csv
from typing import Dict, List, Any, Optional


class LookupManager:
    """
    Manager for CWR lookup tables.
    
    This class handles loading and accessing lookup tables for validating
    CWR data according to the CISAC specifications.
    """
    
    def __init__(self, tables_dir: Optional[str] = None):
        """
        Initialize the lookup manager.
        
        Args:
            tables_dir: Directory containing the lookup table CSV files.
                        If None, defaults to the 'lookup' directory in the same
                        directory as this module.
        """
        if tables_dir is None:
            # Default to the 'lookup' directory in the same directory as this module
            current_dir = os.path.dirname(os.path.abspath(__file__))
            tables_dir = os.path.join(current_dir, 'tables')
        
        self.tables_dir = tables_dir
        self.tables: Dict[str, List[Dict[str, str]]] = {}
        
        # Ensure the tables directory exists
        os.makedirs(tables_dir, exist_ok=True)
        
    def load_table(self, table_name: str) -> List[Dict[str, str]]:
        """
        Load a lookup table from a CSV file.
        
        Args:
            table_name: Name of the table to load (without the .csv extension)
            
        Returns:
            List of dictionaries containing the table data
            
        Raises:
            FileNotFoundError: If the table file does not exist
        """
        # Check if the table is already loaded
        if table_name in self.tables:
            return self.tables[table_name]
        
        # Construct the file path
        file_path = os.path.join(self.tables_dir, f"{table_name}.csv")
        
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Lookup table not found: {file_path}")
        
        # Load the table from the CSV file
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            table_data = [row for row in reader]
        
        # Store the table in memory
        self.tables[table_name] = table_data
        
        return table_data
    
    def get_table(self, table_name: str) -> List[Dict[str, str]]:
        """
        Get a lookup table.
        
        Args:
            table_name: Name of the table to get
            
        Returns:
            List of dictionaries containing the table data
            
        Raises:
            FileNotFoundError: If the table file does not exist
        """
        return self.load_table(table_name)
    
    def lookup(self, table_name: str, key_field: str, key_value: str, 
               value_field: Optional[str] = None) -> Optional[Any]:
        """
        Look up a value in a table.
        
        Args:
            table_name: Name of the table to search in
            key_field: Name of the field to search by
            key_value: Value to search for
            value_field: Name of the field to return. If None, returns the entire row.
            
        Returns:
            The value of the specified field, the entire row, or None if not found
            
        Raises:
            FileNotFoundError: If the table file does not exist
        """
        table = self.get_table(table_name)
        
        # Look for the row with the matching key
        for row in table:
            if row.get(key_field) == key_value:
                if value_field:
                    return row.get(value_field)
                return row
        
        return None
    
    def is_valid(self, table_name: str, key_field: str, key_value: str) -> bool:
        """
        Check if a value is valid according to a lookup table.
        
        Args:
            table_name: Name of the table to search in
            key_field: Name of the field to search by
            key_value: Value to check
            
        Returns:
            True if the value exists in the table, False otherwise
            
        Raises:
            FileNotFoundError: If the table file does not exist
        """
        result = self.lookup(table_name, key_field, key_value)
        return result is not None
    
    def extract_lookup_table(self, csv_file: str, table_name: str,
                             code_column: str = 'CODE', 
                             definition_column: str = 'DEFINITION') -> None:
        """
        Extract a lookup table from a CSV file and save it as a separate table.
        
        Args:
            csv_file: Path to the CSV file containing the lookup table data
            table_name: Name of the table to extract
            code_column: Name of the column containing the codes
            definition_column: Name of the column containing the definitions
            
        Raises:
            FileNotFoundError: If the CSV file does not exist
        """
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"CSV file not found: {csv_file}")
        
        # Read the CSV file
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            rows = [row for row in reader]
        
        # Extract the rows for the specified table
        table_rows = []
        current_table = None
        
        for row in rows:
            table_field = row.get('TABLE_NAME', '')
            
            # Check if this is a new table
            if table_field and not table_field.isspace():
                current_table = table_field
            
            # If this row belongs to the table we're looking for, add it
            if current_table == table_name and row.get(code_column) and row.get(definition_column):
                table_rows.append({
                    'CODE': row.get(code_column, ''),
                    'DEFINITION': row.get(definition_column, '')
                })
        
        # Create the output CSV file
        output_file = os.path.join(self.tables_dir, f"{table_name}.csv")
        
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['CODE', 'DEFINITION']
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(table_rows)
    
    def extract_all_lookup_tables(self, csv_file: str) -> List[str]:
        """
        Extract all lookup tables from a CSV file.
        
        Args:
            csv_file: Path to the CSV file containing the lookup table data
            
        Returns:
            List of names of the extracted tables
            
        Raises:
            FileNotFoundError: If the CSV file does not exist
        """
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"CSV file not found: {csv_file}")
        
        # Read the CSV file
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            rows = [row for row in reader]
        
        # Find all table names
        table_names = set()
        
        for row in rows:
            table_field = row.get('TABLE_NAME', '')
            
            # Check if this is a valid table name
            if table_field and not table_field.isspace():
                table_names.add(table_field)
        
        # Extract each table
        for table_name in table_names:
            self.extract_lookup_table(csv_file, table_name)
        
        return list(table_names) 