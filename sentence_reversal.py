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
    
    # Implement reversed instead of using standard library
    return ' '.join(reversed(words))
            