# CWR Field Specifications

This document describes the field specifications for CWR records in versions 2.1 and 2.2.

## Record Types

### HDR (Header) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'HDR' |
| 4-5      | 2      | Sender Type | Alphanumeric | PB (Publisher), SO (Society), WR (Writer), AA (Administrative Agency) |
| 6-14     | 9      | Sender ID | Numeric | ID of the sender |
| 15-59    | 45     | Sender Name | Alphanumeric | Name of the sender |
| 60-67    | 8      | Creation Date | Numeric | YYYYMMDD |
| 68-75    | 8      | Creation Time | Numeric | HHMMSS00 |
| 76-83    | 8      | Transmission Date | Numeric | YYYYMMDD |
| 84-90    | 7      | Character Set | Alphanumeric | ASCII or other character set |
| 91-94    | 4      | Version Number | Numeric | 02.10 for v2.1, 02.20 for v2.2 |

### GRH (Group Header) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'GRH' |
| 4-6      | 3      | Transaction Type | Alphanumeric | NWR, REV, ISW, etc. |
| 7-11     | 5      | Group ID | Numeric | Unique group identifier |
| 12-15    | 4      | Version Number | Numeric | 02.10 for v2.1, 02.20 for v2.2 |
| 16       | 1      | Batch Request ID | Alphanumeric | Identifier for batch processing |

### GRT (Group Trailer) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'GRT' |
| 4-8      | 5      | Group ID | Numeric | Group identifier (same as GRH) |
| 9-13     | 5      | Transaction Count | Numeric | Number of transactions in the group |
| 14-21    | 8      | Record Count | Numeric | Number of records in the group |

### TRL (Trailer) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'TRL' |
| 4-8      | 5      | Group Count | Numeric | Number of groups in the file |
| 9-13     | 5      | Transaction Count | Numeric | Number of transactions in the file |
| 14-21    | 8      | Record Count | Numeric | Number of records in the file |

### WRK (Work Registration) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'WRK' |
| 4-8      | 5      | Transaction Sequence | Numeric | Transaction sequence number |
| 9-11     | 3      | Record Sequence | Numeric | Record sequence number |
| 12-25    | 14     | Submitter Work Number | Alphanumeric | Submitter's identifier for the work |
| 26-85    | 60     | Title | Alphanumeric | Title of the work |
| 86-87    | 2      | Language Code | Alphanumeric | Language code (ISO 639-1) |
| 88-109   | 22     | Work Type Code | Alphanumeric | Type of work (e.g., 'POP' for popular music) |
| 110-114  | 5      | Duration | Numeric | Duration in hours, minutes, seconds (HHMMSS) |
| 115-138  | 24     | Catalogue Number | Alphanumeric | Catalogue number for the work |
| 139-158  | 20     | ISWC | Alphanumeric | International Standard Musical Work Code |
| 159      | 1      | Recorded Indicator | Alphanumeric | 'Y' if the work has been recorded, 'N' if not |
| 160-167  | 8      | Text Music Relationship | Alphanumeric | Relationship between text and music |
| 168-171  | 4      | Composite Type | Alphanumeric | Type of composite work |
| 172-175  | 4      | Version Type | Alphanumeric | Type of version (e.g., 'ORI' for original) |
| 176-179  | 4      | Excerpt Type | Alphanumeric | Type of excerpt |
| 180-183  | 4      | Music Arrangement | Alphanumeric | Type of music arrangement |
| 184-187  | 4      | Lyric Adaptation | Alphanumeric | Type of lyric adaptation |
| 188      | 1      | Grand Rights Indicator | Alphanumeric | 'Y' for grand rights work, 'N' otherwise |
| 189-192  | 4      | Composite Component Count | Numeric | Number of components in a composite work |

### ALT (Alternative Title) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'ALT' |
| 4-8      | 5      | Transaction Sequence | Numeric | Transaction sequence number |
| 9-11     | 3      | Record Sequence | Numeric | Record sequence number |
| 12-71    | 60     | Title | Alphanumeric | Alternative title of the work |
| 72-73    | 2      | Title Type | Alphanumeric | Type of title (e.g., 'AT' for alternative) |
| 74-75    | 2      | Language Code | Alphanumeric | Language code (ISO 639-1) |

