import itertools
import pytest

from hypothesis import given, example
from hypothesis.strategies import (
    text,
    lists,
    data,
    sampled_from,
)

import sweetmorse.constants as c
from sweetmorse.morse import Morse


@pytest.mark.parametrize(
    "one,other,are_equal",
    (
        (
            Morse.from_plain_text("same text"),
            Morse.from_plain_text("same text"),
            True,
        ),
        (
            Morse.from_plain_text("same text"),
            Morse.from_human_readable("... ._ __ .   _ . _.._ _"),
            True,
        ),
        (
            Morse.from_plain_text("one text"),
            Morse.from_plain_text("two text"),
            False,
        ),
        (
            Morse.from_plain_text("one text"),
            None,
            False,
        ),
        (
            Morse.from_plain_text("one text"),
            object(),
            False,
        ),
    )
)
def test_equality(one, other, are_equal):
    assert (one == other) == are_equal
    assert (other == one) == are_equal


def test_repr_makes_object():
    """'...If at all possible, this should look like a valid Python expression
    that could be used to recreate an object with the same value...'
    https://docs.python.org/3.5/reference/datamodel.html#object.__repr__
    """
    m = Morse(["Hello,", "World!"])

    from_repr = eval(repr(m))

    assert from_repr == m


def test_sos_from_all_formats():
    assert Morse.from_plain_text("SOS").plain_text == "SOS"

    assert Morse.from_human_readable(
        "... ___ ..."
    ).plain_text == "SOS"

    assert Morse.from_binary(
        "101010001110111011100010101"
    ).plain_text == "SOS"


def test_sos_from_all_formats_with_newline():
    """Typical usage will terminate input with a newline.  Be ready!"""
    assert Morse.from_plain_text("SOS\n").plain_text == "SOS"

    assert Morse.from_human_readable(
        "... ___ ...\n"
    ).plain_text == "SOS"

    assert Morse.from_binary(
        "101010001110111011100010101\n"
    ).plain_text == "SOS"


@given(text(alphabet=list(c.PLAIN_TEXT_ALPHABET)))
@example('O  O')
def test_there_and_back_plain_text(value):
    print(value)
    morse = Morse.from_plain_text(value)

    morse_from_human_readable = Morse.from_human_readable(
        morse.human_readable
    )
    assert morse_from_human_readable.plain_text == value.strip().upper()

    morse_from_binary = Morse.from_binary(morse.binary)
    assert morse_from_binary.plain_text == value.strip().upper()


@given(data())
def test_there_and_back_human_readable(data):
    human_readable_chars = data.draw(
        lists(elements=sampled_from(list(c.HUMAN_READABLE_CHARS)))
    )
    separators = data.draw(
        lists(
            elements=sampled_from(
                (
                    c.HUMAN_READABLE_CHAR_GAP,
                    c.HUMAN_READABLE_WORD_GAP
                )
            ),
            min_size=max(len(human_readable_chars)-1, 0),
            max_size=max(len(human_readable_chars)-1, 0),
        )
    )
    value = ''.join(
        char
        for char in itertools.chain.from_iterable(
            itertools.zip_longest(
                human_readable_chars,
                separators,
                fillvalue=None
            )
        )
        if char is not None
    )
    print(value)

    morse = Morse.from_human_readable(value)

    morse_from_plain_text = Morse.from_plain_text(morse.plain_text)
    assert morse_from_plain_text.human_readable == value

    morse_from_binary = Morse.from_binary(morse.binary)
    assert morse_from_binary.human_readable == value


@given(data())
def test_there_and_back_binary(data):
    binary_chars = data.draw(
        lists(elements=sampled_from(list(c.BINARY_CHARS)))
    )
    separators = data.draw(
        lists(
            elements=sampled_from(
                (
                    c.BINARY_CHAR_GAP,
                    c.BINARY_WORD_GAP
                )
            ),
            min_size=max(len(binary_chars)-1, 0),
            max_size=max(len(binary_chars)-1, 0),
        )
    )
    value = ''.join(
        char
        for char in itertools.chain.from_iterable(
            itertools.zip_longest(
                binary_chars,
                separators,
                fillvalue=None
            )
        )
        if char is not None
    )
    print(value)

    morse = Morse.from_binary(value)

    morse_from_plain_text = Morse.from_plain_text(morse.plain_text)
    assert morse_from_plain_text.binary == value

    morse_from_human_readable = Morse.from_human_readable(
        morse.human_readable
    )
    assert morse_from_human_readable.binary == value


def test_parse_finds_correct_format():
    assert (
        Morse.parse("SOS") ==
        Morse.parse("... ___ ...") ==
        Morse.parse("101010001110111011100010101")
    )
