from pathlib import Path
from typing import Optional

from src.petpptx.schemas.relationships import Relationships as XmlRelationships
from src.petpptx.schemas.relationships import Relationship as XmlRelationship


class Relationships:
    _schema: XmlRelationships = XmlRelationships

    def __init__(self, path_name: str, model: Optional[XmlRelationships] = None):
        self._path_name = Path(path_name)
        self._model = model
        if self._model is None:
            self._model = self._schema()

    def get_model(self):
        return self._model

    def create_new_rid(self, safety_mode=True) -> str:
        rid = f"rId{len(self._model.relationship)}"
        if not safety_mode:
            return rid
        max_id = 0
        for el in self._model.relationship:
            max_id = max(max_id, int(el.id.replace("rId", "")))
        return f"rId{max_id + 1}"

    def get_model_by_rid(self, rid: str) -> XmlRelationship:
        for el in self._model.relationship:
            if el.id == rid:
                return el

    def get_model_by_target(self, target: str) -> XmlRelationship:
        for el in self._model.relationship:
            if el.target == target:
                return el

    def add_target(self, type_value, target,  rid=None):
        if rid is None:
            rid = self.create_new_rid()
        rel = XmlRelationship(id=rid, type_value=type_value, target=target)
        self._model.relationship.append(rel)

    def remove_target(self, target):
        ...