### SWR (Submitter Writer) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'SWR' |
| 4-8      | 5      | Transaction Sequence | Numeric | Transaction sequence number |
| 9-11     | 3      | Record Sequence | Numeric | Record sequence number |
| 12-25    | 14     | Interested Party Number | Alphanumeric | Identifier for the writer |
| 26-45    | 20     | Writer Last Name | Alphanumeric | Last name of the writer |
| 46-75    | 30     | Writer First Name | Alphanumeric | First name of the writer |
| 76       | 1      | Writer Unknown Indicator | Alphanumeric | 'Y' if writer is unknown, 'N' otherwise |
| 77-78    | 2      | Writer Role | Alphanumeric | Role of the writer (e.g., 'CA' for composer/author) |
| 79-84    | 6      | PR Ownership Share | Numeric | Performing rights ownership share (percentage) |
| 85-90    | 6      | MR Ownership Share | Numeric | Mechanical rights ownership share (percentage) |
| 91-96    | 6      | SR Ownership Share | Numeric | Synchronization rights ownership share (percentage) |

### SWT (Writer Territory) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'SWT' |
| 4-8      | 5      | Transaction Sequence | Numeric | Transaction sequence number |
| 9-11     | 3      | Record Sequence | Numeric | Record sequence number |
| 12-25    | 14     | Interested Party Number | Alphanumeric | Identifier for the writer (same as SWR) |
| 26       | 1      | Sequence Number | Numeric | Sequence number for multiple SWT records |
| 27       | 1      | Inclusion/Exclusion Indicator | Alphanumeric | 'I' for inclusion, 'E' for exclusion |
| 28-31    | 4      | Territory Code | Numeric | Territory code (from TIS table) |
| 32-37    | 6      | PR Collection Share | Numeric | Performing rights collection share (percentage) |
| 38-43    | 6      | MR Collection Share | Numeric | Mechanical rights collection share (percentage) |
| 44-49    | 6      | SR Collection Share | Numeric | Synchronization rights collection share (percentage) |

### SPU (Submitter Publisher) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'SPU' |
| 4-8      | 5      | Transaction Sequence | Numeric | Transaction sequence number |
| 9-11     | 3      | Record Sequence | Numeric | Record sequence number |
| 12-13    | 2      | Publisher Sequence | Numeric | Sequence number for multiple publishers |
| 14-27    | 14     | Interested Party Number | Alphanumeric | Identifier for the publisher |
| 28-87    | 60     | Publisher Name | Alphanumeric | Name of the publisher |
| 88       | 1      | Publisher Type | Alphanumeric | Type of publisher (e.g., 'E' for original publisher) |
| 89       | 1      | Publisher Unknown Indicator | Alphanumeric | 'Y' if publisher is unknown, 'N' otherwise |
| 90-91    | 2      | Publisher Role | Alphanumeric | Role of the publisher |
| 92-97    | 6      | PR Ownership Share | Numeric | Performing rights ownership share (percentage) |
| 98-103   | 6      | MR Ownership Share | Numeric | Mechanical rights ownership share (percentage) |
| 104-109  | 6      | SR Ownership Share | Numeric | Synchronization rights ownership share (percentage) |

### SPT (Publisher Territory) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'SPT' |
| 4-8      | 5      | Transaction Sequence | Numeric | Transaction sequence number |
| 9-11     | 3      | Record Sequence | Numeric | Record sequence number |
| 12-13    | 2      | Publisher Sequence | Numeric | Sequence number (same as SPU) |
| 14       | 1      | Sequence Number | Numeric | Sequence number for multiple SPT records |
| 15       | 1      | Inclusion/Exclusion Indicator | Alphanumeric | 'I' for inclusion, 'E' for exclusion |
| 16-19    | 4      | Territory Code | Numeric | Territory code (from TIS table) |
| 20-25    | 6      | PR Collection Share | Numeric | Performing rights collection share (percentage) |
| 26-31    | 6      | MR Collection Share | Numeric | Mechanical rights collection share (percentage) |
| 32-37    | 6      | SR Collection Share | Numeric | Synchronization rights collection share (percentage) |

### PER (Performing Artist) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'PER' |
| 4-8      | 5      | Transaction Sequence | Numeric | Transaction sequence number |
| 9-11     | 3      | Record Sequence | Numeric | Record sequence number |
| 12-51    | 40     | Performing Artist Last Name | Alphanumeric | Last name of the performing artist |
| 52-81    | 30     | Performing Artist First Name | Alphanumeric | First name of the performing artist |
| 82-92    | 11     | Performing Artist IPI Name Number | Numeric | IPI name number for the performing artist |
| 93-105   | 13     | Performing Artist IPI Base Number | Numeric | IPI base number for the performing artist |

