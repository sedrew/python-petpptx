from pathlib import Path

from src.petpptx.pkg import PptxFileHandler

test_pattern_pptx = 'minimal.pptx'


def test_read_pptx_from_path():
    pptx_handler = PptxFileHandler(test_pattern_pptx)
    pptx_handler.load_file_map()

    assert len(pptx_handler._file_map.keys()) > 1
    assert pptx_handler._file_map.get(Path('[Content_Types].xml'), None) is not None


def test_get_file_by_path():
    pptx_handler = PptxFileHandler(test_pattern_pptx)
    pptx_handler.load_file_map()

    assert pptx_handler.get_file_by_path('[Content_Types].xml') is not None


def test_pack_pptx():
    pptx_handler = PptxFileHandler(test_pattern_pptx)
    pptx_handler.load_file_map()
    pptx_handler.pack_pptx("empty.pptx")
    assert Path("empty.pptx").exists()






