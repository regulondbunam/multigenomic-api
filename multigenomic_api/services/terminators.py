from ..models.terminators import Terminators
from . import base


def get_all():
    return base.get_all(Terminators)


def find_by_id(id_: str):
    return base.find_one_by_id(Terminators, id_)


def get_closer_terminators(left_end_pos: int, right_end_pos: int) -> [Terminators]:
    terminators = Terminators.objects(__raw__={"$or": [
                                      {"$and": [
                                          {"transcriptionTerminationSite.leftEndPosition": {"$gte": left_end_pos}},
                                          {"transcriptionTerminationSite.rightEndPosition": {"$lte": right_end_pos}}
                                      ]},
                                      {"$and": [
                                          {"transcriptionTerminationSite.leftEndPosition": {"$lt": left_end_pos}},
                                          {"transcriptionTerminationSite.rightEndPosition": {"$gt": left_end_pos, "$lte": right_end_pos}}
                                      ]},
                                      {"$and": [
                                          {"transcriptionTerminationSite.leftEndPosition": {"$gte": left_end_pos, "$lte": right_end_pos}},
                                          {"transcriptionTerminationSite.rightEndPosition": {"$gt": right_end_pos}}
                                      ]},
                                      {"$and": [
                                          {"transcriptionTerminationSite.leftEndPosition": {"$lte": left_end_pos}},
                                          {"transcriptionTerminationSite.rightEndPosition": {"$gte": right_end_pos}}
                                      ]}
                                    ]})
    return terminators
