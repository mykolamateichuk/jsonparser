from typing import NamedTuple


class Token(NamedTuple):
    json_string: str
    token: any = None


def update_input(json_string: str, num_characters: int = 1) -> str:
    return json_string[num_characters:]
