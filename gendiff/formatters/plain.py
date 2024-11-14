def to_plain_value(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_plain(diff_tree, parentkey=''):
    lines = []

    for unit in diff_tree:
        key_path = f"{parentkey}.{unit['name']}" if parentkey else unit['name']
        status = unit['status']
        if status == 'added':
            value = to_plain_value(unit['value'])
            lines.append(f"Property '{key_path}' was added with value: {value}")
        elif status == 'deleted':
            lines.append(f"Property '{key_path}' was removed")
        elif status == 'changed':
            old_value = to_plain_value(unit['old_value'])
            new_value = to_plain_value(unit['new_value'])
            lines.append((
                f"Property '{key_path}' was updated. "
                f"From {old_value} to {new_value}"
            ))
        elif status == 'nested':
            nested_lines = format_plain(unit['children'], key_path)
            lines.extend(nested_lines)

    return lines


def plain_formatter(diff_tree):
    lines = format_plain(diff_tree)
    return '\n'.join(lines)
