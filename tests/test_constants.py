import sweetmorse.constants as c


def test_no_accidental_hyphens():
    for char in c.HUMAN_READABLE_CHARS:
        assert '-' not in char
