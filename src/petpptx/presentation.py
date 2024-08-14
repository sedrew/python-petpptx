from functools import cached_property
from os import PathLike
from typing import Optional

from src.petpptx.app_props import AppProperties
from src.petpptx.constants import EnumRelationshipType
from src.petpptx.contet_type import ContentTypes
from src.petpptx.handler.xml_handler import PptxXmlHandler
from src.petpptx.mixin_handler import MixinHandler
from src.petpptx.pkg import PptxFileHandler
from src.petpptx.core_props import CoreProperties
from src.petpptx.relationship import Relationships
from src.petpptx.slide import Slides, SlideMaster, SlideLayout, Theme
from src.petpptx.schemas.presentation import Presentation as XmlPresentation
from src.petpptx.schemas.view_pr import ViewPr as XmlViewProp
from src.petpptx.schemas.presentation_pr import PresentationPr as XmlPresentationProp, Ext
from src.petpptx.schemas.tbl_style_lst import TblStyleLst as XmlTableStyle


class _PresentationBuilder:

    @staticmethod
    def create_model(part: MixinHandler):
        model = XmlPresentation()

        content_types = ContentTypes(part=part)

        _rels = Relationships(file_path="/_rels/.rels", part=part)
        _rels.add_target(type_value=EnumRelationshipType.OFFICE_DOCUMENT, target="/ppt/presentation.xml")
        _rels.add_target(type_value=EnumRelationshipType.CORE_PROPERTIES, target="/docProps/core.xml")
        _rels.add_target(type_value=EnumRelationshipType.EXTENDED_PROPERTIES, target="/docProps/app.xml")
        _rels.add_target(type_value=EnumRelationshipType.THUMBNAIL, target="/docProps/thumbnail.jpeg")

        core_props = CoreProperties(part=part)
        app_props = AppProperties("/docProps/app.xml")

        part.set_model(file_path=core_props._file_path, model=core_props.get_model())
        part.set_model(file_path=app_props._file_path, model=app_props.get_model())
        part.set_model(file_path=content_types._file_path, model=content_types.get_model())
        part.set_model(file_path=_rels._file_path, model=_rels.get_model())

        SlideMaster(part=part)
        SlideLayout(part=part)
        Theme(part=part)

        ns_map = {
            "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
            "p": "http://schemas.openxmlformats.org/presentationml/2006/main"
        }
        part.set_model(file_path="ppt/viewProps", model=XmlViewProp(), ns_map=ns_map)
        part.set_model(file_path="ppt/presProps", model=XmlPresentationProp(), ns_map=ns_map)
        part.set_model(file_path="ppt/tableStyles", model=XmlTableStyle)

        return model


class Presentation:
    """PresentationML (PML) presentation.

    Not intended to be constructed directly. Use :func:`pptx.Presentation` to open or
    create a presentation.
    """

    _schema: XmlPresentation = XmlPresentation
    _file_path = "/ppt/presentation.xml"

    def __init__(self, io: Optional[str | PathLike] = None):
        self._part = MixinHandler(pkg=PptxFileHandler(pptx_path=io), handler=PptxXmlHandler())

        if self._part.has_model(file_path=self._file_path):
            self._model = self._part.deserialize_model(file_path=self._file_path, schema=self._schema)
        else:
            self._model = self._part.set_model(file_path=self._file_path,
                                               model=_PresentationBuilder.create_model(part=self._part))

        self._rels = Relationships(file_path="ppt/_rels/presentation.xml.rels", part=self._part)

    def save(self, file_name: str | PathLike):
        """
        Save this presentation to *file_name*, where *file_name* can be either a path
        to a file (a string) or a file-like object.
        """
        self._part.save(file_name=file_name)

    @property
    def core_properties(self):
        """
        Instance of |CoreProperties| holding the read/write Dublin Core
        document properties for this presentation.
        """
        return CoreProperties(part=self._part)

    @property
    def notes_master(self):
        """
        Instance of |NotesMaster| for this presentation. If the presentation
        does not have a notes master, one is created from a default template
        and returned. The same single instance is returned on each call.
        """
        return

    @property
    def slide_height(self):
        """
        Height of slides in this presentation, in English Metric Units (EMU).
        Returns |None| if no slide width is defined. Read/write.
        """
        pass

    @slide_height.setter
    def slide_height(self, height):
        pass

    @property
    def slide_layouts(self):
        """
        Sequence of |SlideLayout| instances belonging to the first
        |SlideMaster| of this presentation. A presentation can have more than
        one slide master and each master will have its own set of layouts.
        This property is a convenience for the common case where the
        presentation has only a single slide master.
        """
        return

    @property
    def slide_master(self):
        """
        First |SlideMaster| object belonging to this presentation. Typically,
        presentations have only a single slide master. This property provides
        simpler access in that common case.
        """
        return

    def slide_masters(self):
        """
        Sequence of |SlideMaster| objects belonging to this presentation
        """
        return

    @property
    def slide_width(self):
        """
        Width of slides in this presentation, in English Metric Units (EMU).
        Returns |None| if no slide width is defined. Read/write.
        """

    @slide_width.setter
    def slide_width(self, width):
        pass

    @cached_property
    def slides(self):
        """
        |Slides| object containing the slides in this presentation.
        """
        return Slides(part=self._part, prs_model=self._model, prs_rels=self._rels)
