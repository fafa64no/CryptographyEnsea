

MSG_TO_DECODE = open("data/Exo3.txt").read()
MSG_ALPHABET = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
]

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

print(calc_coincidence_number(MSG_TO_DECODE))