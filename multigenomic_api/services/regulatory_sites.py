from ..models.regulatory_sites import RegulatorySites
from ..services.transcription_factors import find_by_id as find_tf_by_id
from ..services.regulatory_interactions import find_by_regulator_id as find_reg_ints_by_regulator_id
from . import base


def get_all() -> [RegulatorySites]:
    return base.get_all(RegulatorySites)


def find_by_id(id_: str) -> RegulatorySites:
    return base.find_one_by_id(RegulatorySites, id_)


def find_by_evidence_id(ev_id: str) -> RegulatorySites:
    return base.find_by_evidence_id(RegulatorySites, ev_id)


def get_tf_binding_sites(tf_id: str) -> [RegulatorySites]:
    reg_sites_of_tf = []
    tf = find_tf_by_id(tf_id)
    for active_conformation in tf.active_conformations:
        reg_ints = find_reg_ints_by_regulator_id(active_conformation.id)
        for ri in reg_ints:
            if ri.regulatory_sites_id:
                reg_site = find_by_id(ri.regulatory_sites_id)
                if reg_site not in reg_sites_of_tf:
                    reg_sites_of_tf.append(reg_site)
    return reg_sites_of_tf


def find_by_sequence(sequence: str) -> [RegulatorySites]:
    return RegulatorySites.objects(__raw__={"sequence": sequence})
