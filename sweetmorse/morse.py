import itertools
import sweetmorse.constants as c


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
            c.PLAIN_TEXT_ALPHABET
        )
        if problem_characters:
            raise ValueError(
                'Characters given that cannot be Morse encoded: {}'
                .format(problem_characters)
            )

        words = [
            word
            for word in processed_value.split(c.PLAIN_TEXT_WORD_GAP)
        ]
        return cls(words)

    @classmethod
    def from_human_readable(cls, value):
        if not isinstance(value, str):
            raise TypeError(
                'Value must be a string.  Given: {}'.format(type(value))
            )

        words = value.strip().split(c.HUMAN_READABLE_WORD_GAP)

        distinct_characters = set(
            itertools.chain(
                char
                for word in words
                for char in word.split(c.HUMAN_READABLE_CHAR_GAP)
                if char  # Filter empty strings
            )
        )
        problem_characters = (
            distinct_characters
            .difference(c.HUMAN_READABLE_CHARS)
            .difference(c.HUMAN_READABLE_CHAR_GAP)
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
                    example=c.PLAIN_TEXT_TO_HUMAN_READABLE["L"],
                    char_sep=c.HUMAN_READABLE_CHAR_GAP,
                    word_sep=c.HUMAN_READABLE_WORD_GAP,
                )
            )

        plain_text_words = [
            cls._human_readable_word_to_plain_text(word)
            for word in words
        ]
        return cls(plain_text_words)

    @classmethod
    def _human_readable_word_to_plain_text(cls, word):
        return c.PLAIN_TEXT_CHAR_GAP.join(
            c.HUMAN_READABLE_TO_PLAIN_TEXT[char]
            for char in word.split(c.HUMAN_READABLE_CHAR_GAP)
            if char  # Filter empty strings
        )

    @classmethod
    def from_binary(cls, value):
        if not isinstance(value, str):
            raise TypeError(
                'Value must be a string.  Given: {}'.format(type(value))
            )

        processed_value = value.strip()

        # Do we only have 0 and 1?
        distinct_values = set(processed_value)
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
                    example=c.PLAIN_TEXT_TO_BINARY["L"],
                    char_sep=c.BINARY_CHAR_GAP,
                    word_sep=c.BINARY_WORD_GAP,
                )
            )

        # Do we have a valid sequence of 0 and 1?
        words = processed_value.split(c.BINARY_WORD_GAP)
        distinct_characters = set(
            itertools.chain(
                char
                for word in words
                for char in word.split(c.BINARY_CHAR_GAP)
                if char  # Filter empty strings
            )
        )
        problem_characters = distinct_characters.difference(c.BINARY_CHARS)
        if problem_characters:
            raise ValueError(
                'Characters given that are not '
                'binary Morse encoded: {problem_characters}\n'
                'Binary Morse characters look like {example}, the '
                'characters are separated by {char_sep}, and the '
                'words are separated by {word_sep}.'
                .format(
                    problem_characters=', '.join(problem_characters),
                    example=c.PLAIN_TEXT_TO_BINARY["L"],
                    char_sep=c.BINARY_CHAR_GAP,
                    word_sep=c.BINARY_WORD_GAP,
                )
            )

        plain_text_words = [
            c.PLAIN_TEXT_WORD_GAP.join(
                cls._binary_word_to_plain_text(word)
                for word in words
            )
        ]
        return cls(plain_text_words)

    @classmethod
    def _binary_word_to_plain_text(cls, word):
        return c.PLAIN_TEXT_CHAR_GAP.join(
            c.BINARY_TO_PLAIN_TEXT[char]
            for char in word.split(c.BINARY_CHAR_GAP)
            if char  # Filter empty strings
        )

    def __init__(self, plain_text_words):
        self.plain_text_words = plain_text_words

    def __str__(self):
        return self.plain_text

    def __repr__(self):
        return '{class_name}({plain_text_words})'.format(
            class_name=self.__class__.__name__,
            plain_text_words=self.plain_text_words,
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return repr(self) == repr(other)
        else:
            return NotImplemented

    @property
    def plain_text(self):
        return c.PLAIN_TEXT_WORD_GAP.join(self.plain_text_words)

    @property
    def human_readable(self):
        return c.HUMAN_READABLE_WORD_GAP.join(
            self._plain_text_word_to_human_readable(word)
            for word in self.plain_text_words
        )

    @classmethod
    def _plain_text_word_to_human_readable(cls, word):
        return c.HUMAN_READABLE_CHAR_GAP.join(
            c.PLAIN_TEXT_TO_HUMAN_READABLE[char]
            for char in word
        )

    @property
    def binary(self):
        return c.BINARY_WORD_GAP.join(
            self._plain_text_word_to_binary(word)
            for word in self.plain_text_words
        )

    @classmethod
    def _plain_text_word_to_binary(cls, word):
        return c.BINARY_CHAR_GAP.join(
            c.PLAIN_TEXT_TO_BINARY[char]
            for char in word
        )
