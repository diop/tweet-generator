def anagram_easy(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    return sorted(str1) == sorted(str2)

print(anagram_easy('Clint Eastwood', 'old west action'))


def anagram_medium(str1, str2):
    if len (str1) != len(str2):
        return False

    count = {}

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            ccount[letter] = 1

    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True
            
print(anagram_medium('Clint Eastwood', 'Old West Action'))
