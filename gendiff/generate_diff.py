import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

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

    formatted_result = "{\n " + "\n ".join(result) + "\n}"
    return formatted_result
