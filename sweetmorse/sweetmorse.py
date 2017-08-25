#!/usr/bin/env python3

import itertools
import string

LOWERCASE_CHARS = set(string.ascii_lowercase)

PLAIN_TEXT_TO_HUMAN_READABLE = {
    'A': '._',
    'B': '_...',
    'C': '_._.',
    'D': '_..',
    'E': '.',
    'F': '.._.',
    'G': '__.',
    'H': '....',
    'I': '..',
    'J': '.___',
    'K': '_._',
    'L': '._..',
    'M': '__',
    'N': '_.',
    'O': '___',
    'P': '.__.',
    'Q': '__._',
    'R': '._.',
    'S': '...',
    'T': '_',
    'U': '.._',
    'V': '..._',
    'W': '.__',
    'X': '_.._',
    'Y': '_.__',
    'Z': '__..',
    '0': '_____',
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.',
    '.': '._._._',
    ',': '--..--',
    '?': '..__..',
    '\'': '.___.',
    '!': '_._.__',
    '/': '_.._.',
    '(': '_.__.',
    ')': '_.__._',
    '&': '._...',
    ':': '___...',
    ';': '_._._.',
    '=': '_..._',
    '+': '._._.',
    '-': '_...._',
    '_': '..__._',
    '"': '._.._.',
    '$': '..._.._',
    '@': '.__._.',
    ' ': ' ',
}
PLAIN_TEXT_CHAR_GAP = ''
PLAIN_TEXT_WORD_GAP = ' '
PLAIN_TEXT_CHARS = set(
    char
    for char in PLAIN_TEXT_TO_HUMAN_READABLE.keys()
    if char != PLAIN_TEXT_WORD_GAP
)
PLAIN_TEXT_ALPHABET = PLAIN_TEXT_CHARS.union({PLAIN_TEXT_WORD_GAP})

HUMAN_READABLE_TO_PLAIN_TEXT = {
    v: k
    for k, v in PLAIN_TEXT_TO_HUMAN_READABLE.items()
}
HUMAN_READABLE_CHAR_GAP = ' '
HUMAN_READABLE_WORD_GAP = '   '
HUMAN_READABLE_CHARS = set(
    char
    for char in HUMAN_READABLE_TO_PLAIN_TEXT.keys()
    if char != HUMAN_READABLE_CHAR_GAP
)
HUMAN_READABLE_ALPHABET = HUMAN_READABLE_CHARS.union(
    {HUMAN_READABLE_CHAR_GAP, HUMAN_READABLE_WORD_GAP}
)

PLAIN_TEXT_TO_BINARY = {
    '!': '1110101110101110111',
    '"': '101110101011101',
    '$': '10101011101010111',
    '&': '10111010101',
    '\'': '101110111011101',
    '(': '111010111011101',
    ')': '1110101110111010111',
    '+': '1011101011101',
    ',': '1110111010101110111',
    '-': '111010101010111',
    '.': '10111010111010111',
    '/': '1110101011101',
    '0': '1110111011101110111',
    '1': '10111011101110111',
    '2': '101011101110111',
    '3': '1010101110111',
    '4': '10101010111',
    '5': '101010101',
    '6': '11101010101',
    '7': '1110111010101',
    '8': '111011101110101',
    '9': '11101110111011101',
    ':': '11101110111010101',
    ';': '11101011101011101',
    '=': '1110101010111',
    '?': '101011101110101',
    '@': '10111011101011101',
    'A': '10111',
    'B': '111010101',
    'C': '11101011101',
    'D': '1110101',
    'E': '1',
    'F': '101011101',
    'G': '111011101',
    'H': '1010101',
    'I': '101',
    'J': '1011101110111',
    'K': '111010111',
    'L': '101110101',
    'M': '1110111',
    'N': '11101',
    'O': '11101110111',
    'P': '10111011101',
    'Q': '1110111010111',
    'R': '1011101',
    'S': '10101',
    'T': '111',
    'U': '1010111',
    'V': '101010111',
    'W': '101110111',
    'X': '11101010111',
    'Y': '1110101110111',
    'Z': '11101110101',
    '_': '10101110111010111',
}
BINARY_TO_PLAIN_TEXT = {v: k for k, v in PLAIN_TEXT_TO_BINARY.items()}
BINARY_CHARS = set(BINARY_TO_PLAIN_TEXT.keys())
BINARY_CHAR_GAP = '000'
BINARY_WORD_GAP = '0000000'
BINARY_ALPHABET = BINARY_CHARS.union({BINARY_CHAR_GAP, BINARY_WORD_GAP})


