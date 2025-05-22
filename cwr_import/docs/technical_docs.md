# CWR Import Module: Technical Documentation

## Overview

The CWR Import Module is a Python library for parsing and validating Common Works Registration (CWR) files in versions 2.1 and 2.2. This document provides technical information for developers working with the module.

## Module Structure

- `src/` - Source code
  - `__init__.py` - Package initialization
  - `cwr_parser.py` - Main parser implementation
  - `main.py` - High-level interface and CLI entry point
  - `models/` - Data models
    - `records.py` - Record type definitions
  - `validator/` - Validation components
    - `validator.py` - CWR validator implementation
  - `lookup/` - Lookup table management
    - `lookup_manager.py` - Lookup table manager
    - `tables/` - Directory for lookup table CSV files

- `tests/` - Test cases
  - `test_import.py` - Main test script
  - `samples/` - Sample CWR files for testing

- `docs/` - Documentation
  - `technical_docs.md` - This file
  - `field_specs.md` - Field specifications

## Key Classes

### CWRImport (src/main.py)

The main class providing a high-level interface for parsing and validating CWR files.

```python
import json
from cwr_import.src.main import CWRImport

# Initialize the CWR import module
cwr_import = CWRImport(version='2.2')

# Parse a CWR file
result = cwr_import.parse_file('path/to/cwr_file.txt')

# Check validation results
if result['is_valid']:
    print("File is valid")
else:
    print("File is invalid")
    for error in result['validation_errors']:
        print(f"Error: {error}")

# Convert result to JSON
json_data = cwr_import.to_json(result)
```

### CWRParser (src/cwr_parser.py)

The core parser class responsible for parsing CWR files.

```python
from cwr_import.src.cwr_parser import CWRParser

# Initialize the parser
parser = CWRParser(version='2.2')

# Parse a CWR file
with open('path/to/cwr_file.txt', 'r') as f:
    result = parser.parse(f)

# Access parsed data
header = result['header']
transactions = result['transactions']
```

### CWRValidator (src/validator/validator.py)

The validator class responsible for validating CWR files.

```python
from cwr_import.src.validator.validator import CWRValidator

# Initialize the validator
validator = CWRValidator(version='2.2')

# Validate parsed CWR data
is_valid = validator.validate(cwr_data)

# Access validation errors and warnings
errors = validator.errors
warnings = validator.warnings
```

### LookupManager (src/lookup/lookup_manager.py)

The lookup manager class responsible for managing lookup tables.

```python
from cwr_import.src.lookup.lookup_manager import LookupManager

# Initialize the lookup manager
lookup_manager = LookupManager()

# Load a lookup table
table = lookup_manager.get_table('agreement_type')

# Look up a value
value = lookup_manager.lookup('agreement_type', 'CODE', 'OS', 'DEFINITION')

# Check if a value is valid
is_valid = lookup_manager.is_valid('agreement_type', 'CODE', 'OS')

# Extract lookup tables from a CSV file
lookup_manager.extract_all_lookup_tables('path/to/lookup_table.csv')
```

## Record Models

The module defines data models for various CWR record types in `src/models/records.py`.

### BaseRecord

Base class for all CWR record types.

### HeaderRecord (HDR)

Represents the HDR (Header) record in a CWR file.

### GroupHeaderRecord (GRH)

Represents the GRH (Group Header) record in a CWR file.

### TrailerRecord (TRL)

Represents the TRL (Trailer) record in a CWR file.

### WorkRegistrationRecord (WRK)

Represents the WRK (Work Registration) transaction header record.

### SubmitterWriterRecord (SWR)

Represents the SWR (Submitter Writer) record.

### WriterTerritoryRecord (SWT)

Represents the SWT (Writer Territory) record.

### SubmitterPublisherRecord (SPU)

Represents the SPU (Submitter Publisher) record.

### PublisherTerritoryRecord (SPT)

Represents the SPT (Publisher Territory) record.

### CWRTransaction

Represents a complete CWR transaction (a group of related records).

### CWRFile

Represents a complete CWR file.

## Command Line Interface

The module provides a command-line interface for parsing and validating CWR files.

```bash
# Parse and validate a CWR file
cwr_import path/to/cwr_file.txt --output output.json

# Parse and validate a CWR file with a specific version
cwr_import path/to/cwr_file.txt --version 2.2 --output output.json

# Parse a CWR file without validation
cwr_import path/to/cwr_file.txt --no-validate --output output.json
```

## Error Handling

The module handles various types of errors:

- **FileNotFoundError**: Raised when a file does not exist
- **ValueError**: Raised when a file is not a valid CWR file
- **ValidationError**: Represents a validation error in a CWR file

## Extending the Module

### Adding Support for New Record Types

To add support for a new record type:

1. Define a new record class in `src/models/records.py`
2. Add parsing logic to `CWRParser._parse_record()` in `src/cwr_parser.py`
3. Add validation logic to `CWRValidator` in `src/validator/validator.py`

### Adding Support for New CWR Versions

To add support for a new CWR version:

1. Update version checking in `CWRParser` and `CWRValidator`
2. Add version-specific parsing logic to `CWRParser`
3. Add version-specific validation logic to `CWRValidator`
4. Update command-line interface in `main.py`

## Performance Considerations

- The module is designed to handle CWR files of typical size (< 1MB) efficiently
- For larger files, consider using the `parse()` method with a file-like object to avoid loading the entire file into memory

## Thread Safety

The module is not thread-safe by default. Each thread should create its own instance of `CWRImport`, `CWRParser`, `CWRValidator`, and `LookupManager`.

## Dependencies

The module has no external dependencies beyond the Python standard library. 