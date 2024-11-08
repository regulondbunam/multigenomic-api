from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument
from mongoengine import EmbeddedDocument

from .base import Base


class TranscriptionTerminationSite(DynamicEmbeddedDocument):
    left_end_position = fields.IntField(required=False, db_field="leftEndPosition")
    right_end_position = fields.IntField(required=False, db_field="rightEndPosition")
    range = fields.StringField(required=False)
    type = fields.StringField(required=False)
    meta = {'abstract': True}


class Citations(EmbeddedDocument):
    publications_id = fields.StringField(required=False)
    evidences_id = fields.StringField(required=False)


class ExternalCrossReferences(EmbeddedDocument):
    external_cross_references_id = fields.StringField(required=False, db_field="externalCrossReferences_id")
    object_id = fields.StringField(required=False, db_field="objectId")


class Terminators(DynamicDocument, Base):
    citations = fields.EmbeddedDocumentListField(Citations, db_field="citations")
    external_cross_references = fields.EmbeddedDocumentListField(ExternalCrossReferences, db_field="externalCrossReferences")
    class_ = fields.StringField(required=False, db_field="class")
    transcriptionTerminationSite = fields.EmbeddedDocumentField(TranscriptionTerminationSite, required=True)
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    additive_evidences_ids = fields.ListField(required=False, db_field="additiveEvidences")
    organisms_id = fields.StringField(db_field="organisms_id")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'terminators'}