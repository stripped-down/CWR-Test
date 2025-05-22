# CWR Import Module: Product Requirements Document

## 1. Introduction

### 1.1 Purpose
This document outlines the requirements for developing a Common Works Registration (CWR) import module focused on versions 2.1 and 2.2. The module will parse, validate, and process CWR files according to the CISAC standards.

### 1.2 Scope
The CWR import module will support the parsing and validation of CWR files in versions 2.1 and 2.2 formats. It will extract all relevant information about musical works, rights holders, and territorial rights.

### 1.3 Definitions and Acronyms
- **CWR**: Common Works Registration
- **CISAC**: Confédération Internationale des Sociétés d'Auteurs et Compositeurs
- **PRO**: Performing Rights Organization
- **ISWC**: International Standard Musical Work Code
- **IPI**: Interested Party Information

## 2. Product Overview

### 2.1 Product Perspective
The CWR import module will be a standalone component that can be integrated into larger music rights management systems. It will serve as the entry point for processing works registration data in the industry-standard CWR format.

### 2.2 Product Features
- Parse CWR files in 2.1 and 2.2 formats
- Validate file structure against CWR specifications
- Validate record content and field values
- Extract work metadata (titles, identifiers, creation information)
- Extract rights holder information (writers, publishers)
- Extract territory-specific rights distributions
- Convert CWR data to structured internal format
- Generate detailed error reports for invalid data

### 2.3 User Classes and Characteristics
- **Music Publishers**: Organizations registering works with PROs
- **PROs**: Organizations receiving work registrations
- **Application Developers**: Integrating the import module into larger systems

## 3. Functional Requirements

### 3.1 File Parsing

#### 3.1.1 Header Parsing
- The system shall parse CWR file headers (HDR records)
- The system shall validate CWR version information
- The system shall extract sender and recipient information

#### 3.1.2 Group Header Parsing
- The system shall parse group headers (GRH records)
- The system shall validate transaction counts

#### 3.1.3 Transaction Parsing
- The system shall parse transaction headers (e.g., WRK, REV)
- The system shall validate record sequences within transactions

#### 3.1.4 Record Parsing
- The system shall parse all record types defined in CWR 2.1/2.2 specifications
- The system shall extract field values according to the defined field positions and lengths

### 3.2 Data Validation

#### 3.2.1 Structural Validation
- The system shall validate the overall file structure
- The system shall validate record sequences
- The system shall validate record counts

#### 3.2.2 Field Validation
- The system shall validate field formats (e.g., dates, numeric values)
- The system shall validate field values against lookup tables
- The system shall validate mandatory fields

#### 3.2.3 Transaction Validation
- The system shall validate relationships between records
- The system shall validate integrity constraints (e.g., share totals = 100%)

### 3.3 Data Extraction

#### 3.3.1 Work Information
- The system shall extract work titles (original and alternative)
- The system shall extract work identifiers (ISWC, submitter work IDs)
- The system shall extract work attributes (e.g., duration, language, creation date)

#### 3.3.2 Rights Holder Information
- The system shall extract writer information (names, IPI numbers, roles)
- The system shall extract publisher information (names, IPI numbers, roles)
- The system shall extract rights holder relationships

#### 3.3.3 Territory Information
- The system shall extract territory-specific rights distributions
- The system shall extract collection shares by territory

#### 3.3.4 Additional Metadata
- The system shall extract audio-visual production information (if present)
- The system shall extract recording information (if present)
- The system shall extract performing artist information (if present)

### 3.4 Error Reporting

#### 3.4.1 Error Identification
- The system shall identify and categorize errors based on CWR error specifications
- The system shall assign appropriate error codes and levels

#### 3.4.2 Error Reporting
- The system shall generate detailed error reports
- The system shall provide line and position information for errors
- The system shall provide suggestions for error resolution where possible

## 4. Technical Requirements

### 4.1 Performance Requirements
- The system shall process standard CWR files (typically <1MB) in under 5 seconds
- The system shall support processing of larger CWR files (up to 10MB)

### 4.2 Security Requirements
- The system shall not store sensitive data unless explicitly configured to do so
- The system shall log access to CWR files

### 4.3 Software Quality Attributes
- **Reliability**: The system shall correctly parse 99.9% of valid CWR files
- **Robustness**: The system shall gracefully handle malformed CWR files
- **Extensibility**: The system shall be designed to allow future support for additional CWR versions

## 5. Record Types to Support

The module shall support all record types defined in CWR 2.1 and 2.2, including but not limited to:

### 5.1 Header Records
- HDR (File Header)
- GRH (Group Header)
- GRT (Group Trailer)
- TRL (File Trailer)

### 5.2 Transaction Headers
- WRK (Work Registration)
- REV (Work Revision)
- ISW (ISWC Request)
- ISR (ISWC Response)

### 5.3 Work Information
- NWR (New Work Registration)
- REV (Revised Registration)
- ALT (Alternative Title)
- EWT (Entire Work Title)
- VER (Original Work Title for Versions)
- PER (Performing Artist)
- REC (Recording Detail)
- ORN (Work Origin)

### 5.4 Rights Holder Information
- SWR (Submitter Writer)
- OWR (Other Writer)
- SPU (Submitter Publisher)
- OPU (Other Publisher)
- SWT (Writer Territory of Control)
- OWT (Publisher Territory of Control)
- SPT (Publisher Territory of Control)
- OPT (Other Publisher Territory of Control)
- PWR (Publisher Writer)

### 5.5 Component Information
- COM (Component)
- IND (Instrumentation Detail)
- INS (Instrumentation Summary)

## 6. Lookup Tables

The system shall include and utilize the following lookup tables for validation:

- Agreement Type
- BIEM/CISAC Media Type
- BLTVR (Background, Logo, Theme, Visual, Rolled up Cue)
- CIS Language Code
- Composite Type
- CWR Work Type
- Dialect
- Excerpt Type
- Instrument
- Intended Purpose
- Lyric Adaptation
- Music Arrangement
- Musical Work Distribution Category
- Publisher Type
- Recording Technique
- Sender ID Code
- Society Code
- Special Agreement Types
- Territory Codes
- Text Music Relationship
- Title Type
- Version Type
- Writer Role

## 7. Implementation Considerations

### 7.1 File Format Details
CWR files are fixed-width text files with specific record types and field definitions. Each record has a specific format defined by the CWR standard.

### 7.2 Error Handling
The system should implement the error codes and levels as defined in the CWR specifications, including:
- Fatal (F): Errors that prevent processing
- Record (R): Errors within specific records
- Transaction (T): Errors affecting an entire transaction
- Group (G): Errors affecting an entire group

### 7.3 Extensibility
The system should be designed to allow for future support of additional CWR versions (e.g., 3.0, 3.1) with minimal modifications to the core architecture.

## 8. Constraints

### 8.1 Standards Compliance
The implementation must strictly adhere to the CWR 2.1 and 2.2 specifications published by CISAC.

### 8.2 Licensing
All lookup table data included must comply with CISAC licensing requirements.

## 9. Documentation Requirements

The following documentation shall be provided:
- API Documentation
- Field Specifications
- Error Code Reference
- Sample Code
- Integration Guide 