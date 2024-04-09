from dataclasses import dataclass
from pathlib import Path
from typing import Any, TypeVar

from src.petpptx.constants import EnumNameSpace
from src.petpptx.pkg.file_handler import PkgFileMap
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer


@dataclass
class ModelObject:
    model: Any
    schema: Any


ModelMap = dict[Path, ModelObject]

T = TypeVar('T')


class PptxXmlHandler:
    serializer: XmlSerializer = XmlSerializer()

    def __init__(self):
        self._model_map: dict[Path, ModelObject] = dict()
        self._context = XmlContext()

    def add_model(self, path_name: Path | str, model, schema):
        if isinstance(path_name, str):
            path_name = Path(path_name)
        self._model_map.update({path_name: ModelObject(model=model, schema=schema)})

    def parse_xml(self, path_name,  blob: bytes, schema: T) -> T:
        parser = XmlParser(context=self._context)
        model = parser.from_bytes(blob, schema)  # TODO переделать
        self._model_map.update({path_name: ModelObject(model=model, schema=schema)})
        return model

    def get_model_by_path(self, path_name):
        return self._model_map.get(path_name, None).model

    def to_bytes(self) -> PkgFileMap:
        res = dict()
        ns_map = {None: "http://schemas.openxmlformats.org/package/2006/content-types",
                  }
        for key, el_model in self._model_map.items():
            print(el_model.model.Meta.namespace)
           # ns_map = {None: el_model.model.Meta.namespace}
            res.update({key: self.serializer.render(el_model.model)})

        print("DDDDDD")
        print(res)
        return res
