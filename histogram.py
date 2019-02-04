# Handle reading and writing source text file to drive.
# use regular expression to remove number + period in fron of every text block.

import re

def histogram(source_text):
    '''
    A histogram() function which takes a source_text argument 
    (can be either a filename or the contents of the file as a string, your choice) 
    and return a histogram data structure that stores each unique word 
    along with the number of times the word appears in the source text.
    '''
    

def unique_words(histogram):
    '''
    A unique_words() function that takes a histogram argument and 
    returns the total count of unique words in the histogram. 
    For example, when given the histogram for The Adventures of Sherlock Holmes, 
    it returns the integer 8475.
    '''
    return len(histogram)

def frequency():
    '''
    A frequency() function that takes a word and histogram argument and 
    returns the number of times that word appears in a text. 
    For example, when given the word "mystery" and the Holmes histogram, 
    it will return the integer 20.
    '''

def clean_document(source_text):
    '''
    Cleanes the source text document.
    '''

def save_histogram_disk(filen_name, histogram):
    '''
    Takes a file name and a histogram then
    Writes a file to disk.
    '''

def main():
    with open(source_text, 'r') as f:
        words_document = f.read()

    cleaned_words = clean_document(words_document)
    new_histogram = generate_dict(cleaned_words)
    new_unique_words = unique_words(new_histogram)

    print(new_histogram)
    print(new_unique_words)

if __name__ = '__main__'
    main()
