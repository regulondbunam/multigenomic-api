from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument

from .biological_base import BiologicalBase


class Products(DynamicEmbeddedDocument):
    product_id = fields.StringField(required=True)
    coefficient = fields.IntField(required=False)
    meta = {'abstract': True}


class RegulatoryComplexes(DynamicDocument, BiologicalBase):

    abbreviated_name = fields.StringField(required=False, db_field="abbreviatedName")
    function = fields.StringField(required=False, db_field="function")
    is_transcription_factor = fields.BooleanField(required=False, db_field="isTranscriptionFactor")
    products = fields.EmbeddedDocumentListField(Products, required=False)
    regulatory_continuants_ids = fields.ListField(fields.StringField(), required=False, db_field="regulatoryContinuants_ids")
    type = fields.StringField(required=False)
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    additive_evidences_ids = fields.ListField(required=False, db_field="additiveEvidences")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'regulatoryComplexes'}
