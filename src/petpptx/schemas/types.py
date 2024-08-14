from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://schemas.openxmlformats.org/package/2006/content-types"

from src.petpptx.schemas.base_schema import BaseSchema


@dataclass
class Default(BaseSchema):
    class Meta:
        namespace = (
            "http://schemas.openxmlformats.org/package/2006/content-types"
        )

    extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "required": True,
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContentType",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Override(BaseSchema):
    class Meta:
        namespace = (
            "http://schemas.openxmlformats.org/package/2006/content-types"
        )

    part_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartName",
            "type": "Attribute",
            "required": True,
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContentType",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Types(BaseSchema):
    class Meta:
        namespace = (
            "http://schemas.openxmlformats.org/package/2006/content-types"
        )

    default: List[Default] = field(
        default_factory=list,
        metadata={
            "name": "Default",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    override: List[Override] = field(
        default_factory=list,
        metadata={
            "name": "Override",
            "type": "Element",
            "min_occurs": 1,
        },
    )
