from ..models.transcription_units import TranscriptionUnits
from . import base


def get_all():
    return base.get_all(TranscriptionUnits)


def find_by_id(id_: str):
    return base.find_one_by_id(TranscriptionUnits, id_)


def find_by_evidence_id(ev_id: str) -> TranscriptionUnits:
    return base.find_by_evidence_id(TranscriptionUnits, ev_id)


def find_by_operon_id(operons_id: str) -> [TranscriptionUnits]:
    return TranscriptionUnits.objects(operons_id=operons_id)


def find_by_gene_id(gene_id: str) -> [TranscriptionUnits]:
    return TranscriptionUnits.objects(genes_ids=gene_id)


def find_by_promoter_id(promoter_id: str) -> [TranscriptionUnits]:
    return TranscriptionUnits.objects(promoters_id=promoter_id)


def get_operons_id_by_gene_id(gene_id: str) -> str:
    transcription_units = TranscriptionUnits.objects(genes_ids=gene_id)
    operon_ids = [tu.operons_id for tu in transcription_units]
    operon_ids = list(set(operon_ids))
    if len(operon_ids) == 1:
        operons_id = ''.join(operon_ids)
    else:
        raise ValueError
    return operons_id


def find_by_terminator_id(terminator_id: str):
    return TranscriptionUnits.objects(terminators_ids=terminator_id)

