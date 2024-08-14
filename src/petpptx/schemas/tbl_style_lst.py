from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schemas.openxmlformats.org/drawingml/2006/main"


@dataclass
class TblStyleLst:
    class Meta:
        name = "tblStyleLst"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    def_value: Optional[str] = field(
        default="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}",
        metadata={
            "name": "def",
            "type": "Attribute",
            "required": True,
        },
    )
