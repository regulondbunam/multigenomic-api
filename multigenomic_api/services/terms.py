from ..models.terms import Terms
from . import base


def get_all() -> [Terms]:
    return base.get_all(Terms)


def find_by_id(id_: str) -> Terms:
    return base.find_one_by_id(Terms, id_)


def find_by_name(name: str) -> Terms:
    return base.find_by_name(Terms, name)


def get_associated_members_ids(id_: str, member_type) -> [str]:
    members = Terms.objects(_id=id_).only("members").first()
    members_ids = members["members"][member_type]
    return members_ids


def get_multifun_terms() -> [Terms]:
    return Terms.objects(ontologies_id="RDBONTOLMTF00001")


def get_by_subclass_id(term_id: str) -> [Terms]:
    return Terms.objects(sub_class_of=term_id)


def get_terms_by_gene_member_id(gene_id) -> [Terms]:
    return Terms.objects(members__genes=gene_id)
