from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ChExt:
    class Meta:
        name = "chExt"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

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
class ChOff:
    class Meta:
        name = "chOff"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

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
class Ext:
    class Meta:
        name = "ext"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

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
class Off:
    class Meta:
        name = "off"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

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
class CNvPr:
    class Meta:
        name = "cNvPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ClrMapOvr:
    class Meta:
        name = "clrMapOvr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    master_clr_mapping: Optional[object] = field(
        default=None,
        metadata={
            "name": "masterClrMapping",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
        },
    )


@dataclass
class Xfrm:
    class Meta:
        name = "xfrm"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    off: Optional[Off] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ext: Optional[Ext] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ch_off: Optional[ChOff] = field(
        default=None,
        metadata={
            "name": "chOff",
            "type": "Element",
            "required": True,
        },
    )
    ch_ext: Optional[ChExt] = field(
        default=None,
        metadata={
            "name": "chExt",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class NvGrpSpPr:
    class Meta:
        name = "nvGrpSpPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    c_nv_pr: Optional[CNvPr] = field(
        default=None,
        metadata={
            "name": "cNvPr",
            "type": "Element",
            "required": True,
        },
    )
    c_nv_grp_sp_pr: Optional[object] = field(
        default=None,
        metadata={
            "name": "cNvGrpSpPr",
            "type": "Element",
        },
    )
    nv_pr: Optional[object] = field(
        default=None,
        metadata={
            "name": "nvPr",
            "type": "Element",
        },
    )


@dataclass
class GrpSpPr:
    class Meta:
        name = "grpSpPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    xfrm: Optional[Xfrm] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )


@dataclass
class SpTree:
    class Meta:
        name = "spTree"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    nv_grp_sp_pr: Optional[NvGrpSpPr] = field(
        default=None,
        metadata={
            "name": "nvGrpSpPr",
            "type": "Element",
            "required": True,
        },
    )
    grp_sp_pr: Optional[GrpSpPr] = field(
        default=None,
        metadata={
            "name": "grpSpPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CSld:
    class Meta:
        name = "cSld"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    sp_tree: Optional[SpTree] = field(
        default=None,
        metadata={
            "name": "spTree",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SldLayout:
    class Meta:
        name = "sldLayout"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    preserve: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    c_sld: Optional[CSld] = field(
        default=None,
        metadata={
            "name": "cSld",
            "type": "Element",
            "required": True,
        },
    )
    clr_map_ovr: Optional[ClrMapOvr] = field(
        default=None,
        metadata={
            "name": "clrMapOvr",
            "type": "Element",
            "required": True,
        },
    )
