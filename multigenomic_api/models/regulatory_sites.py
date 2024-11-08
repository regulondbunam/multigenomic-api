from mongoengine import fields
from mongoengine import EmbeddedDocument
from mongoengine import DynamicDocument

from .biological_base import BiologicalBase


class RegulatorySites(DynamicDocument, BiologicalBase):
    absolute_position = fields.FloatField(required=False, db_field="absolutePosition")
    length = fields.IntField(required=False)
    organisms_id = fields.StringField(db_field="organisms_id")

    meta = {'collection': 'regulatorySites'}