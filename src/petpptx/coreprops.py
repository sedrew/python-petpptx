from decimal import Decimal
from pathlib import Path
from typing import Optional
from xml.etree.ElementTree import QName
from xsdata.models.datatype import XmlDateTime

from src.petpptx.schemas.core_properties import CoreProperties as SchemaProperties
from src.petpptx.schemas.core_properties import Created as SchemaCreated
from src.petpptx.schemas.core_properties import Modified as SchemaModified


class _CorePropertiesBuilder:
    _schema: SchemaProperties = SchemaProperties

    @staticmethod
    def get_model():
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
        model = SchemaProperties(title="Presentation",
                                 creator="petpptx",
                                 last_modified_by="petpptx",
                                 revision=1,
                                 created=created,
                                 modified=modified
                                 )
        return model


class CoreProperties:
    _schema: SchemaProperties = SchemaProperties

    def __init__(self, path_name: str, model: Optional[SchemaProperties] = None):
        self._path_name = Path(path_name)
        self._model = model
        if self._model is None:
            self._model = _CorePropertiesBuilder.get_model()

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
