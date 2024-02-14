from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import EmbeddedDocument

from .biological_base import BiologicalBase


class Conformations(EmbeddedDocument):
    id = fields.StringField(required=True, db_field="_id")
    type = fields.StringField(required=True, db_field="type")
    class_ = fields.StringField(required=True, db_field="class")

    meta = {'abstract': True}

class Regulators(DynamicDocument, BiologicalBase):
    confidence_level = fields.StringField(required=True, db_field="confidenceLevel")
    conformations = fields.EmbeddedDocumentListField(Conformations, required=True, db_field="conformations")
    abbreviated_name = fields.StringField(required=False, db_field="abbreviatedName")
    regulator_class = fields.ListField(required=False, db_field="regulatorClass")
    regulation_type = fields.StringField(required=False, db_field="regulationType")
    type = fields.ListField(fields.StringField(), required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'regulators'}
