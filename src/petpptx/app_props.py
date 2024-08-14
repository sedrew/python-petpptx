from decimal import Decimal
from pathlib import Path
from typing import Optional

from src.petpptx.schemas.properties import Properties as SchemaProperties
from src.petpptx.schemas.properties import HeadingPairs as SchemaHeadingPairs
from src.petpptx.schemas.properties import Vector as SchemaVector
from src.petpptx.schemas.properties import Variant as SchemaVariant
from src.petpptx.schemas.properties import TitlesOfParts as SchemaTitlesOfParts


class _AppPropertiesBuilder:
    _schema: SchemaProperties = SchemaProperties

    @staticmethod
    def get_model():
        vector = SchemaVector(size=4,
                              base_type="variant",
                              lpstr="Theme",
                              variant=[SchemaVariant(i4=1),
                                       SchemaVariant(lpstr="Slide Titles"),
                                       SchemaVariant(i4=1),
                                       ]
                              )
        heading_pairs = SchemaHeadingPairs(vector=vector)
        vector_parts = SchemaVector(size=2,
                                    base_type="lpstr",
                                    lpstr="Office Theme",  # TODO посмотри XML и схему
                                    )
        titles_of_parts = SchemaTitlesOfParts(vector=vector_parts)
        model = SchemaProperties(total_time=0,
                                 words=0,
                                 application="Microsoft Office PowerPoint",
                                 presentation_format="On-screen Show (4:3)",
                                 paragraphs=0,
                                 slides=1,
                                 notes=0,
                                 hidden_slides=0,
                                 mmclips=0,
                                 scale_crop=False,
                                 heading_pairs=heading_pairs,
                                 titles_of_parts=titles_of_parts,
                                 company="Microsoft",
                                 links_up_to_date=False,
                                 shared_doc=False,
                                 hyperlinks_changed=False,
                                 app_version=Decimal(14.000),
                                 )
        return model


class AppProperties:
    _schema: SchemaProperties = SchemaProperties

    def __init__(self, file_path: str, model: Optional[SchemaProperties] = None):
        self._file_path = Path(file_path)
        self._model = model
        if self._model is None:
            self._model = _AppPropertiesBuilder.get_model()

    def get_model(self):
        return self._model
