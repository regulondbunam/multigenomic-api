from mongoengine import DynamicDocument
from mongoengine import fields

from .biological_base import BiologicalBase


class Motifs(DynamicDocument, BiologicalBase):
    alternate_sequence = fields.StringField(required=False, db_field="alternateSequence")
    attachedGroup = fields.StringField(required=False, db_field="attached_group")
    class_ = fields.StringField(required=False, db_field="class")
    data_source = fields.StringField(required=False, db_field="dataSource")
    description = fields.StringField(required=False)
    homology_motif = fields.StringField(required=False, db_field="homologyMotif")
    products_id = fields.StringField(required=False)
    residue_number = fields.ListField(fields.IntField(), required=False, db_field="residueNumber")
    type = fields.StringField(required=False)
    organisms_id = fields.StringField(db_field="organisms_id")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'motifs'}