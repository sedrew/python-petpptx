import io
from abc import ABC
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
from pathlib import Path
from typing import Optional, NewType

PkgFileMap = NewType("PkgFileMap", dict[Path, bytes])


class StructuredData(ABC):

    def to_bytes(self) -> dict[Path, bytes | str]:
        ...


class PPTXFileHandler:

    def __init__(self, pptx_path=None, structure=StructuredData()):
        self.pptx_path = pptx_path
        self._file_map: PkgFileMap = PkgFileMap(dict())

    def load_file_map(self) -> dict[Path, ZipFile]:
        """Load a map of file names within the .pptx (ZIP) archive."""
        with ZipFile(self.pptx_path, 'r') as zip_ref:
            self._file_map = {Path(file.filename):  zip_ref.read(file) for file in zip_ref.infolist()}
        return self._file_map

    def pack_pptx(self, target_file: str | Path, other_map: Optional[PkgFileMap] = None):
        if other_map is None:
            other_map = dict()
        with ZipFile(target_file,  "w", ZIP_DEFLATED) as new_zip:
            _structure_map = {**self._file_map, **other_map}
            for path, el_blob in _structure_map.items():
                new_zip.writestr(str(path), el_blob)

    def pop_file_by_path(self, file_path: str | Path) -> Optional[ZipInfo]:
        if isinstance(file_path, str):
            file_path = Path(file_path)
        return self._file_map.pop(file_path, None)

    def get_file_by_path(self, file_path: str | Path) -> Optional[ZipInfo]:
        if isinstance(file_path, str):
            file_path = Path(file_path)
        return self._file_map.get(file_path, None)
