from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schemas.openxmlformats.org/drawingml/2006/main"


@dataclass
class TblStyleLst:
    class Meta:
        name = "tblStyleLst"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    def_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "def",
            "type": "Attribute",
            "required": True,
        },
    )
