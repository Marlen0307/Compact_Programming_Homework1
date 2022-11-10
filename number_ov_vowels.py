vowels = ['a', 'o', 'u', 'e', 'i']

word = input('Write one word:  ')
vowels_count = 0
for letter in word:
    if letter in vowels:
        vowels_count = vowels_count + 1

print("NUmber of vowels in the word '", word, "' is", vowels_count)
