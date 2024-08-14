from pathlib import Path
from typing import Optional

from src.petpptx.mixin_handler import MixinHandler
from src.petpptx.schemas.relationships import Relationships as XmlRelationships
from src.petpptx.schemas.relationships import Relationship as XmlRelationship


class RID:
    ...


class Relationships:
    _schema: XmlRelationships = XmlRelationships

    def __init__(self, file_path: str, part: MixinHandler):
        self._file_path = file_path
        self._part = part
        if self._part.has_model(self._file_path):
            self._model = part.deserialize_model(file_path=self._file_path, schema=self._schema)
        else:
            self._model = self._part.set_model(file_path=self._file_path, model=self._schema())

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

    def add_target(self, target, type_value=None, rid=None):
        if rid is None:
            rid = self.create_new_rid()
        rel = XmlRelationship(id=rid, type_value=type_value, target=target)
        self._model.relationship.append(rel)

    def remove_target(self, target):
        for idx, el in enumerate(self._model.relationship):
            if target == el.target:
                self._model.relationship.pop(idx)
                break
