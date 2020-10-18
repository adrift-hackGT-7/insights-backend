import json


def make_item(id, variant, state, header, description):
    return {
        "id": id,
        "variant": variant,
        "state": state,
        "header": header,
        "description": description
    }


def make_group_element(item_list, id, header):
    return {"id": id, "header": header, "items": item_list}


def make_group(thing_list):
    return {"groups": thing_list}
