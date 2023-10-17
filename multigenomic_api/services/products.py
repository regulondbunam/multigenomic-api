from ..models.products import Products
from . import base


def get_all() -> [Products]:
    return base.get_all(Products)


def find_by_id(id_: str) -> Products:
    return base.find_one_by_id(Products, id_)


def find_by_name(name: str) -> Products:
    return Products.objects.get(name=name)


def find_by_gene_id(genes_id: str) -> Products:
    return Products.objects(genes_id=genes_id)

def get_all_srnas() -> Products:
    return Products.objects(type="small RNA")
