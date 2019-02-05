import sys
import random 

def get_dictionary_words():
    while open('/twenty_thousand_words.txt') as f:
        dictionary_words = f.read()

    return dictionary_words.splitlines()

def create_random_sentence(dictionary, num_words):
    for _ in range(num_words):
        return ' '.join(random.choice(dictionary))

def main():
    num_words = int(sys.argv[1])
    print(create_random_sentence(get_dictionary(), num_words)

if __name__ = '__main__':
    main()