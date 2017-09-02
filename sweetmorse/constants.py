import string

# Formats
PLAIN = 'PLAIN'
HUMAN_READABLE = 'HUMAN_READABLE'
BINARY = 'BINARY'

# PLAIN
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
    ',': '__..__',
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

# HUMAN_READABLE
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

# BINARY
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
