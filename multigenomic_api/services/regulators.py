from ..models.regulators import Regulators
from . import base


def get_all() -> [Regulators]:
    return base.get_all(Regulators)


def find_by_id(id_: str) -> Regulators:
    return base.find_one_by_id(Regulators, id_)


def find_by_conformation(conf_id: str) -> [Regulators]:
    return Regulators.objects(__raw__={"conformations._id": conf_id})


def find_by_evidence_id(ev_id: str) -> Regulators:
    return base.find_by_evidence_id(Regulators, ev_id)