### REC (Recording Detail) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'REC' |
| 4-8      | 5      | Transaction Sequence | Numeric | Transaction sequence number |
| 9-11     | 3      | Record Sequence | Numeric | Record sequence number |
| 12-71    | 60     | Recording Title | Alphanumeric | Title of the recording |
| 72-131   | 60     | Version Title | Alphanumeric | Title of the version |
| 132-181  | 50     | Display Artist | Alphanumeric | Display artist for the recording |
| 182-201  | 20     | Recording ID | Alphanumeric | Identifier for the recording |
| 202-213  | 12     | ISRC | Alphanumeric | International Standard Recording Code |
| 214      | 1      | Recording Format | Alphanumeric | Format of the recording (e.g., 'A' for audio) |
| 215-219  | 5      | Recording Duration | Numeric | Duration in hours, minutes, seconds (HHMMSS) |
| 220-227  | 8      | Release Date | Numeric | Release date (YYYYMMDD) |

### ORN (Work Origin) Record

| Position | Length | Field | Format | Description |
|----------|--------|-------|--------|-------------|
| 1-3      | 3      | Record Type | Alphanumeric | Always 'ORN' |
| 4-8      | 5      | Transaction Sequence | Numeric | Transaction sequence number |
| 9-11     | 3      | Record Sequence | Numeric | Record sequence number |
| 12-15    | 4      | Intended Purpose | Alphanumeric | Intended purpose of the work (e.g., 'FIL' for film) |
| 16-75    | 60     | Production Title | Alphanumeric | Title of the production |
| 76-95    | 20     | CD Identifier | Alphanumeric | Identifier for the CD |
| 96-99    | 4      | Cut Number | Numeric | Cut number on the CD |
| 100-159  | 60     | Library | Alphanumeric | Library name |
| 160      | 1      | BLTVR | Alphanumeric | Background (B), Logo (L), Theme (T), etc. |
| 161-164  | 4      | Production Year | Numeric | Year of production (YYYY) |
| 165-224  | 60     | Episode Title | Alphanumeric | Title of the episode |
| 225-228  | 4      | Episode Number | Numeric | Episode number |

## Lookup Tables

The CWR format uses various lookup tables for field validation. The following tables are used in CWR 2.1 and 2.2:

### Agreement Type

| Code | Definition |
|------|------------|
| OS   | Original Specific |
| PS   | Subpublishing Specific |
| PG   | Subpublishing General |
| OG   | Original General |

### BLTVR (Background, Logo, Theme, Visual, Rolled up Cue)

| Code | Definition |
|------|------------|
| B    | Background |
| L    | Logo |
| R    | Rolled up Cue |
| T    | Theme |
| V    | Visual |

### Composite Type

| Code | Definition |
|------|------------|
| COS  | Composite of Samples |
| MED  | Medley |
| POT  | Potpourri |
| UCO  | Unspecified Composite |

### Excerpt Type

| Code | Definition |
|------|------------|
| MOV  | Movement |
| UEX  | Unspecified Excerpt |

### Intended Purpose

| Code | Definition |
|------|------------|
| COM  | Commercial / Jingle / Trailer |
| FIL  | Film |
| GEN  | General Usage |
| LIB  | Library Work |
| MUL  | Multimedia |
| RAD  | Radio |
| TEL  | Television |
| THR  | Theatre |
| VID  | Video |

### Lyric Adaptation

| Code | Definition |
|------|------------|
| NEW  | New |
| MOD  | Modification |
| NON  | None |
| ORI  | Original |
| REP  | Replacement |
| ADL  | Addition |
| UNS  | Unspecified |
| TRA  | Translation |

### Music Arrangement

| Code | Definition |
|------|------------|
| NEW  | New |
| ARR  | Arrangement |
| ADM  | Addition |
| UNS  | Unspecified arrangement |
| ORI  | Original |

### Musical Work Distribution Category

| Code | Definition |
|------|------------|
| JAZ  | Jazz |
| POP  | Popular |
| SER  | Serious |
| UNC  | Unclassified Distribution Category |

### Publisher Type

| Code | Definition |
|------|------------|
| AQ   | Acquirer |
| AM   | Administrator |
| PA   | Income Participant |
| E    | Original Publisher |
| ES   | Substituted Publisher |
| SE   | Sub Publisher |

### Version Type

| Code | Definition |
|------|------------|
| MOD  | Modified Version |
| ORI  | Original Version |
| ADM  | Additional Music |
| ADL  | Additional Lyrics |

### Writer Role

| Code | Definition |
|------|------------|
| A    | Author |
| AD   | Adapter |
| AR   | Arranger |
| C    | Composer |
| CA   | Composer/Author |
| SA   | Sub-Author |
| SR   | Sub-Arranger |
| TR   | Translator | 