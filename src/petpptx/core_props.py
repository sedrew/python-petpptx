from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDateTime

from src.petpptx.mixin_handler import MixinHandler
from src.petpptx.schemas.core_properties import CoreProperties as SchemaProperties
from src.petpptx.schemas.core_properties import Created as SchemaCreated
from src.petpptx.schemas.core_properties import Modified as SchemaModified
from src.petpptx.schemas.presentation import Presentation as XmlPresentation


class _CorePropertiesBuilder:
    _schema: SchemaProperties = SchemaProperties

    @staticmethod
    def create_model(model: SchemaProperties):
        created = SchemaCreated(type_value=QName("dcterms:W3CDTF"),
                                value=XmlDateTime(year=2024,
                                                  month=4,
                                                  day=4,
                                                  hour=4,
                                                  minute=4,
                                                  second=4))
        modified = SchemaModified(type_value=QName("dcterms:W3CDTF"),
                                  value=XmlDateTime(year=2024,
                                                    month=4,
                                                    day=4,
                                                    hour=4,
                                                    minute=5,
                                                    second=5))
        model.title = "Presentation"
        model.creator = "petpptx"
        model.last_modified_by = "petpptx"
        model.revision = 1
        model.created = created
        model.modified = modified
        return model


class CoreProperties:
    _file_path = "/docProps/core.xml"
    _schema: SchemaProperties = SchemaProperties
    _ns_map: dict = {}

    def __init__(self, part: MixinHandler):
        self._part = part
        if self._part.has_model(file_path=self._file_path):
            self._model = part.deserialize_model(file_path=self._file_path, schema=self._schema)
        else:
            self._model = self._part.set_model(file_path=self._file_path,
                                               model=_CorePropertiesBuilder.create_model(model=self._schema()))

    def get_model(self):
        return self._model

    @property
    def title(self):
        return self._model.title

    @title.setter
    def title(self, title: str):
        self._model.title = title

    @property
    def creator(self):
        return self._model.creator

    @creator.setter
    def creator(self, creator: str):
        self._model.creator = creator
