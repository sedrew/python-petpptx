from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class Variant:
    class Meta:
        name = "variant"
        namespace = "http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"

    i4: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lpstr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Vector:
    class Meta:
        name = "vector"
        namespace = "http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"

    size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    base_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseType",
            "type": "Attribute",
            "required": True,
        },
    )
    lpstr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variant: List[Variant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class HeadingPairs:
    class Meta:
        namespace = "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"

    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes",
            "required": True,
        },
    )


@dataclass
class TitlesOfParts:
    class Meta:
        namespace = "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"

    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes",
            "required": True,
        },
    )


@dataclass
class Properties:
    class Meta:
        namespace = "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"

    total_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalTime",
            "type": "Element",
            "required": True,
        },
    )
    words: Optional[int] = field(
        default=None,
        metadata={
            "name": "Words",
            "type": "Element",
            "required": True,
        },
    )
    application: Optional[str] = field(
        default=None,
        metadata={
            "name": "Application",
            "type": "Element",
            "required": True,
        },
    )
    presentation_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresentationFormat",
            "type": "Element",
            "required": True,
        },
    )
    paragraphs: Optional[int] = field(
        default=None,
        metadata={
            "name": "Paragraphs",
            "type": "Element",
            "required": True,
        },
    )
    slides: Optional[int] = field(
        default=None,
        metadata={
            "name": "Slides",
            "type": "Element",
            "required": True,
        },
    )
    notes: Optional[int] = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "required": True,
        },
    )
    hidden_slides: Optional[int] = field(
        default=None,
        metadata={
            "name": "HiddenSlides",
            "type": "Element",
            "required": True,
        },
    )
    mmclips: Optional[int] = field(
        default=None,
        metadata={
            "name": "MMClips",
            "type": "Element",
            "required": True,
        },
    )
    scale_crop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ScaleCrop",
            "type": "Element",
            "required": True,
        },
    )
    heading_pairs: Optional[HeadingPairs] = field(
        default=None,
        metadata={
            "name": "HeadingPairs",
            "type": "Element",
            "required": True,
        },
    )
    titles_of_parts: Optional[TitlesOfParts] = field(
        default=None,
        metadata={
            "name": "TitlesOfParts",
            "type": "Element",
            "required": True,
        },
    )
    manager: Optional[object] = field(
        default=None,
        metadata={
            "name": "Manager",
            "type": "Element",
        },
    )
    company: Optional[str] = field(
        default=None,
        metadata={
            "name": "Company",
            "type": "Element",
            "required": True,
        },
    )
    links_up_to_date: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LinksUpToDate",
            "type": "Element",
            "required": True,
        },
    )
    shared_doc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SharedDoc",
            "type": "Element",
            "required": True,
        },
    )
    hyperlink_base: Optional[object] = field(
        default=None,
        metadata={
            "name": "HyperlinkBase",
            "type": "Element",
        },
    )
    hyperlinks_changed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HyperlinksChanged",
            "type": "Element",
            "required": True,
        },
    )
    app_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AppVersion",
            "type": "Element",
            "required": True,
        },
    )
