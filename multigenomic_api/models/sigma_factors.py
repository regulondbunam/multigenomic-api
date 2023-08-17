from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument

from .biological_base import BiologicalBase


class SigmaFactors(DynamicDocument, BiologicalBase):
    genes_id = fields.StringField(required=True)
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    additive_evidences_ids = fields.ListField(required=False, db_field="additiveEvidences")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'sigmaFactors'}