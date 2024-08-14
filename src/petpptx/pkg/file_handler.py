import io
import tempfile
from abc import ABC
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
from pathlib import Path
from typing import Optional, NewType
import shutil


PkgFileMap = NewType("PkgFileMap", dict[Path, bytes])


class PptxUnpackerInMemory:
    pass


class PptxUnpackerInTemp:

    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()

    def get(self):
        pass

    def cleanup(self):
        shutil.rmtree(self.temp_dir)


class PptxFileHandler:

    def __init__(self, pptx_path: Optional[Path | str] = None):
        self.pptx_path = pptx_path
        self._file_map: PkgFileMap = self.load_file_map(pptx_path=pptx_path)

    @staticmethod
    def load_file_map(pptx_path: Optional[Path | str] = None) -> PkgFileMap:
        if pptx_path is None:
            return PkgFileMap(dict())
        """Load a map of file names within the .pptx (ZIP) archive."""
        with ZipFile(pptx_path, 'r') as zip_ref:
            file_map = PkgFileMap({Path(file.filename):  zip_ref.read(file) for file in zip_ref.infolist()})
        return file_map

    def pack_pptx(self, target_file: str | Path, other_map: Optional[PkgFileMap] = None):
        if other_map is None:
            other_map = dict()
        with ZipFile(target_file,  "w", ZIP_DEFLATED) as new_zip:
            _structure_map = {**self._file_map, **other_map}
            for path, el_blob in _structure_map.items():
                new_zip.writestr(str(path), el_blob)

    def pop_file_by_path(self, file_path: str | Path) -> Optional[bytes]:
        if isinstance(file_path, str):
            file_path = Path(file_path)
        return self._file_map.pop(file_path, None)

    def get_file_by_path(self, file_path: str | Path) -> Optional[ZipInfo]:
        if isinstance(file_path, str):
            file_path = Path(file_path)
        return self._file_map.get(file_path, None)
