from mongoengine import fields
from mongoengine import DynamicDocument

from .base import Base


class Evidences(DynamicDocument, Base):
    ev_class = fields.StringField(required=False, db_field="class")
    code = fields.StringField(required=False)
    head = fields.StringField(required=False)
    pertains_to = fields.ListField(fields.StringField(), required=False, db_field="pertainsTo")
    type = fields.ListField(fields.StringField(), required=False, db_field="type")
    cv_code_rule = fields.ListField(fields.StringField(), required=False, db_field="crossEvidenceCodeRule")
    category = fields.ListField(fields.StringField(), required=False, db_field="evidenceCategory")
    approach = fields.ListField(fields.StringField(), required=False, db_field="evidenceApproach")
    note_web = fields.ListField(fields.StringField(), required=False, db_field="noteWeb")

    meta = {'collection': 'evidences'}
