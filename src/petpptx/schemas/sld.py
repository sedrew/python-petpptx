from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.formats.dataclass.models.generics import AnyElement


@dataclass
class CreationId:
    class Meta:
        name = "creationId"
        namespace = "http://schemas.microsoft.com/office/powerpoint/2010/main"

    val: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


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
class EndParaRpr:
    class Meta:
        name = "endParaRPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    dirty: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Ext2:
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
class RPr:
    class Meta:
        name = "rPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    dirty: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    smt_clean: Optional[int] = field(
        default=None,
        metadata={
            "name": "smtClean",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SpLocks:
    class Meta:
        name = "spLocks"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    no_grp: Optional[int] = field(
        default=None,
        metadata={
            "name": "noGrp",
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
    name: Optional[str] = field(
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
class Ph:
    class Meta:
        name = "ph"
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
    idx: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class R:
    class Meta:
        name = "r"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    r_pr: Optional[RPr] = field(
        default=None,
        metadata={
            "name": "rPr",
            "type": "Element",
            "required": True,
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
    ext: Optional[Ext2] = field(
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
class CNvSpPr:
    class Meta:
        name = "cNvSpPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    sp_locks: Optional[SpLocks] = field(
        default=None,
        metadata={
            "name": "spLocks",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )


@dataclass
class Ext1:
    class Meta:
        name = "ext"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    creation_id: Optional[CreationId] = field(
        default=None,
        metadata={
            "name": "creationId",
            "type": "Element",
            "namespace": "http://schemas.microsoft.com/office/powerpoint/2010/main",
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
class NvPr:
    class Meta:
        name = "nvPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    ph: Optional[Ph] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class P:
    class Meta:
        name = "p"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    r: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    end_para_rpr: Optional[EndParaRpr] = field(
        default=None,
        metadata={
            "name": "endParaRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ExtLst:
    class Meta:
        name = "extLst"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    ext: Optional[Ext1] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
class NvSpPr:
    class Meta:
        name = "nvSpPr"
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
    c_nv_sp_pr: Optional[CNvSpPr] = field(
        default=None,
        metadata={
            "name": "cNvSpPr",
            "type": "Element",
            "required": True,
        },
    )
    nv_pr: Optional[NvPr] = field(
        default=None,
        metadata={
            "name": "nvPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TxBody:
    class Meta:
        name = "txBody"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    body_pr: Optional[object] = field(
        default=None,
        metadata={
            "name": "bodyPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
        },
    )
    lst_style: Optional[object] = field(
        default=None,
        metadata={
            "name": "lstStyle",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
        },
    )
    p: Optional[P] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )


@dataclass
class Sp:
    class Meta:
        name = "sp"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    nv_sp_pr: Optional[NvSpPr] = field(
        default=None,
        metadata={
            "name": "nvSpPr",
            "type": "Element",
            "required": True,
        },
    )
    sp_pr: Optional[object] = field(
        default=None,
        metadata={
            "name": "spPr",
            "type": "Element",
        },
    )
    tx_body: Optional[TxBody] = field(
        default=None,
        metadata={
            "name": "txBody",
            "type": "Element",
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
    sp: List[Sp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class CSld:
    class Meta:
        name = "cSld"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    sp_tree: Optional[SpTree] = field(
        default=None,
        metadata={
            "name": "spTree",
            "type": "Element",
            "required": True,
        },
    )
    ext_lst: Optional[ExtLst] = field(
        default=None,
        metadata={
            "name": "extLst",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Sld:
    class Meta:
        name = "sld"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
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

    any_elements: List[AnyElement] = field(
        default_factory=list,
        metadata={
            "wildcard": True,
            "namespace": "##any",
            "keep": True}
    )


