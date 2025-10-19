# main.py
import string

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J -> I

def sanitize_key(key: str) -> str:
    return "".join([c for c in key.upper().replace("J","I") if c.isalpha()])

def generate_key_matrix(key: str):
    key = sanitize_key(key)
    matrix = []
    used = set()

    for ch in key:
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    for ch in ALPHABET:
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    char = char.upper()
    if char == 'J': char = 'I'
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    raise ValueError(f"Character '{char}' not found in key matrix")


def prepare_text(text: str, for_encrypt=True):
    """
    Normalize the text: uppercase, replace J->I, remove non-alpha.
    For encryption also split into digraphs and insert filler 'X' where needed.
    For decryption just make even-length (padding if required).
    """
    s = "".join([c for c in text.upper().replace("J","I") if c.isalpha()])

    if for_encrypt:
        digraphs = []
        i = 0
        while i < len(s):
            a = s[i]
            b = s[i+1] if i+1 < len(s) else ''
            if b == '':
                # last single char -> pad with X
                digraphs.append(a + 'X')
                i += 1
            elif a == b:
                # repeat letter pair -> insert X between
                digraphs.append(a + 'X')
                i += 1
            else:
                digraphs.append(a + b)
                i += 2
        return digraphs
    else:
        # for decrypt: ensure even length by padding with X if odd
        if len(s) % 2 != 0:
            s += 'X'
        return [s[i:i+2] for i in range(0, len(s), 2)]


def encrypt(text: str, key: str) -> str:
    matrix = generate_key_matrix(key)
    digraphs = prepare_text(text, for_encrypt=True)
    result = []

    for pair in digraphs:
        a, b = pair[0], pair[1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # same row -> shift right
            result.append(matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:  # same column -> shift down
            result.append(matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2])
        else:
            result.append(matrix[r1][c2] + matrix[r2][c1])

    return "".join(result)


def decrypt(text: str, key: str) -> str:
    matrix = generate_key_matrix(key)
    digraphs = prepare_text(text, for_encrypt=False)
    result = []

    for pair in digraphs:
        a, b = pair[0], pair[1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # same row -> shift left
            result.append(matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5])
        elif c1 == c2:  # same column -> shift up
            result.append(matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2])
        else:
            result.append(matrix[r1][c2] + matrix[r2][c1])

    return "".join(result)