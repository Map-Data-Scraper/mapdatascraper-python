from typing import Union

QUERY_DELIMITER = '    '

def as_list(value: Union[list, str]) -> list:
    if isinstance(value, list):
        return value
    else:
        return [value]


def parse_fields(fields: Union[list, str]) -> str:
    if isinstance(fields, list):
        return ','.join(fields)
    else:
        return fields
