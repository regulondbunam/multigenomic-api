from ..models.transcription_factor import TranscriptionFactors
from mongoengine.queryset.visitor import Q
from mongoengine.errors import DoesNotExist
from . import base


def get_all() -> [TranscriptionFactors]:
    return base.get_all(TranscriptionFactors)


def find_by_id(id_: str) -> TranscriptionFactors:
    return base.find_one_by_id(TranscriptionFactors, id_)


def find_by_name(name: [str]) -> [TranscriptionFactors]:
    try:
        return TranscriptionFactors.objects.get(name=name)
    except DoesNotExist:
        return None


def find_tf_id_by_product_id(product_id) -> str or None:
    return TranscriptionFactors.objects(products_ids=product_id)


def find_tf_id_by_conformation_id(active_conf_id) -> [str] or None:
    try:
        return TranscriptionFactors.objects(Q(active_conformations__id=active_conf_id) | Q(products_ids=active_conf_id) | Q(_id=active_conf_id))
    except DoesNotExist:
        return None


def find_tf_id_by_conformation_name(active_conf_name) -> [str] or None:
    try:
        return TranscriptionFactors.objects(Q(name=active_conf_name))
    except DoesNotExist:
        return None
