import statistics
from math import floor

MSG_TO_DECODE = open("data/Exo3.txt").read()
MSG_ALPHABET = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
]
FRENCH_IC = 0.0778


def calc_coincidence_number(data: str) -> float:
    result = 0.0
    text_size = len(data)
    if text_size == 0:
        return result

    for char in MSG_ALPHABET:
        nb_char = data.count(char)
        result += nb_char * (nb_char - 1)

    result = result / (text_size * (text_size - 1))
    return result

def calc_subsequence_coincidence_number(data: str, k: int) -> float:
    results: list[float] = []
    text_size = len(data)
    text_sub_sequences_nb = floor(text_size / k)

    for i in range(text_sub_sequences_nb):
        txt = data[i * k : (i + 1) * k]
        results.append(calc_coincidence_number(txt))

    return statistics.mean(results)

def find_best_subsequence_coincidence_number(data: str) -> int:
    text_size = len(data)

    best_subsequence_k = 2
    best_subsequence_ic = calc_subsequence_coincidence_number(data, best_subsequence_k)

    for k in range(3, text_size + 1):
        ic = calc_subsequence_coincidence_number(data, k)
        if abs(ic - FRENCH_IC) < abs(best_subsequence_ic - FRENCH_IC):
            best_subsequence_ic = ic
            best_subsequence_k = k

    return best_subsequence_k


print(f"Coincidence number: {calc_coincidence_number(MSG_TO_DECODE):.4f}")
print(f"Best subsequence number: {find_best_subsequence_coincidence_number(MSG_TO_DECODE)}")