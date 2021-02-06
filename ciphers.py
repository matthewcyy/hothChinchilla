"""
Caesar cipher
"""

import string


def string_to_digits(text: str):
    """
    :param text: input text to convert into digits
    :return digit_list: list of indices in string_uppercase
    """
    digit_list = []
    for letter in text:
        letter = letter.upper()
        if letter not in string.ascii_uppercase:
            continue
        digit_list.append(string.ascii_uppercase.index(letter))

    return digit_list


def digits_to_string(digit_list: list):
    """
    :param digit_list: input digit list to convert back to str
    :return out: output string
    """
    out = ""
    for digit in digit_list:
        out += string.ascii_uppercase[digit]
    return out


def caesar_cipher(message: str, shift: int):
    """
    Shifts str forward by
    :param shift: int
    :param message:
    :return :
    """
    digit_list = string_to_digits(message)
    for i, digit in enumerate(digit_list):
        digit_list[i] = (digit + shift) % 26
    return digits_to_string(digit_list)
