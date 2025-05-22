"""
CWR Record Models - Defines data models for CWR record types.
"""
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import datetime


@dataclass
class BaseRecord:
    """Base class for all CWR record types."""
    record_type: str
    record_sequence: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        return {
            'record_type': self.record_type,
            'record_sequence': self.record_sequence
        }


@dataclass
class HeaderRecord(BaseRecord):
    """HDR (Header) record for CWR files."""
    record_type: str = 'HDR'
    sender_type: str = ''  # Publisher (PB), Society (SO), Writer (WR), Administrative Agency (AA)
    sender_id: str = ''
    sender_name: str = ''
    edi_standard: str = 'CWR'
    creation_date: str = ''  # YYYYMMDD
    creation_time: str = ''  # HHMMSS
    transmission_date: str = ''  # YYYYMMDD
    character_set: str = 'ASCII'
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'sender_type': self.sender_type,
            'sender_id': self.sender_id,
            'sender_name': self.sender_name,
            'edi_standard': self.edi_standard,
            'creation_date': self.creation_date,
            'creation_time': self.creation_time,
            'transmission_date': self.transmission_date,
            'character_set': self.character_set
        })
        return data


@dataclass
class GroupHeaderRecord(BaseRecord):
    """GRH (Group Header) record for CWR files."""
    record_type: str = 'GRH'
    transaction_type: str = ''  # NWR, REV, etc.
    group_id: str = ''
    version_number: str = ''
    batch_request_id: str = ''
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_type': self.transaction_type,
            'group_id': self.group_id,
            'version_number': self.version_number,
            'batch_request_id': self.batch_request_id
        })
        return data


@dataclass
class GroupTrailerRecord(BaseRecord):
    """GRT (Group Trailer) record for CWR files."""
    record_type: str = 'GRT'
    group_id: str = ''
    transaction_count: int = 0
    record_count: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'group_id': self.group_id,
            'transaction_count': self.transaction_count,
            'record_count': self.record_count
        })
        return data


@dataclass
class TrailerRecord(BaseRecord):
    """TRL (Trailer) record for CWR files."""
    record_type: str = 'TRL'
    group_count: int = 0
    transaction_count: int = 0
    record_count: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'group_count': self.group_count,
            'transaction_count': self.transaction_count,
            'record_count': self.record_count
        })
        return data


@dataclass
class WorkRegistrationRecord(BaseRecord):
    """WRK (Work Registration) transaction header record."""
    record_type: str = 'WRK'
    transaction_sequence: int = 0
    record_sequence: int = 0
    submitter_work_number: str = ''
    title: str = ''
    language_code: str = ''
    work_type_code: str = ''
    duration: Optional[int] = None  # Duration in seconds
    catalogue_number: str = ''
    opus_number: str = ''
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_sequence': self.transaction_sequence,
            'submitter_work_number': self.submitter_work_number,
            'title': self.title,
            'language_code': self.language_code,
            'work_type_code': self.work_type_code,
            'duration': self.duration,
            'catalogue_number': self.catalogue_number,
            'opus_number': self.opus_number
        })
        return data


@dataclass
class AlternativeTitleRecord(BaseRecord):
    """ALT (Alternative Title) record."""
    record_type: str = 'ALT'
    transaction_sequence: int = 0
    record_sequence: int = 0
    title: str = ''
    title_type: str = ''  # OT (Original), AT (Alternative), etc.
    language_code: str = ''
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_sequence': self.transaction_sequence,
            'title': self.title,
            'title_type': self.title_type,
            'language_code': self.language_code
        })
        return data


@dataclass
class SubmitterWriterRecord(BaseRecord):
    """SWR (Submitter Writer) record."""
    record_type: str = 'SWR'
    transaction_sequence: int = 0
    record_sequence: int = 0
    interested_party_number: str = ''
    writer_id: str = ''
    last_name: str = ''
    first_name: str = ''
    writer_unknown: bool = False
    writer_role: str = ''  # C (Composer), A (Author), CA (Composer/Author), etc.
    pr_ownership_share: float = 0.0  # Percentage (0-100)
    mr_ownership_share: float = 0.0  # Percentage (0-100)
    sr_ownership_share: float = 0.0  # Percentage (0-100)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_sequence': self.transaction_sequence,
            'interested_party_number': self.interested_party_number,
            'writer_id': self.writer_id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'writer_unknown': self.writer_unknown,
            'writer_role': self.writer_role,
            'pr_ownership_share': self.pr_ownership_share,
            'mr_ownership_share': self.mr_ownership_share,
            'sr_ownership_share': self.sr_ownership_share
        })
        return data


@dataclass
class WriterTerritoryRecord(BaseRecord):
    """SWT (Writer Territory) record."""
    record_type: str = 'SWT'
    transaction_sequence: int = 0
    record_sequence: int = 0
    interested_party_number: str = ''
    territory_code: str = ''
    pr_collection_share: float = 0.0  # Percentage (0-100)
    mr_collection_share: float = 0.0  # Percentage (0-100)
    sr_collection_share: float = 0.0  # Percentage (0-100)
    inclusion_exclusion_indicator: str = ''  # I (Include) or E (Exclude)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_sequence': self.transaction_sequence,
            'interested_party_number': self.interested_party_number,
            'territory_code': self.territory_code,
            'pr_collection_share': self.pr_collection_share,
            'mr_collection_share': self.mr_collection_share,
            'sr_collection_share': self.sr_collection_share,
            'inclusion_exclusion_indicator': self.inclusion_exclusion_indicator
        })
        return data


