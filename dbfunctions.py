from flask_lists.app import Lists
from flask_lists.app import Items


def get_items_from_list(list_name):
    current_list = Lists().query.filter_by(list_name=list_name).first().list_items
    print(current_list)
    item_ids_array = current_list.split("_")

    all_items = Items().query.all()
    item_names_array = []

    for i in item_ids_array:
        item_names_array.append({
            "name": get_name_by_id(i),
            "id": i
        })

    return item_names_array


def get_name_by_id(id):
    if id.startswith("1"):
        print("starts with 1")
        return Lists().query.filter_by(id=id).first().list_name
    elif id.startswith("0"):
        print("starts with 0")
        return Items().query.filter_by(id=id).first().item_name


def get_all_Items():
    return_array = []

    all_items = Items().query.all()

    for i in all_items:
        return_array.append({
            "name": i.item_name,
            "id": i.id
        })

    return return_array
