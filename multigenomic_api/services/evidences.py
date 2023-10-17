from ..models.evidences import Evidences
from . import base


def get_all() -> [Evidences]:
    return base.get_all(Evidences)


def find_by_id(id_: str) -> Evidences:
    return base.find_one_by_id(Evidences, id_)


def find_one_by_code_rule(code: str) -> Evidences:
    return Evidences.objects(cv_code_rule=code)


def find_one_by_code(code: str) -> Evidences:
    return Evidences.objects.get(code=code)
