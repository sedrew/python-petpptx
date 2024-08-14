from pathlib import Path

from src.petpptx.mixin_handler import MixinHandler
from src.petpptx.schemas.types import Types as XmlTypes
from src.petpptx.schemas.types import Override as XmlOverride
from src.petpptx.schemas.types import Default as XmlDefault
from src.petpptx.constants import EnumContentType
from typing import Optional


class _ContentTypesBuilder:
    _schema: XmlTypes = XmlTypes

    @staticmethod
    def create_model(model: XmlTypes) -> XmlTypes:
        model.default = [
                        XmlDefault(extension="bin", content_type=EnumContentType.PML_PRINTER_SETTINGS),
                        XmlDefault(extension="jpeg", content_type=EnumContentType.JPEG),
                        XmlDefault(extension="rels", content_type=EnumContentType.OPC_RELATIONSHIPS),
                        XmlDefault(extension="xml", content_type=EnumContentType.XML),
                        ]
        return model


class ContentTypes:
    _schema: XmlTypes = XmlTypes

    def __init__(self, part: MixinHandler, file_path: str = "[Content_Types].xml"):
        self._file_path = Path(file_path)
        self._part = part
        if self._part.has_model(file_path=file_path):
            self._model = part.deserialize_model(file_path=file_path, schema=self._schema)
        else:
            self._model = self._part.set_model(file_path=file_path,
                                               model=_ContentTypesBuilder.create_model(self._schema()))

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

    def remove_part(self, part_name: str):
        for idx, el in enumerate(self._model.override):
            if part_name == el.part_name:
                self._model.override.pop(idx)
                break
