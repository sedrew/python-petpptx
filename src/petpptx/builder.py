from src.petpptx.handler.xml_handler import PptxXmlHandler
from src.petpptx.contet_type import ContentTypes
from src.petpptx.relationship import Relationships
from src.petpptx.constants import EnumRelationshipType
from src.petpptx.coreprops import CoreProperties
from src.petpptx.appprops import AppProperties


def create_minimal_presentation() -> PptxXmlHandler:
    handler = PptxXmlHandler()

    content_types = ContentTypes()

    _rels = Relationships(path_name="/_rels/.rels")
    _rels.add_target(type_value=EnumRelationshipType.OFFICE_DOCUMENT, target="ppt/presentation.xml")
    _rels.add_target(type_value=EnumRelationshipType.CORE_PROPERTIES, target="docProps/core.xml")
    _rels.add_target(type_value=EnumRelationshipType.EXTENDED_PROPERTIES, target="docProps/app.xml")
    _rels.add_target(type_value=EnumRelationshipType.THUMBNAIL, target="docProps/thumbnail.jpeg")

    core_props = CoreProperties("/docProps/core.xml")
    app_props = AppProperties("/docProps/app.xml")

    handler.add_model(path_name=core_props._path_name, model=core_props.get_model(), schema=core_props._schema)
    handler.add_model(path_name=app_props._path_name, model=app_props.get_model(), schema=app_props._schema)

    handler.add_model(path_name=content_types._path_name, model=content_types.get_model(), schema=content_types._schema)
    handler.add_model(path_name=_rels._path_name, model=_rels.get_model(), schema=_rels._schema)

    return handler





