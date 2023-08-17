from mongoengine import fields
from mongoengine import DynamicDocument

from .biological_base import BiologicalBase


class TranscriptionUnits(DynamicDocument, BiologicalBase):
    genes_ids = fields.ListField(fields.StringField(), required=True)
    promoters_id = fields.StringField(required=False)
    operons_id = fields.StringField(required=True)
    terminators_ids = fields.ListField(fields.StringField(), required=False)
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    additive_evidences_ids = fields.ListField(required=False, db_field="additiveEvidences")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'transcriptionUnits'}