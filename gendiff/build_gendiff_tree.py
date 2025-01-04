def build_gendiff_tree(data1: dict, data2: dict) -> list:
    diff_tree = []
    keys = data1.keys() | data2.keys()

    for key in sorted(keys):
        if key not in data1:
            diff_tree.append({
                "name": key,
                "status": "added",
                "value": data2[key],
            })
        elif key not in data2:
            diff_tree.append({
                "name": key,
                "status": "deleted",
                "value": data1[key],
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_gendiff_tree(data1[key], data2[key])
            diff_tree.append({
                "name": key,
                "status": "nested",
                "children": children

            })
        elif data1[key] != data2[key]:
            diff_tree.append({
                "name": key,
                "status": "changed",
                "old_value": data1[key],
                "new_value": data2[key],
            })
        else:
            diff_tree.append({
                "name": key,
                "status": "unchanged",
                "value": data1[key]
            })

    return diff_tree
