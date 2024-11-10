def build_gendiff_tree(data1, data2):
    result = []
    keys = data1.keys() | data2.keys()

    for key in sorted(keys):
        if key not in data1:
            result.append(f"+ {key}: {data2[key]}")
        elif key not in data2:
            result.append(f"- {key}: {data1[key]}")
        elif data1[key] != data2[key]:
            result.append(f"- {key}: {data1[key]}")
            result.append(f"+ {key}: {data2[key]}")
        else:
            result.append(f"  {key}: {data1[key]}")

    diff = "{\n " + "\n ".join(result) + "\n}"
    return diff
