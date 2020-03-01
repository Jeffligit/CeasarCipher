def string_to_symbols(string):
    string = string.upper()
    string_list = []
    i = 0
    while i < len(string):
        string_list.append(ord(string[i]) - ord('A'))
        i += 1
    return string_list


def symbols_to_string(symbols):
    string = ''
    i = 0
    while i < len(symbols):
        string = string + chr(symbols[i] + ord('A'))
        i += 1
    return string


def shift(symbol, offset):
    if -1 < symbol < 26:
        return (symbol + offset) % 26
    else:
        return symbol


def unshift(symbol, offset):
    offset = 26 - offset
    return shift(symbol, offset)


def encrypt(message, key):
    message_value = string_to_symbols(message)
    encrypted_value = []
    for value in message_value:
        encrypted_value.append(shift(value, key))
    return symbols_to_string(encrypted_value)


def decrypt(cipher, key):
    encrypted_value = string_to_symbols(cipher)
    message_value = []
    for value in encrypted_value:
        message_value.append(unshift(value, key))
    return symbols_to_string(message_value)


def get_dictionary_frequencies(filename):
    frequency_list = []
    f = open(filename, 'r')
    for frequency in f:
        frequency_list.append(float(frequency))
    f.close()
    return frequency_list


def find_frequency(symbol):
    number_of_letters = 0
    frequency_list = [0] * 26
    for character in symbol:
        if -1 < character < 26:
            number_of_letters += 1
            frequency_list[character] += 1
    i = 0
    while i < len(frequency_list):
        frequency_list[i] = frequency_list[i] / number_of_letters
        i += 1
    return frequency_list


def scoring_frequency(freqs, english_freqs):
    i = 0
    score = 0
    while i < len(freqs):
        score = score + abs(english_freqs[i] - freqs[i])
        i += 1
    return score


def crack(filename, message):
    score_counter = []
    i = 0
    while i < 26:
        message_value = string_to_symbols(decrypt(message, i))
        score_counter.append(scoring_frequency(find_frequency(message_value), get_dictionary_frequencies(filename)))
        i += 1
    return decrypt(message, score_counter.index(min(score_counter)))


def main():
    word = ''
    f = open('encrypted_message.txt', 'r')
    for letters in f:
        word = word + letters
    f.close()
    print(crack('english.txt', word))
    return


main()