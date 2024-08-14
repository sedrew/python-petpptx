from dataclasses import dataclass, field
from typing import List, Optional, Union

from src.petpptx.schemas.base_schema import BaseSchema


@dataclass
class CreationId2:
    class Meta:
        name = "creationId"
        namespace = "http://schemas.microsoft.com/office/drawing/2014/main"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
    )


@dataclass
class CreationId1:
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

    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
    )


@dataclass
class ModId(BaseSchema):
    class Meta:
        name = "modId"
        namespace = "http://schemas.microsoft.com/office/powerpoint/2010/main"

    val: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Chart(BaseSchema):
    class Meta:
        name = "chart"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/chart"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
            "required": True,
        },
    )


@dataclass
class RelIds(BaseSchema):
    class Meta:
        name = "relIds"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/diagram"

    dm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
            "required": True,
        },
    )
    lo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
            "required": True,
        },
    )
    qs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
            "required": True,
        },
    )
    cs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
            "required": True,
        },
    )


@dataclass
class ChExt(BaseSchema):
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
class ChOff(BaseSchema):
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
class SchemeClr:
    class Meta:
        name = "schemeClr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SolidFill:
    class Meta:
        name = "solidFill"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    scheme_clr: Optional[SchemeClr] = field(
        default=None,
        metadata={
            "name": "schemeClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EndParaRpr:
    class Meta:
        name = "endParaRPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    solid_fill: Optional[SolidFill] = field(
        default=None,
        metadata={
            "name": "solidFill",
            "type": "Element",
            "required": True,
        },
    )

    # any_elements: list[object] = field(
    #     default_factory=list,
    #     metadata={
    #         "type": "Wildcard",
    #         "namespace": "##any"
    #     }
    # )

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
            "required": True,
        },
    )

    attrs: dict = field(default_factory=dict, metadata={"type": "Attributes"})


@dataclass
class NormAutofit(BaseSchema):
    class Meta:
        name = "normAutofit"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    font_scale: Optional[int] = field(
        default=None,
        metadata={
            "name": "fontScale",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Off(BaseSchema):
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
class PrstGeom(BaseSchema):
    class Meta:
        name = "prstGeom"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    prst: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    av_lst: Optional[object] = field(
        default=None,
        metadata={
            "name": "avLst",
            "type": "Element",
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

    # lang: List[Union[str]] = field(
    #     default_factory=list,
    #     metadata={
    #         "type": "Elements",
    #         "choices": (
    #             {"wildcard": True, "type": str},
    #             {"name": "lang", "type": str}
    #         )
    #     }
    # )

    attrs: dict = field(default_factory=dict, metadata={"type": "Attributes"})

    dirty: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
    )



@dataclass
class SpLocks(BaseSchema):
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
class ClrMapOvr(BaseSchema):
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
class Ph(BaseSchema):
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
class BodyPr:
    class Meta:
        name = "bodyPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    wrap: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rtl_col: Optional[int] = field(
        default=None,
        metadata={
            "name": "rtlCol",
            "type": "Attribute",
        },
    )
    sp_auto_fit: Optional[object] = field(
        default=None,
        metadata={
            "name": "spAutoFit",
            "type": "Element",
        },
    )
    norm_autofit: Optional[NormAutofit] = field(
        default=None,
        metadata={
            "name": "normAutofit",
            "type": "Element",
        },
    )

    attrs: dict = field(default_factory=dict, metadata={"type": "Attributes"})

    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
    )



@dataclass
class Ext2(BaseSchema):
    class Meta:
        name = "ext"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    cx: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cy: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    creation_id: Optional[CreationId2] = field(
        default=None,
        metadata={
            "name": "creationId",
            "type": "Element",
            "namespace": "http://schemas.microsoft.com/office/drawing/2014/main",
        },
    )


@dataclass
class GraphicData(BaseSchema):
    class Meta:
        name = "graphicData"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    rel_ids: Optional[RelIds] = field(
        default=None,
        metadata={
            "name": "relIds",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/diagram",
        },
    )
    chart: Optional[Chart] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/chart",
        },
    )


@dataclass
class R:
    class Meta:
        name = "r"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    r_pr: List[Union[RPr, str]] = field(  # TODO
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {"wildcard": True, "type": object},
                {"name": "rPr", "type": RPr},
                {"name": "t", "type": str},
            )
        }
    )

    # r_pr: Optional[RPr] = field(
    #     default=None,
    #     metadata={
    #         "name": "rPr",
    #         "type": "Element",
    #         "required": True,
    #     },
    # )

    # t: Optional[str] = field(
    #     default=None,
    #     metadata={
    #         "type": "Element",
    #         "required": True,
    #     },
    # )


@dataclass
class CNvSpPr(BaseSchema):
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
class Ext1(BaseSchema):
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
    creation_id: Optional[CreationId1] = field(
        default=None,
        metadata={
            "name": "creationId",
            "type": "Element",
            "namespace": "http://schemas.microsoft.com/office/powerpoint/2010/main",
        },
    )
    mod_id: Optional[ModId] = field(
        default=None,
        metadata={
            "name": "modId",
            "type": "Element",
            "namespace": "http://schemas.microsoft.com/office/powerpoint/2010/main",
        },
    )


