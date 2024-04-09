from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDateTime


@dataclass
class Created:
    class Meta:
        name = "created"
        namespace = "http://purl.org/dc/terms/"

    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        },
    )
    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Modified:
    class Meta:
        name = "modified"
        namespace = "http://purl.org/dc/terms/"

    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        },
    )
    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class CoreProperties:
    class Meta:
        name = "coreProperties"
        namespace = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "required": True,
        },
    )
    subject: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        },
    )
    creator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "required": True,
        },
    )
    keywords: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        },
    )
    last_modified_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModifiedBy",
            "type": "Element",
            "required": True,
        },
    )
    revision: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    created: Optional[Created] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "required": True,
        },
    )
    modified: Optional[Modified] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "required": True,
        },
    )
    category: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
