from pathlib import Path

from src.petpptx.schemas.types import Types as XmlTypes
from src.petpptx.schemas.types import Override as XmlOverride
from src.petpptx.schemas.types import Default as XmlDefault
from src.petpptx.constants import EnumContentType
from typing import Optional


class _ContentTypesBuilder:
    _schema: XmlTypes = XmlTypes

    @staticmethod
    def get_model():
        model = XmlTypes(default=[
                XmlDefault(extension="bin", content_type=EnumContentType.PML_PRINTER_SETTINGS),
                XmlDefault(extension="jpeg", content_type=EnumContentType.JPEG),
                XmlDefault(extension="rels", content_type=EnumContentType.OPC_RELATIONSHIPS),
                XmlDefault(extension="xml", content_type=EnumContentType.XML),
                ])
        return model


class ContentTypes:
    _schema: XmlTypes = XmlTypes

    def __init__(self, path_name: str = "[Content_Types].xml", model: Optional[XmlTypes] = None):
        self._path_name = Path(path_name)
        self._model = model
        if self._model is None:
            self._model = _ContentTypesBuilder.get_model()

    def get_override_by_part_name(self, part_name: str) -> Optional[XmlOverride]:
        for el in self._model.override:
            if el.part_name == part_name:
                return el
        return None

    def get_model(self) -> XmlTypes:
        return self._model

    def add_type(self, part_name: str, content_type):
        override = XmlOverride(part_name=part_name, content_type=content_type)
        self._model.override.append(override)

    def remove_type(self, target):
        ...
