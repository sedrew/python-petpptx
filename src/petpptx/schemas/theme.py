from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://schemas.openxmlformats.org/drawingml/2006/main"


@dataclass
class Alpha:
    class Meta:
        name = "alpha"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    val: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class BevelT:
    class Meta:
        name = "bevelT"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    w: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    h: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Cs:
    class Meta:
        name = "cs"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    typeface: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Ea:
    class Meta:
        name = "ea"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    typeface: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class FillToRect:
    class Meta:
        name = "fillToRect"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    l: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    t: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    r: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Font:
    class Meta:
        name = "font"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    script: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    typeface: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Latin:
    class Meta:
        name = "latin"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    typeface: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Lin:
    class Meta:
        name = "lin"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    ang: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    scaled: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrstDash:
    class Meta:
        name = "prstDash"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Rot:
    class Meta:
        name = "rot"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    lat: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    lon: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    rev: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SatMod:
    class Meta:
        name = "satMod"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    val: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Shade:
    class Meta:
        name = "shade"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    val: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SysClr:
    class Meta:
        name = "sysClr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    last_clr: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastClr",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Tint:
    class Meta:
        name = "tint"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    val: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Camera:
    class Meta:
        name = "camera"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    prst: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    rot: Optional[Rot] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Dk1:
    class Meta:
        name = "dk1"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    sys_clr: Optional[SysClr] = field(
        default=None,
        metadata={
            "name": "sysClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LightRig:
    class Meta:
        name = "lightRig"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    rig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    dir: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    rot: Optional[Rot] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lt1:
    class Meta:
        name = "lt1"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    sys_clr: Optional[SysClr] = field(
        default=None,
        metadata={
            "name": "sysClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MajorFont:
    class Meta:
        name = "majorFont"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    latin: Optional[Latin] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ea: Optional[Ea] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    cs: Optional[Cs] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    font: List[Font] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class MinorFont:
    class Meta:
        name = "minorFont"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    latin: Optional[Latin] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ea: Optional[Ea] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    cs: Optional[Cs] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    font: List[Font] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Path:
    class Meta:
        name = "path"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    fill_to_rect: Optional[FillToRect] = field(
        default=None,
        metadata={
            "name": "fillToRect",
            "type": "Element",
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
    tint: Optional[Tint] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    shade: Optional[Shade] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sat_mod: Optional[SatMod] = field(
        default=None,
        metadata={
            "name": "satMod",
            "type": "Element",
        },
    )


@dataclass
class Sp3D:
    class Meta:
        name = "sp3d"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    bevel_t: Optional[BevelT] = field(
        default=None,
        metadata={
            "name": "bevelT",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SrgbClr:
    class Meta:
        name = "srgbClr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    val: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    alpha: Optional[Alpha] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Accent1:
    class Meta:
        name = "accent1"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Accent2:
    class Meta:
        name = "accent2"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Accent3:
    class Meta:
        name = "accent3"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Accent4:
    class Meta:
        name = "accent4"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Accent5:
    class Meta:
        name = "accent5"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Accent6:
    class Meta:
        name = "accent6"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Dk2:
    class Meta:
        name = "dk2"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FolHlink:
    class Meta:
        name = "folHlink"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FontScheme:
    class Meta:
        name = "fontScheme"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    major_font: Optional[MajorFont] = field(
        default=None,
        metadata={
            "name": "majorFont",
            "type": "Element",
            "required": True,
        },
    )
    minor_font: Optional[MinorFont] = field(
        default=None,
        metadata={
            "name": "minorFont",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Gs:
    class Meta:
        name = "gs"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    pos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    scheme_clr: Optional[SchemeClr] = field(
        default=None,
        metadata={
            "name": "schemeClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Hlink:
    class Meta:
        name = "hlink"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lt2:
    class Meta:
        name = "lt2"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class OuterShdw:
    class Meta:
        name = "outerShdw"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    blur_rad: Optional[int] = field(
        default=None,
        metadata={
            "name": "blurRad",
            "type": "Attribute",
            "required": True,
        },
    )
    dist: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    dir: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    rot_with_shape: Optional[int] = field(
        default=None,
        metadata={
            "name": "rotWithShape",
            "type": "Attribute",
            "required": True,
        },
    )
    srgb_clr: Optional[SrgbClr] = field(
        default=None,
        metadata={
            "name": "srgbClr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Scene3D:
    class Meta:
        name = "scene3d"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    camera: Optional[Camera] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    light_rig: Optional[LightRig] = field(
        default=None,
        metadata={
            "name": "lightRig",
            "type": "Element",
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
class ClrScheme:
    class Meta:
        name = "clrScheme"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    dk1: Optional[Dk1] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lt1: Optional[Lt1] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    dk2: Optional[Dk2] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lt2: Optional[Lt2] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    accent1: Optional[Accent1] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    accent2: Optional[Accent2] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    accent3: Optional[Accent3] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    accent4: Optional[Accent4] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    accent5: Optional[Accent5] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    accent6: Optional[Accent6] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    hlink: Optional[Hlink] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    fol_hlink: Optional[FolHlink] = field(
        default=None,
        metadata={
            "name": "folHlink",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EffectLst:
    class Meta:
        name = "effectLst"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    outer_shdw: Optional[OuterShdw] = field(
        default=None,
        metadata={
            "name": "outerShdw",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GsLst:
    class Meta:
        name = "gsLst"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    gs: List[Gs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Ln:
    class Meta:
        name = "ln"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    w: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    cap: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    cmpd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    algn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    solid_fill: Optional[SolidFill] = field(
        default=None,
        metadata={
            "name": "solidFill",
            "type": "Element",
            "required": True,
        },
    )
    prst_dash: Optional[PrstDash] = field(
        default=None,
        metadata={
            "name": "prstDash",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EffectStyle:
    class Meta:
        name = "effectStyle"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    effect_lst: Optional[EffectLst] = field(
        default=None,
        metadata={
            "name": "effectLst",
            "type": "Element",
            "required": True,
        },
    )
    scene3d: Optional[Scene3D] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sp3d: Optional[Sp3D] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GradFill:
    class Meta:
        name = "gradFill"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    rot_with_shape: Optional[int] = field(
        default=None,
        metadata={
            "name": "rotWithShape",
            "type": "Attribute",
            "required": True,
        },
    )
    gs_lst: Optional[GsLst] = field(
        default=None,
        metadata={
            "name": "gsLst",
            "type": "Element",
            "required": True,
        },
    )
    path: Optional[Path] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lin: Optional[Lin] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class LnStyleLst:
    class Meta:
        name = "lnStyleLst"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    ln: List[Ln] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class BgFillStyleLst:
    class Meta:
        name = "bgFillStyleLst"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    solid_fill: Optional[SolidFill] = field(
        default=None,
        metadata={
            "name": "solidFill",
            "type": "Element",
            "required": True,
        },
    )
    grad_fill: List[GradFill] = field(
        default_factory=list,
        metadata={
            "name": "gradFill",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class EffectStyleLst:
    class Meta:
        name = "effectStyleLst"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    effect_style: List[EffectStyle] = field(
        default_factory=list,
        metadata={
            "name": "effectStyle",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class FillStyleLst:
    class Meta:
        name = "fillStyleLst"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    solid_fill: Optional[SolidFill] = field(
        default=None,
        metadata={
            "name": "solidFill",
            "type": "Element",
            "required": True,
        },
    )
    grad_fill: List[GradFill] = field(
        default_factory=list,
        metadata={
            "name": "gradFill",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class FmtScheme:
    class Meta:
        name = "fmtScheme"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    fill_style_lst: Optional[FillStyleLst] = field(
        default=None,
        metadata={
            "name": "fillStyleLst",
            "type": "Element",
            "required": True,
        },
    )
    ln_style_lst: Optional[LnStyleLst] = field(
        default=None,
        metadata={
            "name": "lnStyleLst",
            "type": "Element",
            "required": True,
        },
    )
    effect_style_lst: Optional[EffectStyleLst] = field(
        default=None,
        metadata={
            "name": "effectStyleLst",
            "type": "Element",
            "required": True,
        },
    )
    bg_fill_style_lst: Optional[BgFillStyleLst] = field(
        default=None,
        metadata={
            "name": "bgFillStyleLst",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ThemeElements:
    class Meta:
        name = "themeElements"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    clr_scheme: Optional[ClrScheme] = field(
        default=None,
        metadata={
            "name": "clrScheme",
            "type": "Element",
            "required": True,
        },
    )
    font_scheme: Optional[FontScheme] = field(
        default=None,
        metadata={
            "name": "fontScheme",
            "type": "Element",
            "required": True,
        },
    )
    fmt_scheme: Optional[FmtScheme] = field(
        default=None,
        metadata={
            "name": "fmtScheme",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Theme:
    class Meta:
        name = "theme"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    theme_elements: Optional[ThemeElements] = field(
        default=None,
        metadata={
            "name": "themeElements",
            "type": "Element",
            "required": True,
        },
    )
    object_defaults: Optional[object] = field(
        default=None,
        metadata={
            "name": "objectDefaults",
            "type": "Element",
        },
    )
    extra_clr_scheme_lst: Optional[object] = field(
        default=None,
        metadata={
            "name": "extraClrSchemeLst",
            "type": "Element",
        },
    )
