from mongoengine import fields
from mongoengine import DynamicDocument

from .biological_base import BiologicalBase


class RegulatoryContinuants(DynamicDocument, BiologicalBase):

    is_regulator = fields.StringField(required=False, db_field="isRegulator")
    type = fields.StringField(required=False)
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    additive_evidences_ids = fields.ListField(required=False, db_field="additiveEvidences")
    organisms_id = fields.StringField(db_field="organisms_id")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'regulatoryContinuants'}
