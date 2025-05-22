"""
CWR Import Module - Main entry point for the CWR parser.
"""
import os
import sys
import json
import argparse
from typing import Dict, List, Any, Optional, TextIO

from .cwr_parser import CWRParser
from .validator.validator import CWRValidator
from .models.records import CWRFile


class CWRImport:
    """
    Main class for the CWR import module.
    
    This class provides a high-level interface for parsing and validating
    CWR files in versions 2.1 and 2.2.
    """
    
    def __init__(self, version: Optional[str] = None):
        """
        Initialize the CWR import module.
        
        Args:
            version: CWR version to use ('2.1' or '2.2'). If None, version will be detected from the file.
        """
        self.version = version
        self.parser = CWRParser(version)
        self.validator = CWRValidator(version or '2.2')
        
    def parse_file(self, file_path: str, validate: bool = True) -> Dict[str, Any]:
        """
        Parse a CWR file from a file path.
        
        Args:
            file_path: Path to the CWR file to parse
            validate: Whether to validate the file after parsing
            
        Returns:
            Dict containing the parsed CWR data
            
        Raises:
            FileNotFoundError: If the file does not exist
            ValueError: If the file is not a valid CWR file
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Parse the file
        result = self.parser.parse_file(file_path)
        
        # Validate if requested
        if validate:
            is_valid = self.validator.validate(result)
            result['is_valid'] = is_valid
            result['validation_errors'] = self.validator.errors
            result['validation_warnings'] = self.validator.warnings
        
        return result
    
    def parse(self, file: TextIO, validate: bool = True) -> Dict[str, Any]:
        """
        Parse a CWR file from a file-like object.
        
        Args:
            file: File-like object containing CWR data
            validate: Whether to validate the file after parsing
            
        Returns:
            Dict containing the parsed CWR data
            
        Raises:
            ValueError: If the file is not a valid CWR file
        """
        # Parse the file
        result = self.parser.parse(file)
        
        # Validate if requested
        if validate:
            is_valid = self.validator.validate(result)
            result['is_valid'] = is_valid
            result['validation_errors'] = self.validator.errors
            result['validation_warnings'] = self.validator.warnings
        
        return result
    
    @staticmethod
    def to_json(cwr_data: Dict[str, Any], output_file: Optional[str] = None) -> Optional[str]:
        """
        Convert CWR data to JSON.
        
        Args:
            cwr_data: Parsed CWR data
            output_file: Optional file path to write the JSON to
            
        Returns:
            JSON string if output_file is None, otherwise None
        """
        json_data = json.dumps(cwr_data, indent=2)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(json_data)
            return None
        
        return json_data


def main():
    """Command-line entry point for the CWR import module."""
    parser = argparse.ArgumentParser(description='Parse and validate CWR files')
    parser.add_argument('file', help='Path to the CWR file to parse')
    parser.add_argument('--version', choices=['2.1', '2.2'], help='CWR version (default: auto-detect)')
    parser.add_argument('--no-validate', action='store_true', help='Skip validation')
    parser.add_argument('--output', help='Output file path (default: stdout)')
    
    args = parser.parse_args()
    
    try:
        # Initialize the CWR import module
        cwr_import = CWRImport(version=args.version)
        
        # Parse the file
        result = cwr_import.parse_file(args.file, validate=not args.no_validate)
        
        # Output the result
        if args.output:
            cwr_import.to_json(result, args.output)
            print(f"Output written to {args.output}")
        else:
            json_data = cwr_import.to_json(result)
            print(json_data)
        
        # Exit with error code if validation failed
        if not args.no_validate and not result.get('is_valid', False):
            sys.exit(1)
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main() 