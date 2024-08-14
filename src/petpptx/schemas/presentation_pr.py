from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class DefaultImageDpi:
    class Meta:
        name = "defaultImageDpi"
        namespace = "http://schemas.microsoft.com/office/powerpoint/2010/main"

    val: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DiscardImageEditData:
    class Meta:
        name = "discardImageEditData"
        namespace = "http://schemas.microsoft.com/office/powerpoint/2010/main"

    val: Optional[int] = field(
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
    default_image_dpi: Optional[DefaultImageDpi] = field(
        default=None,
        metadata={
            "name": "defaultImageDpi",
            "type": "Element",
            "namespace": "http://schemas.microsoft.com/office/powerpoint/2010/main",
        },
    )
    discard_image_edit_data: Optional[DiscardImageEditData] = field(
        default=None,
        metadata={
            "name": "discardImageEditData",
            "type": "Element",
            "namespace": "http://schemas.microsoft.com/office/powerpoint/2010/main",
        },
    )


@dataclass
class ExtLst:
    class Meta:
        name = "extLst"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    ext: List[Ext] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class PresentationPr:
    class Meta:
        name = "presentationPr"
        namespace = (
            "http://schemas.openxmlformats.org/presentationml/2006/main"
        )

    ext_lst: Optional[ExtLst] = field(
        default=ExtLst(ext=list([Ext(uri="{E76CE94A-603C-4142-B9EB-6D1370010A27}",
                                     default_image_dpi=DefaultImageDpi(val=220)),
                                Ext(uri="{D31A062A-798A-4329-ABDD-BBA856620510}",
                                    discard_image_edit_data=DiscardImageEditData(val=0))])),
        metadata={
            "name": "extLst",
            "type": "Element",
            "required": True,
        },
    )
