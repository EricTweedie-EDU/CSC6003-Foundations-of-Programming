# Program that analyzes a given sentence from the user
# Initially asking the user for a sentence containing 10 words

text = input('Enter a sentence that is at least 10 words long: ')

# Counting the number of words in the sentence, then displaying them
words = text.split(' ')
def word_count(words):
    for word in words:
        return len(words)

print(f'There are {word_count(words)} words in your sentence.')

# Counting how many vowels are in the sentence, then displaying them
count = 0
for vow in text:
    if vow.lower() in "aeiou":
        count += 1

print(f'There are {count} vowels in your sentence.')

# Creating a list of unique words, no duplicate words, then displaying them
unique = []
for x in words:
    if x not in unique:
        unique.append(x)

print(f'These are the unique words in your sentence: {unique}')

# Displaying the word(s) with the longest length
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f'The longest word in your sentence is: {longest_word}, which is {len(longest_word)} letters.')