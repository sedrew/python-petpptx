from os import PathLike
from pathlib import Path
from typing import Optional
from src.petpptx.handler.xml_handler import PptxXmlHandler
from src.petpptx.builder import create_minimal_presentation
from src.petpptx.pkg import PPTXFileHandler
from src.petpptx.coreprops import CoreProperties


class Presentation:
    """PresentationML (PML) presentation.

    Not intended to be constructed directly. Use :func:`pptx.Presentation` to open or
    create a presentation.
    """
    def __init__(self, io: Optional[str | PathLike] = None):
        self._pkg = PPTXFileHandler(pptx_path=io)
        self._pkg.load_file_map()
        self._handler: PptxXmlHandler = PptxXmlHandler()
        if io is None:
            self._handler = create_minimal_presentation()

    def save(self, file_name: str | PathLike):
        """
        Save this presentation to *file_name*, where *file_name* can be either a path
        to a file (a string) or a file-like object.
        """
        self._pkg.pack_pptx(target_file=file_name, other_map=self._handler.to_bytes())

    @property
    def core_properties(self):
        """
        Instance of |CoreProperties| holding the read/write Dublin Core
        document properties for this presentation.
        """
        blob = self._pkg.pop_file_by_path("docProps/core.xml")
        self._handler.parse_xml(path_name=Path("docProps/core.xml"), blob=blob, schema=CoreProperties._schema)
        return CoreProperties(path_name="docProps/core.xml",
                              model=self._handler.get_model_by_path(Path("docProps/core.xml")))

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

    def slides(self):
        """
        |Slides| object containing the slides in this presentation.
        """
        pass