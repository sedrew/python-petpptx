from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Sx:
    class Meta:
        name = "sx"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    n: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Sy:
    class Meta:
        name = "sy"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    n: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    d: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GridSpacing:
    class Meta:
        name = "gridSpacing"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    cx: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    cy: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Guide:
    class Meta:
        name = "guide"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    orient: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Origin:
    class Meta:
        name = "origin"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    x: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RestoredLeft:
    class Meta:
        name = "restoredLeft"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    sz: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RestoredTop:
    class Meta:
        name = "restoredTop"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    sz: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GuideLst:
    class Meta:
        name = "guideLst"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    guide: List[Guide] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class NormalViewPr:
    class Meta:
        name = "normalViewPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    restored_left: Optional[RestoredLeft] = field(
        default=None,
        metadata={
            "name": "restoredLeft",
            "type": "Element",
            "required": True,
        },
    )
    restored_top: Optional[RestoredTop] = field(
        default=None,
        metadata={
            "name": "restoredTop",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Scale:
    class Meta:
        name = "scale"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    sx: Optional[Sx] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    sy: Optional[Sy] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )


@dataclass
class CViewPr:
    class Meta:
        name = "cViewPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    var_scale: Optional[int] = field(
        default=None,
        metadata={
            "name": "varScale",
            "type": "Attribute",
        },
    )
    scale: Optional[Scale] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CSldViewPr:
    class Meta:
        name = "cSldViewPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    c_view_pr: Optional[CViewPr] = field(
        default=None,
        metadata={
            "name": "cViewPr",
            "type": "Element",
            "required": True,
        },
    )
    guide_lst: Optional[GuideLst] = field(
        default=None,
        metadata={
            "name": "guideLst",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class NotesTextViewPr:
    class Meta:
        name = "notesTextViewPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    c_view_pr: Optional[CViewPr] = field(
        default=None,
        metadata={
            "name": "cViewPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SlideViewPr:
    class Meta:
        name = "slideViewPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    c_sld_view_pr: Optional[CSldViewPr] = field(
        default=None,
        metadata={
            "name": "cSldViewPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ViewPr:
    class Meta:
        name = "viewPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    normal_view_pr: Optional[NormalViewPr] = field(
        default=NormalViewPr(restored_left=RestoredLeft(sz=15620), restored_top=RestoredTop(sz=94660)),
        metadata={
            "name": "normalViewPr",
            "type": "Element",
            "required": True,
        },
    )
    slide_view_pr: Optional[SlideViewPr] = field(
        default=None,
        metadata={
            "name": "slideViewPr",
            "type": "Element",
            "required": True,
        },
    )
    notes_text_view_pr: Optional[NotesTextViewPr] = field(
        default=None,
        metadata={
            "name": "notesTextViewPr",
            "type": "Element",
            "required": True,
        },
    )
    grid_spacing: Optional[GridSpacing] = field(
        default=None,
        metadata={
            "name": "gridSpacing",
            "type": "Element",
            "required": True,
        },
    )
