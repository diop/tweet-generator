import random
import sys
import os 

input_words = str(sys.argv[1:])

def randomize_words(input_words):
    # Custom shuffle implementation
    output_words = shuffle(input_words)
    return output_words

def shuffle_words(word_list):
    # output_words = input_words[:]
    shuffled_words = []
    list_length = len(word_list)

    for i in range(0, list_length):
        rand = random.randint(0, list_length - 1)
        shuffled_words.append(word_list.pop(rand))

    return shuffled_words

def main():
    print('')

if __name__ == '__main__':
    arguments = sys.argv[1:]
    main()

