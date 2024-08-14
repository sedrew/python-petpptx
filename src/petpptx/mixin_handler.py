from os import PathLike
from pathlib import Path
from typing import TypeVar, Optional

from src.petpptx.handler.xml_handler import PptxXmlHandler
from src.petpptx.pkg import PptxFileHandler

T = TypeVar('T')


class MixinHandler:

    def __init__(self, handler: PptxXmlHandler, pkg: PptxFileHandler):
        self._handler: PptxXmlHandler = handler
        self._pkg: PptxFileHandler = pkg

    def has_pkg_file(self, file_path) -> bool:
        if self._pkg.get_file_by_path(file_path) is None:
            return False
        return True

    def has_model(self, file_path) -> bool:
        if self._handler.get_model_by_path(file_path=file_path) is None:
            return False
        return True

    def deserialize_model(self, file_path: str, schema: T, ns_map: Optional[dict] = None) -> T | None:
        blob = self._pkg.pop_file_by_path(Path(file_path))
        if blob is not None:
            return None

        return self._handler.add_xml_model(file_path=file_path,
                                           model=schema(),
                                           schema=schema,
                                           ns_map=ns_map)

    def get_model(self, file_path: str) -> Optional[T]:
        model = self._handler.get_model_by_path(file_path=file_path)
        return model

    def set_model(self, file_path: str, model: T,  ns_map: Optional[dict] = None) -> T:
        return self._handler.add_xml_model(file_path=file_path,
                                           model=model,
                                           schema=model,
                                           ns_map=ns_map)

    def remove_file_or_model(self, file_path):
        self._pkg.pop_file_by_path(file_path)
        self._handler.pop_model_by_path(file_path)

    def save(self, file_name: str | PathLike):
        self._pkg.pack_pptx(target_file=file_name, other_map=self._handler.to_bytes())


