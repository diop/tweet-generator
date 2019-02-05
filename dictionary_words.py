import sys
import random 

def get_dictionary_words():
    with open('twenty_thousand_words.txt', 'r') as f:
        dictionary_words = f.read()

    return dictionary_words.splitlines()

def create_random_sentence(dictionary, num_words):
    for _ in range(num_words):
        return ''.join(random.choice(dictionary))

def main():
    # https://github.com/DacioRomero/Metrogen/blob/b00c375a1f56d939253f44edfd694e19dfd4df29/Code/dictionary_words.py
    num_words = int(sys.argv[1])
    dictionary = get_dictionary_words()
    print(create_random_sentence(dictionary, num_words))

if __name__ == '__main__':
    main()