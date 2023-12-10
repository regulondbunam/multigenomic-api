def get_all(model):
    return model.objects.timeout(False).order_by('id')


def find_one_by_id(model, object_id: str):
    return model.objects.get(_id=object_id)


def find_by_name(model, name: str):
    return model.objects.get(name=name)


def find_by_evidence_id(model, ev_id: str):
    return model.objects(citations__evidences_id=ev_id)