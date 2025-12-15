from collections import defaultdict, Counter
import itertools

from exercise_3_data import *


def find_repeated_sequences_spacings(text: str, seq_len: int = 3) -> dict:
    occurrences = defaultdict(list)
    text_len = len(text)
    for i in range(text_len - seq_len + 1):
        seq = text[i:i+seq_len]
        occurrences[seq].append(i)

    seq_spacings = {}
    for seq, positions in occurrences.items():
        if len(positions) > 1:
            spacings = []
            for a, b in itertools.combinations(positions, 2):
                spacings.append(b - a)
            if spacings:
                seq_spacings[seq] = spacings

    return seq_spacings


def all_divisors(n: int, min_div: int = 2, max_div: int = None) -> list:
    if n <= 1:
        return []

    max_test = int(n**0.5) + 1
    divs = set()
    for d in range(1, max_test):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)

    if max_div is None:
        result = sorted([d for d in divs if d >= min_div])
    else:
        result = sorted([d for d in divs if min_div <= d <= max_div])

    return result


def kasiski_candidate_key_lengths(text: str, min_seq_len: int, max_seq_len: int, max_key_len: int) -> list:
    candidate_counts = Counter()

    for seq_len in range(min_seq_len, max_seq_len + 1):
        seq_spacings = find_repeated_sequences_spacings(text, seq_len)
        for seq, spacings in seq_spacings.items():
            for dist in spacings:
                divs = all_divisors(dist, min_div=max(2, min_seq_len), max_div=max_key_len)
                candidate_counts.update(divs)

    return candidate_counts.most_common()


def derive_key_by_correlation(ciphertext: str, key_len: int) -> str:
    french_prop = {ch: FRENCH_FREQUENCIES.get(ch, 0.0) / 100.0 for ch in MSG_ALPHABET}
    alpha_index = {ch: i for i, ch in enumerate(MSG_ALPHABET)}
    m = len(MSG_ALPHABET)
    key_chars = []

    for pos in range(key_len):
        col = []
        for i in range(pos, len(ciphertext), key_len):
            col.append(ciphertext[i])
        if not col:
            key_chars.append('A')
            continue

        col_count = Counter(col)
        col_total = sum(col_count.values())
        obs_freq = {ch: (col_count.get(ch, 0) / col_total) for ch in MSG_ALPHABET}

        best_shift = 0
        best_score = -1.0
        for s in range(m):
            score = 0.0
            for c in MSG_ALPHABET:
                c_idx = alpha_index[c]
                dec_idx = (c_idx - s) % m
                dec_char = MSG_ALPHABET[dec_idx]
                score += obs_freq[c] * french_prop.get(dec_char, 0.0)
            if score > best_score:
                best_score = score
                best_shift = s

        key_chars.append(MSG_ALPHABET[best_shift])

    return "".join(key_chars)


def kasiski_and_attempts(
    ciphertext: str,
    min_seq_len: int = 3,
    max_seq_len: int = 5,
    min_key_len: int = 5,
    max_key_len: int = 10,
    top_n: int = 5
) -> list:
    candidate_counts = kasiski_candidate_key_lengths(ciphertext, min_seq_len, max_seq_len, max_key_len)
    if not candidate_counts:
        return []

    candidates = [k for k, cnt in candidate_counts if min_key_len <= k <= max_key_len][:top_n]
    results = []

    for k in candidates:
        derived_key = derive_key_by_correlation(ciphertext, k)

        results.append(derived_key)
    return results


decypher_attempts = kasiski_and_attempts(
    MSG_TO_DECODE
)
print(decypher_attempts)
