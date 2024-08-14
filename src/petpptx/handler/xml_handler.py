from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Any, TypeVar, Optional, Union

from src.petpptx.constants import EnumNameSpace
from src.petpptx.pkg.file_handler import PkgFileMap
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers import PycodeSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers.lxml import LxmlEventWriter

T = TypeVar('T')


@dataclass
class ModelBlob:
    file_path: Path
    blob: bytes
    file_type: str


@dataclass
class ModelXml:
    file_path: Path
    model: Optional[T]
    schema: Any
    ns_map: Optional[dict] = None
    blob: Any = None


ModelMap = dict[Path, Union[ModelXml, ModelBlob]]

parser_config = ParserConfig(fail_on_unknown_properties=False)
config = SerializerConfig(indent="  ")


class PptxXmlHandler:

    def __init__(self):
        self._model_map: ModelMap = dict()
        self._context = XmlContext()
        self.serializer: XmlSerializer = XmlSerializer(context=self._context, config=config, writer=LxmlEventWriter)
        # XmlSerializer(context=self._context, config=config)

    def add_xml_model(self, file_path, model, schema, ns_map):
        xml_model = ModelXml(file_path=Path(file_path), model=model, schema=schema, ns_map=ns_map)
        self._model_map.update({xml_model.file_path: xml_model})
        return xml_model.model

    def pop_model_by_path(self, file_path):
        self._model_map.pop(Path(file_path), None)

    def parse_xml(self, file_path,  blob: bytes | StringIO, schema: T, ns_map: Optional[dict] = None) -> T:
        if isinstance(file_path, str):
            file_path = Path(file_path)
        parser = XmlParser(context=self._context, config=parser_config)
        model = parser.from_bytes(source=blob, clazz=schema, ns_map=ns_map)  # TODO переделать
        model_xml = ModelXml(file_path=file_path, model=model, schema=schema, ns_map=ns_map, blob=blob)
        self._model_map.update({file_path: model_xml})
        return model

    def get_model_by_path(self, file_path) -> ModelXml | ModelBlob | None:
        if self._model_map.get(file_path, None) is None:
            return None
        return self._model_map.get(file_path, None).model

    def to_bytes(self) -> PkgFileMap:
        res = PkgFileMap(dict())
        for key, el_model in self._model_map.items():
            res.update({key: self.serializer.render(el_model.model, ns_map=el_model.ns_map)})

        return res
