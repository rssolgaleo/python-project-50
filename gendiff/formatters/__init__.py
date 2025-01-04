from gendiff.formatters.stylish import default_formatter
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.json import json_formatter


def diff_formatter(diff, format: str) -> dict:
    if format == 'stylish':
        return default_formatter(diff)
    elif format == 'plain':
        return plain_formatter(diff)
    elif format == 'json':
        return json_formatter(diff)
