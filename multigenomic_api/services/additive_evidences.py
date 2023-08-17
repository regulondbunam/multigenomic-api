from ..models.additive_evidences import AdditiveEvidences
from . import base


def get_all() -> [AdditiveEvidences]:
    return base.get_all(AdditiveEvidences)


def find_by_id(id_: str) -> AdditiveEvidences:
    return base.find_one_by_id(AdditiveEvidences, id_)
