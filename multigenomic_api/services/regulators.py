from ..models.regulators import Regulators
from . import base


def get_all() -> [Regulators]:
    return base.get_all(Regulators)


def find_by_id(id_: str) -> Regulators:
    return base.find_one_by_id(Regulators, id_)
