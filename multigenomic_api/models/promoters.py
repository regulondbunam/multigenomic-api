from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument


from .biological_base import BiologicalBase
from .biological_base import Citations


class BindsSigmaFactor(DynamicEmbeddedDocument):
    sigma_factors_id = fields.StringField(required=False, db_field="sigmaFactors_id")
    citations = fields.EmbeddedDocumentListField(Citations, required=False, db_field="citations")

    meta = {'abstract': True}


class Boxes(DynamicEmbeddedDocument):
    left_end_position = fields.IntField(required=False, db_field="leftEndPosition")
    right_end_position = fields.IntField(required=False, db_field="rightEndPosition")
    sequence = fields.StringField(required=False)
    type = fields.StringField(required=False)

    meta = {'abstract': True}


class TranscriptionStartSite(DynamicEmbeddedDocument):
    left_end_position = fields.IntField(required=False, db_field="leftEndPosition")
    right_end_position = fields.IntField(required=False, db_field="rightEndPosition")
    range = fields.StringField(required=False)
    type = fields.StringField(required=False)

    meta = {'abstract': True}


class Promoters(DynamicDocument, BiologicalBase):
    binds_sigma_factor = fields.EmbeddedDocumentField(BindsSigmaFactor, required=False, db_field="bindsSigmaFactor")
    boxes = fields.EmbeddedDocumentListField(Boxes, required=False, db_field="boxes")
    pos1 = fields.IntField(required=False)
    score = fields.FloatField(required=False)
    transcription_start_site = fields.EmbeddedDocumentField(TranscriptionStartSite, required=False, db_field="transcriptionStartSite")
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    additive_evidences_ids = fields.ListField(required=False, db_field="additiveEvidences")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'promoters'}
