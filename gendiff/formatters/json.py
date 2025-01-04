import json


def json_formatter(diff: dict) -> dict:
    return json.dumps(diff, indent=4)
