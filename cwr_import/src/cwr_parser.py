"""
CWR Parser - Main module for parsing CWR files.
"""
from typing import Dict, List, Optional, TextIO, Union, Any
import os


class CWRParser:
    """
    Parser for Common Works Registration (CWR) files.
    
    This class handles the parsing of CWR files in versions 2.1 and 2.2 according to
    the CISAC specifications.
    """
    
    def __init__(self, version: Optional[str] = None):
        """
        Initialize the CWR parser.
        
        Args:
            version: CWR version to use (e.g., '2.1', '2.2'). If None, version will be detected from the file.
        """
        self.version = version
        self.errors = []
        self.warnings = []
        self.records = []
        self.transactions = []
        
    def parse_file(self, file_path: str) -> Dict[str, Any]:
        """
        Parse a CWR file from a file path.
        
        Args:
            file_path: Path to the CWR file to parse
            
        Returns:
            Dict containing the parsed CWR data
            
        Raises:
            FileNotFoundError: If the file does not exist
            ValueError: If the file is not a valid CWR file
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'r', encoding='latin-1') as file:
            return self.parse(file)
    
    def parse(self, file: TextIO) -> Dict[str, Any]:
        """
        Parse a CWR file from a file-like object.
        
        Args:
            file: File-like object containing CWR data
            
        Returns:
            Dict containing the parsed CWR data
            
        Raises:
            ValueError: If the file is not a valid CWR file
        """
        self.errors = []
        self.warnings = []
        self.records = []
        self.transactions = []
        
        # Read the file
        lines = file.readlines()
        
        # Validate header
        if not lines or len(lines) < 3:
            raise ValueError("Invalid CWR file: File too short")
        
        # Parse header record
        header = self._parse_header(lines[0])
        
        # Parse group header
        group_header = self._parse_group_header(lines[1])
        
        # Parse records
        for i in range(2, len(lines) - 1):
            record = self._parse_record(lines[i])
            self.records.append(record)
        
        # Parse trailer
        trailer = self._parse_trailer(lines[-1])
        
        # Organize into transactions
        self._organize_transactions()
        
        # Return the parsed data
        return {
            'header': header,
            'group_header': group_header,
            'transactions': self.transactions,
            'trailer': trailer,
            'errors': self.errors,
            'warnings': self.warnings
        }
    
    def _parse_header(self, line: str) -> Dict[str, Any]:
        """Parse the HDR (header) record from a CWR file."""
        if not line.startswith('HDR'):
            raise ValueError("Invalid CWR file: File does not start with HDR record")
        
        # In a real implementation, this would extract all fields according to their positions
        # For now, we'll just return a basic structure
        return {
            'record_type': 'HDR',
            'version': line[3:7].strip(),
            'sender_type': line[7:9].strip(),
            'sender_id': line[9:14].strip(),
            'sender_name': line[14:59].strip(),
            'creation_date': line[59:67].strip(),
            'transmission_date': line[67:75].strip(),
        }
    
    def _parse_group_header(self, line: str) -> Dict[str, Any]:
        """Parse the GRH (group header) record from a CWR file."""
        if not line.startswith('GRH'):
            raise ValueError("Invalid CWR file: Second line does not contain GRH record")
        
        # Basic extraction for now
        return {
            'record_type': 'GRH',
            'transaction_type': line[3:6].strip(),
            'group_id': line[6:11].strip(),
            'version': line[11:15].strip(),
            'batch_request': line[15].strip(),
        }
    
    def _parse_record(self, line: str) -> Dict[str, Any]:
        """Parse a record from a CWR file."""
        if not line or len(line) < 3:
            return {'record_type': 'UNKNOWN', 'raw_data': line}
        
        record_type = line[0:3]
        
        # In a real implementation, we would have specific parsers for each record type
        # For now, just return the record type and raw data
        return {
            'record_type': record_type,
            'raw_data': line
        }
    
    def _parse_trailer(self, line: str) -> Dict[str, Any]:
        """Parse the TRL (trailer) record from a CWR file."""
        if not line.startswith('TRL'):
            raise ValueError("Invalid CWR file: Last line does not contain TRL record")
        
        # Basic extraction for now
        return {
            'record_type': 'TRL',
            'group_count': int(line[3:8].strip() or '0'),
            'transaction_count': int(line[8:13].strip() or '0'),
            'record_count': int(line[13:21].strip() or '0'),
        }
    
    def _organize_transactions(self):
        """Organize parsed records into transactions."""
        current_transaction = None
        
        for record in self.records:
            record_type = record['record_type']
            
            # Transaction headers
            if record_type in ('WRK', 'REV', 'ACK', 'ISW', 'ISR', 'EXC', 'NWR'):
                if current_transaction:
                    self.transactions.append(current_transaction)
                current_transaction = {
                    'transaction_type': record_type,
                    'records': [record]
                }
            elif current_transaction:
                current_transaction['records'].append(record)
            else:
                # Record outside of a transaction
                self.errors.append(f"Record found outside of a transaction: {record_type}")
        
        # Add the last transaction if there is one
        if current_transaction:
            self.transactions.append(current_transaction) 