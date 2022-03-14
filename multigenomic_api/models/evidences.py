from mongoengine import fields
from mongoengine import DynamicDocument

from .base import Base


class Evidences(DynamicDocument, Base):
    ev_class = fields.StringField(required=False, db_field="class")
    code = fields.StringField(required=False)
    head = fields.StringField(required=False)
    pertains_to = fields.ListField(fields.StringField(), required=False, db_field="pertainsTo")
    type = fields.ListField(fields.StringField(), required=False, db_field="type")

    meta = {'collection': 'evidences'}
