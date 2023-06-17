from Logic.lexer import tokenize
from Logic.parser import parse


def parse_json_file(filename: str) -> dict[str, any]:
    with open(filename) as file:
        str_input = ''
        for line in file.readlines():
            str_input += line

        tokens = tokenize(str_input)
        (parsed_json, _) = parse(tokens, True)

    return parsed_json