class Morse(object):

    @classmethod
    def from_plain_text(cls, value):
        if not isinstance(value, str):
            raise TypeError(
                'Value must be a string.  Given: {}'.format(type(value))
            )

        processed_value = value.strip().upper()
        distinct_characters = set(processed_value)

        problem_characters = distinct_characters.difference(
            PLAIN_TEXT_ALPHABET
        )
        if problem_characters:
            raise ValueError(
                'Characters given that cannot be Morse encoded: {}'
                .format(problem_characters)
            )

        words = [
            word
            for word in processed_value.split(PLAIN_TEXT_WORD_GAP)
        ]
        return cls(words)

    @classmethod
    def from_human_readable(cls, value):
        if not isinstance(value, str):
            raise TypeError(
                'Value must be a string.  Given: {}'.format(type(value))
            )

        words = value.split(HUMAN_READABLE_WORD_GAP)

        distinct_characters = set(
            itertools.chain(
                char
                for word in words
                for char in word.split(HUMAN_READABLE_CHAR_GAP)
                if char  # Filter empty strings
            )
        )
        problem_characters = (
            distinct_characters
            .difference(HUMAN_READABLE_CHARS)
            .difference(HUMAN_READABLE_CHAR_GAP)
        )
        if problem_characters:
            raise ValueError(
                'Characters given that are not '
                'human-readable Morse encoded: {problem_characters}\n'
                'Human-readable Morse characters look like {example}, the '
                'characters are separated by \'{char_sep}\', and the '
                'words are separated by \'{word_sep}\'.'
                .format(
                    problem_characters=', '.join(problem_characters),
                    example=PLAIN_TEXT_TO_HUMAN_READABLE["L"],
                    char_sep=HUMAN_READABLE_CHAR_GAP,
                    word_sep=HUMAN_READABLE_WORD_GAP,
                )
            )

        plain_text_words = [
            cls._human_readable_word_to_plain_text(word)
            for word in words
        ]
        return cls(plain_text_words)

    @classmethod
    def _human_readable_word_to_plain_text(cls, word):
        return PLAIN_TEXT_CHAR_GAP.join(
            HUMAN_READABLE_TO_PLAIN_TEXT[char]
            for char in word.split(HUMAN_READABLE_CHAR_GAP)
            if char  # Filter empty strings
        )

    @classmethod
    def from_binary(cls, value):
        if not isinstance(value, str):
            raise TypeError(
                'Value must be a string.  Given: {}'.format(type(value))
            )

        # Do we only have 0 and 1?
        distinct_values = set(value)
        problem_values = distinct_values.difference({"0", "1"})
        if problem_values:
            raise ValueError(
                'Values given that are not '
                'binary Morse encoded: {problem_values}\n'
                'Binary Morse characters look like {example}, the '
                'characters are separated by {char_sep}, and the '
                'words are separated by {word_sep}.'
                .format(
                    problem_values=', '.join(problem_values),
                    example=PLAIN_TEXT_TO_BINARY["L"],
                    char_sep=BINARY_CHAR_GAP,
                    word_sep=BINARY_WORD_GAP,
                )
            )

        # Do we have a valid sequence of 0 and 1?
        words = value.split(BINARY_WORD_GAP)
        distinct_characters = set(
            itertools.chain(
                char
                for word in words
                for char in word.split(BINARY_CHAR_GAP)
                if char  # Filter empty strings
            )
        )
        problem_characters = distinct_characters.difference(BINARY_CHARS)
        if problem_characters:
            raise ValueError(
                'Characters given that are not '
                'binary Morse encoded: {problem_characters}\n'
                'Binary Morse characters look like {example}, the '
                'characters are separated by {char_sep}, and the '
                'words are separated by {word_sep}.'
                .format(
                    problem_characters=', '.join(problem_characters),
                    example=PLAIN_TEXT_TO_BINARY["L"],
                    char_sep=BINARY_CHAR_GAP,
                    word_sep=BINARY_WORD_GAP,
                )
            )

        plain_text_words = [
            PLAIN_TEXT_WORD_GAP.join(
                cls._binary_word_to_plain_text(word)
                for word in words
            )
        ]
        return cls(plain_text_words)

    @classmethod
    def _binary_word_to_plain_text(cls, word):
        return PLAIN_TEXT_CHAR_GAP.join(
            BINARY_TO_PLAIN_TEXT[char]
            for char in word.split(BINARY_CHAR_GAP)
            if char  # Filter empty strings
        )

    def __init__(self, plain_text_words):
        self.plain_text_words = plain_text_words

    def __str__(self):
        return self.plain_text

    def __repr__(self):
        return '{class_name}(\'{plain_text_words}\')'.format(
            class_name=self.__class__.__name__,
            plain_text_words=self.plain_text_words,
        )

    @property
    def plain_text(self):
        return PLAIN_TEXT_WORD_GAP.join(self.plain_text_words)

    @property
    def human_readable(self):
        return HUMAN_READABLE_WORD_GAP.join(
            self._plain_text_word_to_human_readable(word)
            for word in self.plain_text_words
        )

    @classmethod
    def _plain_text_word_to_human_readable(cls, word):
        return HUMAN_READABLE_CHAR_GAP.join(
            PLAIN_TEXT_TO_HUMAN_READABLE[char]
            for char in word
        )

    @property
    def binary(self):
        return BINARY_WORD_GAP.join(
            self._plain_text_word_to_binary(word)
            for word in self.plain_text_words
        )

    @classmethod
    def _plain_text_word_to_binary(cls, word):
        return BINARY_CHAR_GAP.join(
            PLAIN_TEXT_TO_BINARY[char]
            for char in word
        )


if __name__ == "__main__":
    import argparse
    import sys

    PLAIN = 'PLAIN'
    HUMAN_READABLE = 'HUMAN_READABLE'
    BINARY = 'BINARY'
    CHOICES = [PLAIN, HUMAN_READABLE, BINARY]

    parser = argparse.ArgumentParser(
        description='Convert between plain text and Morse code. '
                    'Formats are {}'.format(CHOICES)
    )
    parser.add_argument(
        dest='from_format',
        metavar='from_format',
        action='store',
        default=None,
        type=str,
        choices=CHOICES,
        help='the format for input data')
    parser.add_argument(
        dest='to_format',
        metavar='to_format',
        action='store',
        default=None,
        type=str,
        choices=CHOICES,
        help='the format for output data')
    args = parser.parse_args()

    input_str = sys.stdin.read()

    morse = (
        Morse.from_plain_text(input_str)
        if args.from_format == PLAIN
        else Morse.from_human_readable(input_str)
        if args.from_format == HUMAN_READABLE
        else Morse.from_binary(input_str)
    )

    sys.stdout.write(
        morse.plain_text
        if args.to_format == PLAIN
        else morse.human_readable
        if args.to_format == HUMAN_READABLE
        else morse.binary
    )
