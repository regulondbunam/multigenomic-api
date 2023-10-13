from ..models.promoters import Promoters
from . import base


def get_all() -> [Promoters]:
    return base.get_all(Promoters)


def find_by_id(id_: str) -> Promoters:
    return base.find_one_by_id(Promoters, id_)


def find_by_evidence_id(ev_id: str) -> Promoters:
    return base.find_by_evidence_id(Promoters, ev_id)


def find_by_sigma_factor_id(sigma_factor_id: str) -> Promoters:
    return Promoters.objects(__raw__={"bindsSigmaFactor.sigmaFactors_id": sigma_factor_id})


def get_closer_promoters(left_end_pos: int, right_end_pos: int) -> [Promoters]:
    promoters = Promoters.objects(__raw__={"$or": [
                                      {"$and": [
                                          {"transcriptionStartSite.leftEndPosition": {"$gte": left_end_pos}},
                                          {"transcriptionStartSite.rightEndPosition": {"$lte": right_end_pos}}
                                      ]},
                                      {"$and": [
                                          {"transcriptionStartSite.leftEndPosition": {"$lt": left_end_pos}},
                                          {"transcriptionStartSite.rightEndPosition": {"$gt": left_end_pos, "$lte": right_end_pos}}
                                      ]},
                                      {"$and": [
                                          {"transcriptionStartSite.leftEndPosition": {"$gte": left_end_pos, "$lte": right_end_pos}},
                                          {"transcriptionStartSite.rightEndPosition": {"$gt": right_end_pos}}
                                      ]},
                                      {"$and": [
                                          {"transcriptionStartSite.leftEndPosition": {"$lte": left_end_pos}},
                                          {"transcriptionStartSite.rightEndPosition": {"$gte": right_end_pos}}
                                      ]}
                                    ]})
    return promoters
