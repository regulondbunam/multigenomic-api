from mongoengine import fields
from mongoengine import DynamicDocument

from .biological_base import BiologicalBase


class Regulators(DynamicDocument, BiologicalBase):
    confidence_level = fields.StringField(required=True)
    abbreviated_name = fields.StringField(required=False)
    regulator_class = fields.StringField(required=True)
    type = fields.ListField(fields.StringField(), required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'regulators'}
