user_word = input('Enter a word: ')
user_word = user_word.upper()
word_without_vowels = ''

for letters in user_word:
    if letters == 'A':
        continue
    elif letters == 'E':
        continue
    elif letters == 'I':
        continue
    elif letters == 'O':
        continue
    elif letters == 'U':
        continue
    else:
        word_without_vowels = word_without_vowels + letters
print(word_without_vowels.lower())