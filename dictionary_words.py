import sys 

def process_words():
    with open('wolof_words.txt', 'r') as f:
        words_document = f.read().split()
    
    # new_word_list = words_document.split()
    print(words_document)
    
process_words()
