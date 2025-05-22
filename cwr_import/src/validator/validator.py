"""
CWR Validator - Validates CWR files according to specifications.
"""
from typing import Dict, List, Any, Optional
import re


class CWRValidator:
    """
    Validator for Common Works Registration (CWR) files.
    
    This class validates CWR files according to the specifications for
    versions 2.1 and 2.2.
    """
    
    def __init__(self, version: str = '2.2'):
        """
        Initialize the CWR validator.
        
        Args:
            version: CWR version to validate against ('2.1' or '2.2')
        """
        self.version = version
        self.errors = []
        self.warnings = []
        
    def validate(self, cwr_data: Dict[str, Any]) -> bool:
        """
        Validate a parsed CWR file.
        
        Args:
            cwr_data: Dictionary containing parsed CWR data
            
        Returns:
            True if the CWR file is valid, False otherwise
        """
        self.errors = []
        self.warnings = []
        
        # Validate file structure
        valid_structure = self._validate_structure(cwr_data)
        
        # Validate header
        valid_header = self._validate_header(cwr_data.get('header', {}))
        
        # Validate group header
        valid_group_header = self._validate_group_header(cwr_data.get('group_header', {}))
        
        # Validate transactions
        valid_transactions = self._validate_transactions(cwr_data.get('transactions', []))
        
        # Validate trailer
        valid_trailer = self._validate_trailer(cwr_data.get('trailer', {}), cwr_data)
        
        # Return overall validity
        return valid_structure and valid_header and valid_group_header and valid_transactions and valid_trailer
    
    def _validate_structure(self, cwr_data: Dict[str, Any]) -> bool:
        """Validate the overall structure of a CWR file."""
        valid = True
        
        # Check required components
        if 'header' not in cwr_data:
            self.errors.append("Missing HDR record")
            valid = False
            
        if 'group_header' not in cwr_data:
            self.errors.append("Missing GRH record")
            valid = False
            
        if 'trailer' not in cwr_data:
            self.errors.append("Missing TRL record")
            valid = False
            
        if 'transactions' not in cwr_data or not cwr_data['transactions']:
            self.errors.append("No transactions found in CWR file")
            valid = False
            
        return valid
    
    def _validate_header(self, header: Dict[str, Any]) -> bool:
        """Validate the HDR (header) record."""
        valid = True
        
        # Check record type
        if header.get('record_type') != 'HDR':
            self.errors.append("Invalid or missing HDR record")
            return False
        
        # Check version
        version = header.get('version', '')
        if self.version == '2.1' and version != '01.10':
            self.errors.append(f"Invalid version for CWR 2.1: {version}")
            valid = False
        elif self.version == '2.2' and version != '02.20':
            self.errors.append(f"Invalid version for CWR 2.2: {version}")
            valid = False
        
        # Check sender type
        sender_type = header.get('sender_type', '')
        if sender_type not in ('PB', 'SO', 'WR', 'AA'):
            self.errors.append(f"Invalid sender type: {sender_type}")
            valid = False
        
        # Check dates
        creation_date = header.get('creation_date', '')
        if not self._validate_date(creation_date):
            self.errors.append(f"Invalid creation date: {creation_date}")
            valid = False
            
        transmission_date = header.get('transmission_date', '')
        if not self._validate_date(transmission_date):
            self.errors.append(f"Invalid transmission date: {transmission_date}")
            valid = False
        
        return valid
    
    def _validate_group_header(self, group_header: Dict[str, Any]) -> bool:
        """Validate the GRH (group header) record."""
        valid = True
        
        # Check record type
        if group_header.get('record_type') != 'GRH':
            self.errors.append("Invalid or missing GRH record")
            return False
        
        # Check transaction type
        transaction_type = group_header.get('transaction_type', '')
        if transaction_type not in ('NWR', 'REV', 'ACK', 'ISW', 'ISR', 'EXC'):
            self.errors.append(f"Invalid transaction type in GRH: {transaction_type}")
            valid = False
        
        # Check version
        version = group_header.get('version', '')
        if self.version == '2.1' and version != '01.10':
            self.errors.append(f"Invalid version in GRH for CWR 2.1: {version}")
            valid = False
        elif self.version == '2.2' and version != '02.20':
            self.errors.append(f"Invalid version in GRH for CWR 2.2: {version}")
            valid = False
        
        return valid
    
    def _validate_transactions(self, transactions: List[Dict[str, Any]]) -> bool:
        """Validate all transactions in the CWR file."""
        valid = True
        
        for i, transaction in enumerate(transactions):
            if not self._validate_transaction(transaction):
                self.errors.append(f"Invalid transaction at index {i}")
                valid = False
        
        return valid
    
    def _validate_transaction(self, transaction: Dict[str, Any]) -> bool:
        """Validate a single transaction in the CWR file."""
        valid = True
        
        transaction_type = transaction.get('transaction_type', '')
        records = transaction.get('records', [])
        
        # Check transaction type
        if transaction_type not in ('WRK', 'REV', 'ACK', 'ISW', 'ISR', 'EXC', 'NWR'):
            self.errors.append(f"Invalid transaction type: {transaction_type}")
            valid = False
        
        # Check record types and sequence
        if not records:
            self.errors.append("Transaction contains no records")
            valid = False
        elif records[0].get('record_type') != transaction_type:
            self.errors.append(f"Transaction header record type does not match transaction type")
            valid = False
        
        # Validate specific transaction types
        if transaction_type == 'NWR':
            valid = valid and self._validate_nwr_transaction(records)
        elif transaction_type == 'REV':
            valid = valid and self._validate_rev_transaction(records)
        
        return valid
    
    def _validate_nwr_transaction(self, records: List[Dict[str, Any]]) -> bool:
        """Validate a NWR (New Work Registration) transaction."""
        valid = True
        
        # Check for required record types
        record_types = [record.get('record_type') for record in records]
        
        # NWR must have at least one SWT record
        if 'SWT' not in record_types:
            self.errors.append("NWR transaction missing SWT record")
            valid = False
        
        # NWR must have at least one SWR record
        if 'SWR' not in record_types:
            self.errors.append("NWR transaction missing SWR record")
            valid = False
        
        return valid
    
    def _validate_rev_transaction(self, records: List[Dict[str, Any]]) -> bool:
        """Validate a REV (Revised Registration) transaction."""
        valid = True
        
        # Check for required record types
        record_types = [record.get('record_type') for record in records]
        
        # REV must have at least one SWT record
        if 'SWT' not in record_types:
            self.errors.append("REV transaction missing SWT record")
            valid = False
        
        # REV must have at least one SWR record
        if 'SWR' not in record_types:
            self.errors.append("REV transaction missing SWR record")
            valid = False
        
        return valid
    
    def _validate_trailer(self, trailer: Dict[str, Any], cwr_data: Dict[str, Any]) -> bool:
        """Validate the TRL (trailer) record."""
        valid = True
        
        # Check record type
        if trailer.get('record_type') != 'TRL':
            self.errors.append("Invalid or missing TRL record")
            return False
        
        # Check counts
        transaction_count = trailer.get('transaction_count', 0)
        actual_transaction_count = len(cwr_data.get('transactions', []))
        if transaction_count != actual_transaction_count:
            self.errors.append(f"Transaction count mismatch: {transaction_count} in TRL, {actual_transaction_count} actual")
            valid = False
        
        return valid
    
    def _validate_date(self, date_str: str) -> bool:
        """Validate a date string in YYYYMMDD format."""
        if not date_str or len(date_str) != 8:
            return False
        
        try:
            year = int(date_str[0:4])
            month = int(date_str[4:6])
            day = int(date_str[6:8])
            
            # Basic validation
            if year < 1900 or year > 2100:
                return False
            if month < 1 or month > 12:
                return False
            if day < 1 or day > 31:
                return False
                
            return True
        except ValueError:
            return False 