from ..models.regulatory_interactions import RegulatoryInteractions
from . import base


def get_all() -> [RegulatoryInteractions]:
    return base.get_all(RegulatoryInteractions)


def find_by_id(id_: str) -> RegulatoryInteractions:
    return base.find_one_by_id(RegulatoryInteractions, id_)


def find_by_regulated_entity_ids(regulated_entity_ids: [str]) -> [RegulatoryInteractions]:
    regulatery_interactions = []
    for regulated_entity_id in regulated_entity_ids:
        regulatery_interactions.append(RegulatoryInteractions.objects.filter(RegulatoryInteractions={"_id": regulated_entity_id}))
    return regulatery_interactions


def find_regulator_by_regulated_entity_id(regulated_entity_id: str) -> [RegulatoryInteractions.regulator]:
    regulators = RegulatoryInteractions.objects().filter(regulatedEntity__match={"_id": regulated_entity_id}).distinct("regulator")
    for regulator in regulators:
        regulator["id"] = regulator.id
    return regulators


def find_regulators_by_regulated_entity_ids(regulated_entity_ids: [str]) -> [RegulatoryInteractions.regulator]:
    regulated_entities_regulators = []
    for regulated_entity_id in regulated_entity_ids:
        regulatory_interactions = RegulatoryInteractions.objects(__raw__={"regulatedEntity._id": regulated_entity_id})
        for ri in regulatory_interactions:
            if ri.regulator:
                ri.regulator["function"] = ri.function
                if ri.regulator not in regulated_entities_regulators:
                    regulated_entities_regulators.append(ri.regulator)
    return regulated_entities_regulators


def find_regulatory_interactions_by_reg_entity_id(reg_ent_id: str) -> [RegulatoryInteractions]:
    return RegulatoryInteractions.objects(__raw__={"regulatedEntity._id": reg_ent_id})


def find_by_regulator_id(regulator_id: str) -> [RegulatoryInteractions]:
    return RegulatoryInteractions.objects(__raw__={"regulator._id": regulator_id})


def find_by_reg_site(reg_site: str) -> [RegulatoryInteractions]:
    return RegulatoryInteractions.objects(regulatory_sites_id=reg_site)
