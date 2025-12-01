import statistics

from exercise_3_data import *


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
    if k <= 0:
        return 0.0

    text_size = len(data)
    subseq_ics = []

    for start in range(k):
        subseq = data[start:text_size:k]
        if len(subseq) < 2:
            continue
        subseq_ics.append(calc_coincidence_number(subseq))

    if not subseq_ics:
        return 0.0
    return statistics.mean(subseq_ics)

def find_best_subsequence_coincidence_number(data: str, max_k: int = None) -> int:
    text_size = len(data)
    if text_size < 2:
        return 1

    if max_k is None:
        max_k = min(DEFAULT_MAX_KEY_SIZE, text_size)
    else:
        max_k = min(max_k, text_size)

    best_k = 1
    best_diff = abs(calc_subsequence_coincidence_number(data, best_k) - FRENCH_IC)

    for k in range(2, max_k + 1):
        ic = calc_subsequence_coincidence_number(data, k)
        diff = abs(ic - FRENCH_IC)
        if diff < best_diff:
            best_diff = diff
            best_k = k

    return best_k

def find_character_frequencies(data: str, k: int, key_pos: int) -> dict:
    results = {}
    text_size = len(data)
    nb_chars = 0.0

    for char in MSG_ALPHABET:
        results[char] = 0.0

    for i in range(key_pos, text_size, k):
        char = data[i]
        results[char] += 1.0
        nb_chars += 1.0

    for char in MSG_ALPHABET:
        results[char] /= nb_chars

    return results

def get_most_probable_key(data: str) -> str:
    probable_key_size = find_best_subsequence_coincidence_number(MSG_TO_DECODE)
    probable_key = ""

    for i in range(probable_key_size):
        obs_freq: dict = find_character_frequencies(data, probable_key_size, i)

        best_shift = 0
        best_score = -1.0

        for s in range(len(MSG_ALPHABET)):
            score = 0.0
            for c in MSG_ALPHABET:
                c_idx = MSG_ALPHABET.index(c)
                dec_idx = (c_idx - s) % len(MSG_ALPHABET)
                dec_char = MSG_ALPHABET[dec_idx]
                score += obs_freq.get(c, 0.0) * FRENCH_FREQUENCIES.get(dec_char, 0.0)

            if score > best_score:
                best_score = score
                best_shift = s

        probable_key += MSG_ALPHABET[best_shift]

    return probable_key

def decrypt_message(ciphered_text: str, key: str) -> str:
    plaintext_chars = []
    key_len = len(key)

    for i, c in enumerate(ciphered_text):
        c_idx = MSG_ALPHABET_INDEX[c]
        k_idx = MSG_ALPHABET_INDEX[key[i % key_len]]
        p_idx = (c_idx - k_idx) % len(MSG_ALPHABET)
        plaintext_chars.append(MSG_ALPHABET[p_idx])

    return "".join(plaintext_chars)


print(f"MSG_TO_DECODE: {MSG_TO_DECODE}")
print(f"Coincidence number: {calc_coincidence_number(MSG_TO_DECODE):.4f}")
print(f"Best subsequence number: {find_best_subsequence_coincidence_number(MSG_TO_DECODE)}")
print(f"Most likely key: {get_most_probable_key(MSG_TO_DECODE)}")
print(f"Most likely message is:\n{decrypt_message(MSG_TO_DECODE, get_most_probable_key(MSG_TO_DECODE))}")