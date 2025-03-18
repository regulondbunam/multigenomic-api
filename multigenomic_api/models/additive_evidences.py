from mongoengine import fields
from mongoengine import DynamicDocument

from .base import Base


class AdditiveEvidences(DynamicDocument, Base):
    code = fields.StringField(required=False)
    category = fields.StringField(required=False)
    pertains_to = fields.ListField(fields.StringField(), required=False, db_field="pertainsTo")
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    rules = fields.ListField(fields.StringField(), required=False)
    evidences_ids = fields.ListField(fields.StringField(), required=False, db_field="evidencesIds")
    additive_evidences_ids = fields.ListField(fields.StringField(), require=False, db_field="additiveEvidences")

    meta = {'collection': 'additiveEvidences'}