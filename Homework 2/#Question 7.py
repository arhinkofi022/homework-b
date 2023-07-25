#Question 7 

def is_vowel(char):
    char = char.lower()

    vowels = ['a', 'e', 'i', 'o', 'u']
    return char in vowels
print(is_vowel("f"))