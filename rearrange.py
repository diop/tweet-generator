import random
import sys

def rearrange(input_words):
    input_words = []
    rearranged_words = []
    
    for word in input_words:
        if word != sys.argv[0]:
            input_words.append[word]
                                
    while len(input_words) > 0:
        random_index = random_randint(0, len(input_words) -1)
        rearranged_words.append(input_words.pop(random_index))
    
    return rearranged_words

def main():
    print(' '.join(rearrange(input_words=sys.argv[1:])))

if '__name__' == '__main__':
    main()