@dataclass
class SubmitterPublisherRecord(BaseRecord):
    """SPU (Submitter Publisher) record."""
    record_type: str = 'SPU'
    transaction_sequence: int = 0
    record_sequence: int = 0
    publisher_sequence: int = 0
    publisher_id: str = ''
    publisher_name: str = ''
    publisher_type: str = ''  # E (Original), AM (Administrator), etc.
    publisher_unknown: bool = False
    publisher_role: str = ''
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_sequence': self.transaction_sequence,
            'publisher_sequence': self.publisher_sequence,
            'publisher_id': self.publisher_id,
            'publisher_name': self.publisher_name,
            'publisher_type': self.publisher_type,
            'publisher_unknown': self.publisher_unknown,
            'publisher_role': self.publisher_role
        })
        return data


@dataclass
class PublisherTerritoryRecord(BaseRecord):
    """SPT (Publisher Territory) record."""
    record_type: str = 'SPT'
    transaction_sequence: int = 0
    record_sequence: int = 0
    publisher_sequence: int = 0
    territory_code: str = ''
    pr_collection_share: float = 0.0  # Percentage (0-100)
    mr_collection_share: float = 0.0  # Percentage (0-100)
    sr_collection_share: float = 0.0  # Percentage (0-100)
    inclusion_exclusion_indicator: str = ''  # I (Include) or E (Exclude)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_sequence': self.transaction_sequence,
            'publisher_sequence': self.publisher_sequence,
            'territory_code': self.territory_code,
            'pr_collection_share': self.pr_collection_share,
            'mr_collection_share': self.mr_collection_share,
            'sr_collection_share': self.sr_collection_share,
            'inclusion_exclusion_indicator': self.inclusion_exclusion_indicator
        })
        return data


@dataclass
class PerformingArtistRecord(BaseRecord):
    """PER (Performing Artist) record."""
    record_type: str = 'PER'
    transaction_sequence: int = 0
    record_sequence: int = 0
    performing_artist_last_name: str = ''
    performing_artist_first_name: str = ''
    performing_artist_ipi_name_number: str = ''
    performing_artist_ipi_base_number: str = ''
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_sequence': self.transaction_sequence,
            'performing_artist_last_name': self.performing_artist_last_name,
            'performing_artist_first_name': self.performing_artist_first_name,
            'performing_artist_ipi_name_number': self.performing_artist_ipi_name_number,
            'performing_artist_ipi_base_number': self.performing_artist_ipi_base_number
        })
        return data


@dataclass
class RecordingDetailRecord(BaseRecord):
    """REC (Recording Detail) record."""
    record_type: str = 'REC'
    transaction_sequence: int = 0
    record_sequence: int = 0
    recording_title: str = ''
    version_title: str = ''
    recording_label: str = ''
    recording_id: str = ''
    isrc: str = ''
    recording_format: str = ''
    recording_duration: Optional[int] = None  # Duration in seconds
    release_date: Optional[str] = None  # YYYYMMDD
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_sequence': self.transaction_sequence,
            'recording_title': self.recording_title,
            'version_title': self.version_title,
            'recording_label': self.recording_label,
            'recording_id': self.recording_id,
            'isrc': self.isrc,
            'recording_format': self.recording_format,
            'recording_duration': self.recording_duration,
            'release_date': self.release_date
        })
        return data


@dataclass
class WorkOriginRecord(BaseRecord):
    """ORN (Work Origin) record."""
    record_type: str = 'ORN'
    transaction_sequence: int = 0
    record_sequence: int = 0
    intended_purpose: str = ''
    production_title: str = ''
    cd_identifier: str = ''
    cut_number: Optional[int] = None
    library: str = ''
    bltvr: str = ''  # Background (B), Logo (L), Theme (T), etc.
    production_year: Optional[int] = None
    episode_title: str = ''
    episode_number: Optional[int] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the record to a dictionary."""
        data = super().to_dict()
        data.update({
            'transaction_sequence': self.transaction_sequence,
            'intended_purpose': self.intended_purpose,
            'production_title': self.production_title,
            'cd_identifier': self.cd_identifier,
            'cut_number': self.cut_number,
            'library': self.library,
            'bltvr': self.bltvr,
            'production_year': self.production_year,
            'episode_title': self.episode_title,
            'episode_number': self.episode_number
        })
        return data


@dataclass
class CWRTransaction:
    """Represents a CWR transaction (a group of related records)."""
    transaction_type: str
    transaction_sequence: int = 0
    header_record: Optional[Any] = None
    records: List[BaseRecord] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the transaction to a dictionary."""
        return {
            'transaction_type': self.transaction_type,
            'transaction_sequence': self.transaction_sequence,
            'header': self.header_record.to_dict() if self.header_record else None,
            'records': [record.to_dict() for record in self.records]
        }


@dataclass
class CWRFile:
    """Represents a complete CWR file."""
    header: HeaderRecord
    group_header: GroupHeaderRecord
    transactions: List[CWRTransaction] = field(default_factory=list)
    group_trailer: Optional[GroupTrailerRecord] = None
    trailer: Optional[TrailerRecord] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the CWR file to a dictionary."""
        return {
            'header': self.header.to_dict(),
            'group_header': self.group_header.to_dict(),
            'transactions': [transaction.to_dict() for transaction in self.transactions],
            'group_trailer': self.group_trailer.to_dict() if self.group_trailer else None,
            'trailer': self.trailer.to_dict() if self.trailer else None
        } 