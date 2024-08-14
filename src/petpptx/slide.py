from pathlib import Path
from typing import Iterator

from src.petpptx.contet_type import ContentTypes
from src.petpptx.handler.xml_handler import PptxXmlHandler, ModelXml
from src.petpptx.mixin_handler import MixinHandler
from src.petpptx.pkg import PptxFileHandler
from src.petpptx.relationship import Relationships
from src.petpptx.schemas.sld import Sld as XmlSlide
from src.petpptx.schemas.sld_layout import SldLayout as XmlSlideLayout
from src.petpptx.schemas.sld_master import SldMaster as XmlSlideMaster
from src.petpptx.schemas.presentation import Presentation as XmlPresentation
from src.petpptx.schemas.theme import Theme as XmlTheme


class _ThemeBuilder:
    @staticmethod
    def create_model() -> XmlTheme:
        model = XmlTheme()
        return model


class Theme:

    _schema = XmlTheme

    def __init__(self, part: MixinHandler, file_path="ppt/theme/theme1.xml"):
        self._part = part

        if self._part.has_model(file_path=file_path):
            self._model = part.deserialize_model(file_path=file_path, schema=self._schema)
        else:
            self._model = self._part.set_model(model=_ThemeBuilder.create_model(),
                                               file_path=file_path)


class _SlideMasterBuilder:
    @staticmethod
    def create_model(part: MixinHandler) -> XmlSlideMaster:
        model = XmlSlideMaster()

        _rels = Relationships(file_path="ppt/slideMasters/_rels/slideMaster1.xml.rels", part=part)
        _rels.add_target(target="ppt/theme/theme1.xml")

        return model


class SlideMaster:
    _schema = XmlSlideMaster

    def __init__(self, part: MixinHandler, file_path="ppt/slideMasters/slideMaster1.xml"):
        self._part = part

        if self._part.has_model(file_path=file_path):
            self._model = part.deserialize_model(file_path=file_path, schema=self._schema)
        else:
            self._model = self._part.set_model(model=_SlideMasterBuilder.create_model(part=self._part),
                                               file_path=file_path)


class _SlideLayoutBuilder:

    @staticmethod
    def create_model(part: MixinHandler) -> XmlSlideLayout:
        model = XmlSlideLayout()

        _rels = Relationships(file_path="ppt/slideLayouts/_rels/slideLayout1.xml.rels", part=part)
        _rels.add_target(target="ppt/slideMasters/slideMaster1.xml")

        return model


class SlideLayout:
    _schema: XmlSlide = XmlSlideLayout

    def __init__(self, part: MixinHandler, file_path="ppt/slideLayouts/slideLayout1.xml"):
        self._part = part

        if self._part.has_model(file_path=file_path):
            self._model = part.deserialize_model(file_path=file_path, schema=self._schema)
        else:
            self._model = self._part.set_model(model=_SlideLayoutBuilder.create_model(part=self._part),
                                               file_path=file_path)


class SlideLayouts:
    pass


class _SlideBuilder:
    @staticmethod
    def create_model() -> XmlSlide:
        model = XmlSlide()
        return model


class Slide:
    _schema: XmlSlide = XmlSlide
    _ns_map = {
        "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
        "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
        "p": "http://schemas.openxmlformats.org/presentationml/2006/main"
    }

    def __init__(self, part: MixinHandler, file_path):
        self._part = part

        if self._part.has_model(file_path=file_path):
            self._model = part.deserialize_model(file_path=file_path, schema=self._schema, ns_map=self._ns_map)
        else:
            self._model = self._part.set_model(file_path=file_path, model=_SlideBuilder.create_model())

    @property
    def name(self):
        """
        String representing the internal name of this slide. Returns an empty
        string (`''`) if no name is assigned. Assigning an empty string or
        |None| to this property causes any name to be removed.
        """
        return self._model.c_sld.name

    @name.setter
    def name(self, value):
        new_value = "" if value is None else value
        # self._element.cSld.name = new_value


class Slides:
    """
    Sequence of slides belonging to an instance of |Presentation|, having
    list semantics for access to individual slides. Supports indexed access,
    len(), and iteration.
    """

    def __init__(self, part: MixinHandler, prs_model: XmlPresentation, prs_rels: Relationships):
        self._part = part
        self._prs_model = prs_model
        self._prs_rels = prs_rels

    def __getitem__(self, idx) -> Slide:
        """
        Provide indexed access, (e.g. 'slides[0]').
        """
        if self._prs_model.sld_id_lst.sld_id is None:
            raise Exception("Id dont found")
        slide_path = f"ppt/{self._prs_rels.get_model_by_rid(rid=self._prs_model.sld_id_lst.sld_id[idx].rid).target}"
        if not self._part.has_pkg_file(slide_path):
            raise Exception("Slide dont found")
        return Slide(part=self._part, file_path=slide_path)

    def __iter__(self) -> Iterator[Slide]:
        """
        Support iteration (e.g. 'for slide in slides:').
        """
        count = self.__len__()
        for idx in range(count):
            yield self.__getitem__(idx)

    def __len__(self):
        """
        Support len() built-in function (e.g. 'len(slides) == 4').
        """
        return len(self._prs_model.sld_id_lst.sld_id)

    def remove(self, idx):
        content_type = ContentTypes(part=self._part)
        if idx > self.__len__():
            raise Exception("Idx out of range")

        slide_path = self._prs_rels.get_model_by_rid(rid=self._prs_model.sld_id_lst.sld_id.pop(idx).rid).target

        self._part.remove_file_or_model(file_path=f"ppt/{slide_path}")
        self._part.remove_file_or_model(file_path=f"ppt/slides/_rels/{Path(slide_path).name}.rels")
        self._prs_rels.remove_target(target=slide_path)
        content_type.remove_part(part_name=f"/ppt/{slide_path}")
