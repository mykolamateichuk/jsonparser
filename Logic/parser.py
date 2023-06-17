from Definitions.json_syntax import *


def parse(tokens: list, root: bool = False) -> tuple[dict | list, list]:
    token = tokens[0]

    if token != OPENING_BRACE and root:
        raise Exception("Root must be an object!")

    if token == OPENING_BRACE:
        return parse_object(tokens[1:])
    elif token == OPENING_BRACKET:
        return parse_array(tokens[1:])
    else:
        return token, tokens[1:]


def parse_object(tokens: list) -> tuple[dict, list]:
    json_object = {}

    token = tokens[0]
    if token == CLOSING_BRACE:
        return json_object, tokens[1:]

    while True:
        json_key = tokens[0]
        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception(f'Expected string key, got: {json_key}')

        if tokens[0] != COLON:
            raise Exception(f'Expected colon after key in object, got: {token}')

        json_value, tokens = parse(tokens[1:])

        json_object[json_key] = json_value

        token = tokens[0]
        if token == CLOSING_BRACE:
            return json_object, tokens[1:]
        elif token != COMMA:
            raise Exception(f'Expected comma after pair in object, got: {token}')

        tokens = tokens[1:]


def parse_array(tokens: list) -> tuple[list, list]:
    json_array = []

    token = tokens[0]
    if token == CLOSING_BRACKET:
        return json_array, tokens[1:]

    while True:
        json, tokens = parse(tokens)
        json_array.append(json)

        token = tokens[0]
        if token == CLOSING_BRACKET:
            return json_array, tokens[1:]
        elif token != COMMA:
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]
