# Handle reading and writing source text file to drive.
# use regular expression to remove number + period in fron of every text block.

import re

def prune(source_text):
    '''
    Cleanes the source text document.
    '''
    removed_new_lines = source_text.replace('\n', '')
    removed_commas = removed_new_lines.replace(', ', ' ')
    removed_periods = removed_commas.replace('.', ' ')
    pruned_source_text = removed_periods.split(' ')

    for index in range(len(pruned_source_text)):
        word = pruned_source_text[index].lower()
        pruned_source_text[index] = word

    for word in pruned_source_text:
        if word == '':
            pruned_source_text.remove(word)

    return pruned_source_text
    
def histogram(source_text):
    '''
    A histogram() function which takes a source_text argument 
    (can be either a filename or the contents of the file as a string, your choice) 
    and return a histogram data structure that stores each unique word 
    along with the number of times the word appears in the source text.
    '''
    text_body = ''
    histogram = {}
    with open(source_text, 'r') as f:
        text_body = f.read()
    
    text_body = prune(text_body)

    for word in text_body:
        if word not in histogram:
            histogram[word] = 0
        histogram[word] += 1
    
    return histogram

def histogram_dictionary(source_text):
    text_body = ''
    with open(source_text, 'r') as f:
        text_body = f.read()
    
    text_body = prune(text_body)
    
    dictogram = {}
    for word in text_body:
        if word in dictogram:
            dictogram[word] += 1
        else:
            dictogram[word] = 1
    
    return dictogram

def unique_words(histogram):
    '''
    A unique_words() function that takes a histogram argument and 
    returns the total count of unique words in the histogram. 
    For example, when given the histogram for The Adventures of Sherlock Holmes, 
    it returns the integer 8475.
    '''
    # for key, value in histogram.items():
    #     if value == 1:
    #         count += 1
    return len(histogram)

def frequency(word, histogram):
    '''
    A frequency() function that takes a word and histogram argument and 
    returns the number of times that word appears in a text. 
    For example, when given the word "mystery" and the Holmes histogram, 
    it will return the integer 20.
    '''
    # for key, value in histogram.items():
    #     if word in key:
    #         return value
    return histogram[word]

def save_histogram_disk(file_name, histogram):
    '''
    Takes a file name and a histogram then
    Writes a file to disk.
    '''
    with open(file_name, w) as f:
        for word in histogram:
            f.write(word + ' ' + str(histogram[word]) + '\n')

if __name__ == '__main__':
    print(histogram_dictionary('african_proverbs.txt'))
