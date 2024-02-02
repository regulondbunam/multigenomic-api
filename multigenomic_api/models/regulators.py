from mongoengine import fields
from mongoengine import DynamicDocument

from .biological_base import BiologicalBase


class Regulators(DynamicDocument, BiologicalBase):
    confidence_level = fields.StringField(required=True, db_field="confidenceLevel")
    abbreviated_name = fields.StringField(required=False, db_field="abbreviatedName")
    regulator_class = fields.ListField(required=False, db_field="regulatorClass")
    regulation_type = fields.StringField(required=False, db_field="regulationType")
    type = fields.ListField(fields.StringField(), required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'regulators'}
