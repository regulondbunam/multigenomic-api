from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument

from .biological_base import BiologicalBase
from .biological_base import Citations
from .biological_base import TermParent


class GOTerm(DynamicEmbeddedDocument, TermParent):
    citations = fields.EmbeddedDocumentListField(Citations, db_field="citations")

    meta = {'abstract': True}


class ProductTerms(DynamicEmbeddedDocument):
    biological_process = fields.EmbeddedDocumentListField(GOTerm, required=False, db_field="biologicalProcess")
    cellular_component = fields.EmbeddedDocumentListField(GOTerm, required=False, db_field="cellularComponent")
    molecular_function = fields.EmbeddedDocumentListField(GOTerm, required=False, db_field="molecularFunction")
    meta = {'abstract': True}


class Products(DynamicDocument, BiologicalBase):
    abbreviated_name = fields.StringField(required=False, db_field="abbreviatedName")
    anticodon = fields.StringField(required=False)
    catalyzes = fields.ListField(required=False)
    coding_segments = fields.ListField(fields.ListField(fields.IntField()), required=False, db_field="codingSegments")
    component_of = fields.ListField(fields.StringField(), required=False, db_field="componentOf")
    consensus_sequences = fields.ListField(fields.StringField(), required=False, db_field="consensusSequences")
    genes_id = fields.StringField(required=True)
    isoelectric_point = fields.FloatField(required=False, db_field="isoelectricPoint")
    is_transcription_factor = fields.BooleanField(required=False, db_field="isTranscriptionFactor")
    locations = fields.ListField(fields.StringField(), required=False)
    modified_forms = fields.ListField(fields.StringField(), required=False, db_field="modifiedForms")
    molecular_weight = fields.FloatField(required=False, db_field="molecularWeight")
    molecular_weights_kd = fields.ListField(fields.FloatField(), required=False, db_field="molecularWeightsKd")
    site_length = fields.ListField(fields.IntField(), required=False, db_field="siteLength")
    splice_form_introns = fields.ListField(fields.ListField(fields.IntField()), required=False, db_field="spliceFormIntrons")
    symmetries = fields.ListField(fields.StringField(), required=False)
    terms = fields.EmbeddedDocumentField(ProductTerms, required=False)
    type = fields.StringField(required=False)
    confidence_level = fields.StringField(required=False, db_field="confidenceLevel")
    additive_evidences_ids = fields.ListField(required=False, db_field="additiveEvidences")
    organisms_id = fields.StringField(db_field="organisms_id")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'products'}