@dataclass
class ExtLst2(BaseSchema):
    class Meta:
        name = "extLst"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    ext: Optional[Ext2] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Graphic(BaseSchema):
    class Meta:
        name = "graphic"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    graphic_data: Optional[GraphicData] = field(
        default=None,
        metadata={
            "name": "graphicData",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class P:
    class Meta:
        name = "p"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    # r: Optional[R] = field(
    #     default=None,
    #     metadata={
    #         "type": "Element",
    #         "required": True,
    #     },
    # )

    r: List[Union[R, EndParaRpr]] = field(  # TODO
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {"wildcard": True, "type": object},
                {"name": "r", "type": R},
                {"name": "endParaRPr", "type": EndParaRpr},
            )
        }
    )

    # end_para_rpr: Optional[EndParaRpr] = field(
    #     default=None,
    #     metadata={
    #         "name": "endParaRPr",
    #         "type": "Element",
    #     },
    # )

    attrs: dict = field(default_factory=dict, metadata={"type": "Attributes"})

    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
    )


@dataclass
class Xfrm1(BaseSchema):
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
        },
    )
    ch_ext: Optional[ChExt] = field(
        default=None,
        metadata={
            "name": "chExt",
            "type": "Element",
        },
    )


@dataclass
class ExtLst1(BaseSchema):
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
class Ext1(BaseSchema):
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
    creation_id: Optional[CreationId1] = field(
        default=None,
        metadata={
            "name": "creationId",
            "type": "Element",
            "namespace": "http://schemas.microsoft.com/office/powerpoint/2010/main",
            "required": True,
        },
    )


@dataclass
class Xfrm2(BaseSchema):
    class Meta:
        name = "xfrm"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    off: Optional[Off] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    ext: Optional[Ext2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )


@dataclass
class CNvPr(BaseSchema):
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
    ext_lst: Optional[ExtLst2] = field(
        default=None,
        metadata={
            "name": "extLst",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
        },
    )


@dataclass
class GrpSpPr(BaseSchema):
    class Meta:
        name = "grpSpPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    xfrm: Optional[Xfrm1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )


@dataclass
class NvPr(BaseSchema):
    class Meta:
        name = "nvPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    ext_lst: Optional[ExtLst1] = field(
        default=None,
        metadata={
            "name": "extLst",
            "type": "Element",
        },
    )
    ph: Optional[Ph] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SpPr:
    class Meta:
        name = "spPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    xfrm: Optional[Xfrm1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    prst_geom: Optional[PrstGeom] = field(
        default=None,
        metadata={
            "name": "prstGeom",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
        },
    )
    no_fill: Optional[object] = field(
        default=None,
        metadata={
            "name": "noFill",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
        },
    )

    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
    )


@dataclass
class TxBody:
    class Meta:
        name = "txBody"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    body_pr: Optional[BodyPr] = field(
        default=None,
        metadata={
            "name": "bodyPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
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

    attrs: dict = field(default_factory=dict, metadata={"type": "Attributes"})

    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
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
class NvGraphicFramePr(BaseSchema):
    class Meta:
        name = "nvGraphicFramePr"
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
    c_nv_graphic_frame_pr: Optional[object] = field(
        default=None,
        metadata={
            "name": "cNvGraphicFramePr",
            "type": "Element",
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
class NvGrpSpPr(BaseSchema):
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
class NvSpPr(BaseSchema):
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
class GraphicFrame(BaseSchema):
    class Meta:
        name = "graphicFrame"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    nv_graphic_frame_pr: Optional[NvGraphicFramePr] = field(
        default=None,
        metadata={
            "name": "nvGraphicFramePr",
            "type": "Element",
            "required": True,
        },
    )
    xfrm: Optional[Xfrm2] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    graphic: Optional[Graphic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )


class Style(BaseSchema):
    class Meta:
        name = "style"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
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
    sp_pr: Optional[SpPr] = field(
        default=None,
        metadata={
            "name": "spPr",
            "type": "Element",
            "required": True,
        },
    )
    any_elements: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any"
        }
    )

    # tx_body: List[Union[TxBody, Style]] = field(  # TODO
    #     default_factory=list,
    #     metadata={
    #         "type": "Elements",
    #         "choices": (
    #             {"wildcard": True, "type": str},
    #             {"name": "txBody", "type": TxBody},
    #             {"name": "style", "type": Style}
    #         )
    #     }
    # )

    tx_body: Optional[TxBody] = field(
        default=None,
        metadata={
            "name": "txBody",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SpTree(BaseSchema):
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

    shapes: List[Union[Sp]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {"wildcard": True, "type": str},
                {"name": "sp", "type": Sp}
            )
        }
    )


@dataclass
class CSld(BaseSchema):
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
class Sld(BaseSchema):
    class Meta:
        name = "sld"
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



