from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Cs:
    class Meta:
        name = "cs"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    typeface: Optional[str] = field(
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
class NotesSz:
    class Meta:
        name = "notesSz"
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
class SldMasterId:
    class Meta:
        name = "sldMasterId"
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
    schemas_openxmlformats_org_office_document_2006_relationships_id: Optional[
        str
    ] = field(
        default=None,
        metadata={
            "name": "id",
            "type": "Attribute",
            "namespace": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
            "required": True,
        },
    )


@dataclass
class SldSz:
    class Meta:
        name = "sldSz"
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
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
class SldMasterIdLst:
    class Meta:
        name = "sldMasterIdLst"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    sld_master_id: Optional[SldMasterId] = field(
        default=None,
        metadata={
            "name": "sldMasterId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DefRpr:
    class Meta:
        name = "defRPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    sz: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    kern: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    solid_fill: Optional[SolidFill] = field(
        default=None,
        metadata={
            "name": "solidFill",
            "type": "Element",
        },
    )
    latin: Optional[Latin] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ea: Optional[Ea] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cs: Optional[Cs] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DefPpr:
    class Meta:
        name = "defPPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lvl1PPr:
    class Meta:
        name = "lvl1pPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
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
    def_tab_sz: Optional[int] = field(
        default=None,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        },
    )
    rtl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ea_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    latin_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    hanging_punct: Optional[int] = field(
        default=None,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        },
    )
    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lvl2PPr:
    class Meta:
        name = "lvl2pPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
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
    def_tab_sz: Optional[int] = field(
        default=None,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        },
    )
    rtl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ea_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    latin_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    hanging_punct: Optional[int] = field(
        default=None,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        },
    )
    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lvl3PPr:
    class Meta:
        name = "lvl3pPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
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
    def_tab_sz: Optional[int] = field(
        default=None,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        },
    )
    rtl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ea_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    latin_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    hanging_punct: Optional[int] = field(
        default=None,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        },
    )
    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lvl4PPr:
    class Meta:
        name = "lvl4pPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
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
    def_tab_sz: Optional[int] = field(
        default=None,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        },
    )
    rtl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ea_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    latin_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    hanging_punct: Optional[int] = field(
        default=None,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        },
    )
    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lvl5PPr:
    class Meta:
        name = "lvl5pPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
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
    def_tab_sz: Optional[int] = field(
        default=None,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        },
    )
    rtl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ea_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    latin_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    hanging_punct: Optional[int] = field(
        default=None,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        },
    )
    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lvl6PPr:
    class Meta:
        name = "lvl6pPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
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
    def_tab_sz: Optional[int] = field(
        default=None,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        },
    )
    rtl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ea_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    latin_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    hanging_punct: Optional[int] = field(
        default=None,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        },
    )
    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lvl7PPr:
    class Meta:
        name = "lvl7pPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
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
    def_tab_sz: Optional[int] = field(
        default=None,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        },
    )
    rtl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ea_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    latin_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    hanging_punct: Optional[int] = field(
        default=None,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        },
    )
    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lvl8PPr:
    class Meta:
        name = "lvl8pPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
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
    def_tab_sz: Optional[int] = field(
        default=None,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        },
    )
    rtl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ea_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    latin_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    hanging_punct: Optional[int] = field(
        default=None,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        },
    )
    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Lvl9PPr:
    class Meta:
        name = "lvl9pPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
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
    def_tab_sz: Optional[int] = field(
        default=None,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        },
    )
    rtl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ea_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    latin_ln_brk: Optional[int] = field(
        default=None,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        },
    )
    hanging_punct: Optional[int] = field(
        default=None,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        },
    )
    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DefaultTextStyle:
    class Meta:
        name = "defaultTextStyle"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    def_ppr: Optional[DefPpr] = field(
        default=None,
        metadata={
            "name": "defPPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    lvl1p_pr: Optional[Lvl1PPr] = field(
        default=None,
        metadata={
            "name": "lvl1pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    lvl2p_pr: Optional[Lvl2PPr] = field(
        default=None,
        metadata={
            "name": "lvl2pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    lvl3p_pr: Optional[Lvl3PPr] = field(
        default=None,
        metadata={
            "name": "lvl3pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    lvl4p_pr: Optional[Lvl4PPr] = field(
        default=None,
        metadata={
            "name": "lvl4pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    lvl5p_pr: Optional[Lvl5PPr] = field(
        default=None,
        metadata={
            "name": "lvl5pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    lvl6p_pr: Optional[Lvl6PPr] = field(
        default=None,
        metadata={
            "name": "lvl6pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    lvl7p_pr: Optional[Lvl7PPr] = field(
        default=None,
        metadata={
            "name": "lvl7pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    lvl8p_pr: Optional[Lvl8PPr] = field(
        default=None,
        metadata={
            "name": "lvl8pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )
    lvl9p_pr: Optional[Lvl9PPr] = field(
        default=None,
        metadata={
            "name": "lvl9pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        },
    )


@dataclass
class Presentation:
    class Meta:
        name = "presentation"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    save_subset_fonts: Optional[int] = field(
        default=None,
        metadata={
            "name": "saveSubsetFonts",
            "type": "Attribute",
            "required": True,
        },
    )
    sld_master_id_lst: Optional[SldMasterIdLst] = field(
        default=None,
        metadata={
            "name": "sldMasterIdLst",
            "type": "Element",
            "required": True,
        },
    )
    sld_sz: Optional[SldSz] = field(
        default=None,
        metadata={
            "name": "sldSz",
            "type": "Element",
            "required": True,
        },
    )
    notes_sz: Optional[NotesSz] = field(
        default=None,
        metadata={
            "name": "notesSz",
            "type": "Element",
            "required": True,
        },
    )
    default_text_style: Optional[DefaultTextStyle] = field(
        default=None,
        metadata={
            "name": "defaultTextStyle",
            "type": "Element",
            "required": True,
        },
    )
