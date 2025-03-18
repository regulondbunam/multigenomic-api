from ..models.regulatory_continuants import RegulatoryContinuants
from . import base


def get_all() -> [RegulatoryContinuants]:
    return base.get_all(RegulatoryContinuants)


def find_by_id(id_: str) -> RegulatoryContinuants:
    return base.find_one_by_id(RegulatoryContinuants, id_)


def find_by_evidence_id(ev_id: str) -> RegulatoryContinuants:
    return base.find_by_evidence_id(RegulatoryContinuants, ev_id)
