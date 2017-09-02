import itertools

from hypothesis import given, example
from hypothesis.strategies import (
    text,
    lists,
    data,
    sampled_from,
)

import sweetmorse.sweetmorse as sm


def test_sos_from_all_formats():
    assert sm.Morse.from_plain_text("SOS").plain_text == "SOS"

    assert sm.Morse.from_human_readable(
        "... ___ ..."
    ).plain_text == "SOS"

    assert sm.Morse.from_binary(
        "101010001110111011100010101"
    ).plain_text == "SOS"


@given(text(alphabet=sm.PLAIN_TEXT_ALPHABET))
@example('O  O')
def test_there_and_back_plain_text(value):
    print(value)
    morse = sm.Morse.from_plain_text(value)

    morse_from_human_readable = sm.Morse.from_human_readable(
        morse.human_readable
    )
    assert morse_from_human_readable.plain_text == value.strip().upper()

    morse_from_binary = sm.Morse.from_binary(morse.binary)
    assert morse_from_binary.plain_text == value.strip().upper()


@given(data())
def test_there_and_back_human_readable(data):
    human_readable_chars = data.draw(
        lists(elements=sampled_from(sm.HUMAN_READABLE_CHARS))
    )
    separators = data.draw(
        lists(
            elements=sampled_from(
                (
                    sm.HUMAN_READABLE_CHAR_GAP,
                    sm.HUMAN_READABLE_WORD_GAP
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

    morse = sm.Morse.from_human_readable(value)

    morse_from_plain_text = sm.Morse.from_plain_text(morse.plain_text)
    assert morse_from_plain_text.human_readable == value

    morse_from_binary = sm.Morse.from_binary(morse.binary)
    assert morse_from_binary.human_readable == value


@given(data())
def test_there_and_back_binary(data):
    binary_chars = data.draw(
        lists(elements=sampled_from(sm.BINARY_CHARS))
    )
    separators = data.draw(
        lists(
            elements=sampled_from(
                (
                    sm.BINARY_CHAR_GAP,
                    sm.BINARY_WORD_GAP
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

    morse = sm.Morse.from_binary(value)

    morse_from_plain_text = sm.Morse.from_plain_text(morse.plain_text)
    assert morse_from_plain_text.binary == value

    morse_from_human_readable = sm.Morse.from_human_readable(
        morse.human_readable
    )
    assert morse_from_human_readable.binary == value
