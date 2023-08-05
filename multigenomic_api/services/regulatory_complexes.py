from ..models.regulatory_complexes import RegulatoryComplexes
from . import base


def get_all() -> [RegulatoryComplexes]:
    return base.get_all(RegulatoryComplexes)


def find_by_id(id_: str) -> RegulatoryComplexes:
    return base.find_one_by_id(RegulatoryComplexes, id_)


def find_by_name(name: str) -> RegulatoryComplexes:
    return RegulatoryComplexes.objects.get(abbreviated_name=name)


def find_by_product_id(product_id) -> str or None:
    return RegulatoryComplexes.objects(__raw__={"products.products_id": product_id})
