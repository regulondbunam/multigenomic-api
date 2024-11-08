from mongoengine import fields
from mongoengine import EmbeddedDocument
from mongoengine import DynamicDocument

from .biological_base import BiologicalBase
from .biological_base import TermParent


class Fragments(EmbeddedDocument, BiologicalBase):
    centisome_position = fields.FloatField(required=False, db_field="centisomePosition")
    meta = {'abstract': True}


class Parents(EmbeddedDocument, TermParent):
    meta = {'abstract': True}
    pass


class Terms(EmbeddedDocument, TermParent):
    term_label = fields.StringField(required=False, db_field="termLabel")
    parents = fields.EmbeddedDocumentListField(Parents)
    meta = {'abstract': True}


class Genes(DynamicDocument, BiologicalBase):
    bnumber = fields.StringField(required=False, db_field="bnumber")
    centisome_position = fields.FloatField(required=False, db_field="centisomePosition")
    fragments = fields.EmbeddedDocumentListField(Fragments, required=False)
    gc_content = fields.FloatField(required=False, db_field="gcContent")
    interrupted = fields.BooleanField(required=False)
    terms = fields.EmbeddedDocumentListField(Terms, required=False)
    type = fields.StringField(required=False)
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    additive_evidences_ids = fields.ListField(required=False, db_field="additiveEvidences")
    organisms_id = fields.StringField(db_field="organisms_id")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'genes'}