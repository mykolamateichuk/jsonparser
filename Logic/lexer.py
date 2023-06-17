from Definitions.json_syntax import *
from Definitions.lexer_defines import *
from Logic.utilities import *


def tokenize(json_string: str) -> list[str]:
    tokens = []

    while len(json_string):
        json_string, str_token = tokenize_str(json_string)
        if str_token:
            tokens.append(str_token)
            continue

        json_string, num_token = tokenize_number(json_string)
        if num_token:
            tokens.append(num_token)
            continue

        json_string, bool_token = tokenize_bool(json_string)
        if bool_token:
            tokens.append(bool_token)
            continue

        json_string, null_token = tokenize_null(json_string)
        if null_token:
            tokens.append(null_token)
            continue

        char = json_string[0]

        if char in WHITESPACE:
            json_string = update_input(json_string)
        elif char in SYNTAX:
            tokens.append(char)
            json_string = update_input(json_string)
        else:
            raise Exception(f"Unknown token '{char}'!")

    return tokens


def tokenize_str(json_string: str) -> Token:
    str_token = ''

    if json_string[0] == QUOTE:
        json_string = update_input(json_string, 1)
    else:
        return Token(json_string)

    for char in json_string:
        if char == QUOTE:
            json_string = update_input(json_string, len(str_token) + 1)
            return Token(json_string, str_token)
        else:
            str_token += char

    raise Exception("No closing quote in a string token!")


def tokenize_number(json_string: str) -> Token:
    num_token = ''

    for char in json_string:
        if char not in NUMBER_CHARS:
            break

        num_token += char

    json_string = update_input(json_string, len(num_token))

    if len(num_token) == 0:
        return Token(json_string)
    elif DOT in num_token:
        return Token(json_string, float(num_token))
    else:
        return Token(json_string, int(num_token))


def tokenize_bool(json_string: str) -> Token:
    input_len = len(json_string)

    if json_string[:LEN_TRUE] == TRUE and input_len >= LEN_TRUE:
        json_string = update_input(json_string, LEN_TRUE)
        return Token(json_string, True)
    elif json_string[:LEN_FALSE] == FALSE and input_len >= LEN_FALSE:
        json_string = update_input(json_string, LEN_FALSE)
        return Token(json_string, False)
    else:
        return Token(json_string)


def tokenize_null(json_string: str) -> Token:
    if json_string[:LEN_NULL] == NULL and len(json_string) >= LEN_NULL:
        json_string = update_input(json_string, LEN_NULL)
        return Token(json_string, None)
    else:
        return Token(json_string)
