# def reverse1(word):
#     return ' '.join(reversed(sentence.split())) 
# Second option

# def reverse2(word):
#     return ' '.join(sentence.split()[::-1])

def reverse_sentence(sentence):
    words = []
    length = len(words)
    spaces = [' ']
    
    index = 0
    
    while index < length:
        if sentence[index] not in spaces:
            word_start = index
            while index < length and sentence[index] not in spaces:
                index += 1
                
            words.append(sentence[word_start:index])
        
        index += 1
    
    return ' '.join(reversed(words))