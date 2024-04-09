from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://schemas.openxmlformats.org/package/2006/relationships"


@dataclass
class Relationship:
    class Meta:
        namespace = (
            "http://schemas.openxmlformats.org/package/2006/relationships"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    target: Optional[str] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Relationships:
    class Meta:
        namespace = (
            "http://schemas.openxmlformats.org/package/2006/relationships"
        )

    relationship: List[Relationship] = field(
        default_factory=list,
        metadata={
            "name": "Relationship",
            "type": "Element",
            "min_occurs": 1,
        },
    )
