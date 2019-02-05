def sampler(words):
    word_list = words.split(' ')
    length = len(word_list)
    dictionary = {}

    for word in word_list:
        dictionary[word] = word_list.count(word)
    
    for key, value in dictionary.items():
        pairs = f'{key} = {value/length}'
        print(pairs)

if __name__ == '__main__':
    words = 'one fish two fish red fish blue fish'
    sampler(words)