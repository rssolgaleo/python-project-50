DEL, ADD, DEF = '  - ', '  + ', '    '


def to_str(key, value, depth):
    if value is None:
        return f"{key}: null"
    elif isinstance(value, bool):
        return f"{key}: {str(value).lower()}"
    elif isinstance(value, dict):
        return format_dict(key, value, depth)
    else:
        return f"{key}: {value}"


def format_dict(key, value, depth):
    indent = DEF * depth
    lines = [f"{key}: {{"]
    for k, v in value.items():
        lines.append(f"{indent}{DEF}{to_str(k, v, depth + 1)}")
    lines.append(f"{indent}}}")
    return '\n'.join(lines)


def format_diff_unit(unit_diff, depth):
    status = unit_diff['status']
    indent = DEF * (depth - 1)
    name = unit_diff['name']

    if status == 'added':
        return f"{indent}{ADD}{to_str(name, unit_diff['value'], depth)}"
    elif status == 'deleted':
        return f"{indent}{DEL}{to_str(name, unit_diff['value'], depth)}"
    elif status == 'unchanged':
        return f"{indent}{DEF}{to_str(name, unit_diff['value'], depth)}"
    elif status == 'nested':
        return f"{indent}{DEF}{name}: {make_diff(unit_diff['children'],
                                                depth + 1)}"
    elif status == 'changed':
        return (f"{indent}{DEL}{to_str(name, unit_diff['old_value'], depth)}\n"
                f"{indent}{ADD}{to_str(name, unit_diff['new_value'], depth)}")


def make_diff(diff_tree, depth=1):
    lines = [format_diff_unit(unit, depth) for unit in diff_tree]
    output = "{\n" + "\n".join(lines) + f"\n{DEF * (depth - 1)}}}"
    return output


def default_formatter(diff_tree):
    return make_diff(diff_tree)
