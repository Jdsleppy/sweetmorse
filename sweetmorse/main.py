#!/usr/bin/env python3
import sweetmorse.constants as c
from sweetmorse.morse import Morse


def main():
    import argparse
    import sys

    choices = [c.PLAIN, c.HUMAN_READABLE, c.BINARY]

    parser = argparse.ArgumentParser(
        description='Convert stdin between plain text and Morse code. '
                    'Formats are {}'.format(choices)
    )
    parser.add_argument(
        dest='from_format',
        metavar='from_format',
        action='store',
        default=None,
        type=str,
        choices=choices,
        help='the format for input data')
    parser.add_argument(
        dest='to_format',
        metavar='to_format',
        action='store',
        default=None,
        type=str,
        choices=choices,
        help='the format for output data')
    args = parser.parse_args()

    input_str = sys.stdin.read()

    morse = (
        Morse.from_plain_text(input_str)
        if args.from_format == c.PLAIN
        else Morse.from_human_readable(input_str)
        if args.from_format == c.HUMAN_READABLE
        else Morse.from_binary(input_str)
    )

    print(
        morse.plain_text
        if args.to_format == c.PLAIN
        else
        morse.human_readable
        if args.to_format == c.HUMAN_READABLE
        else
        morse.binary
    )


if __name__ == "__main__":
    main()
