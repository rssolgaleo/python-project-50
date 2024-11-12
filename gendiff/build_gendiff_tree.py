def build_gendiff_tree(data1, data2):
    diff_tree = []
    keys = data1.keys() | data2.keys()

    for key in sorted(keys):
        if key not in data1:
            diff_tree.append(handle_added(key, data2[key]))
        elif key not in data2:
            diff_tree.append(handle_deleted(key, data1[key]))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff_tree.append(handle_nested(key, data1[key], data2[key]))
        elif data1[key] != data2[key]:
            diff_tree.append(handle_changed(key, data1[key], data2[key]))
        else:
            diff_tree.append(handle_unchanged(key, data1[key]))

    return diff_tree


def handle_added(key, value):
    return {
        "name": key,
        "status": "added",
        "value": value
    }


def handle_deleted(key, value):
    return {
        "name": key,
        "status": "deleted",
        "value": value
    }


def handle_nested(key, value1, value2):
    children = build_gendiff_tree(value1, value2)
    return {
        "name": key,
        "status": "nested",
        "children": children
    }


def handle_changed(key, old_value, new_value):
    return {
        "name": key,
        "status": "changed",
        "old_value": old_value,
        "new_value": new_value
    }


def handle_unchanged(key, value):
    return {
        "name": key,
        "status": "unchanged",
        "value": value
    }
