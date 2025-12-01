MSG_TO_DECODE = open("data/Exo3.txt").read().replace(" ", "").replace("\n", "")
MSG_ALPHABET = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
]
MSG_ALPHABET_INDEX = {ch: i for i, ch in enumerate(MSG_ALPHABET)}

DEFAULT_MAX_KEY_SIZE = 20
FRENCH_IC = 0.0778
FRENCH_PERCENTAGES = {
    "E": 15.87, "A": 9.42, "I": 8.41, "S": 7.90, "N": 7.15, "T": 7.26,
    "R": 6.46, "U": 6.24, "L": 5.34, "O": 5.14,
    "D": 3.39, "M": 3.24, "P": 2.86, "C": 2.64, "V": 2.15,
    "Q": 1.06, "G": 1.04, "B": 1.02, "F": 0.95, "J": 0.89,
    "H": 0.77, "Z": 0.32, "X": 0.30, "Y": 0.24,
    "K": 0.0, "W": 0.0
}
FRENCH_FREQUENCIES = {ch: FRENCH_PERCENTAGES.get(ch, 0.0) / 100.0 for ch in MSG_ALPHABET}