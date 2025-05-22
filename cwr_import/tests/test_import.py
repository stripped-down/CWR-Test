"""
Test script for the CWR import module.
"""
import os
import unittest
from src.main import CWRImport


class TestCWRImport(unittest.TestCase):
    """Test case for the CWR import module."""
    
    def setUp(self):
        """Set up the test case."""
        self.sample_file = os.path.join(os.path.dirname(__file__), 'samples', 'sample_cwr_2.2.txt')
        self.cwr_import = CWRImport()
    
    def test_parse_file(self):
        """Test parsing a CWR file."""
        result = self.cwr_import.parse_file(self.sample_file, validate=False)
        
        # Check that the file was parsed
        self.assertIn('header', result)
        self.assertIn('group_header', result)
        self.assertIn('transactions', result)
        self.assertIn('trailer', result)
        
        # Check header information
        self.assertEqual(result['header']['record_type'], 'HDR')
        self.assertEqual(result['header']['sender_type'], 'PB')
        self.assertEqual(result['header']['sender_id'], '000000123')
        
        # Check group header information
        self.assertEqual(result['group_header']['record_type'], 'GRH')
        self.assertEqual(result['group_header']['transaction_type'], 'WRK')
        
        # Check transactions
        self.assertGreater(len(result['transactions']), 0)
        
        # Check trailer information
        self.assertEqual(result['trailer']['record_type'], 'TRL')
        self.assertEqual(result['trailer']['group_count'], 1)
        self.assertEqual(result['trailer']['transaction_count'], 1)
    
    def test_validation(self):
        """Test validating a CWR file."""
        result = self.cwr_import.parse_file(self.sample_file, validate=True)
        
        # Check validation results
        self.assertIn('is_valid', result)
        self.assertIn('validation_errors', result)
        self.assertIn('validation_warnings', result)


if __name__ == '__main__':
    unittest.main() 