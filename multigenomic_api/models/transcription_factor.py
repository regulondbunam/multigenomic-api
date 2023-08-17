from mongoengine import fields
from mongoengine import EmbeddedDocument
from mongoengine import DynamicDocument

from .biological_base import BiologicalBase


class Conformations(EmbeddedDocument):
    id = fields.StringField(required=True, db_field="_id")
    type = fields.StringField(required=True, db_field="type")

    meta = {'abstract': True}


class TranscriptionFactors(DynamicDocument, BiologicalBase):
    active_conformations = fields.EmbeddedDocumentListField(Conformations, required=True, db_field="activeConformations")
    connectivity_class = fields.StringField(required=False, db_field="connectivityClass")
    global_function = fields.StringField(required=True, db_field="globalFunction")
    inactive_conformations = fields.EmbeddedDocumentListField(Conformations, required=False, db_field="inactiveConformations")
    products_ids = fields.ListField(fields.StringField(), db_field="products_ids")
    sensing_class = fields.StringField(required=False, db_field="sensingClass")
    site_length = fields.ListField(fields.StringField(), db_field="siteLength")
    symmetry = fields.StringField(required=False, db_field="symmetry")
    family = fields.StringField(required=False, db_field="family")
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    additive_evidences_ids = fields.ListField(required=False, db_field="additiveEvidences")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'transcriptionFactors'}