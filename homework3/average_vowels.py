# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()
def counting_vowels_and_consonants(text):
	vowels = "aeiouAEIOU"
	vowel_count = 0
	consonant_count = 0
	for character in text:
		if character.isalpha():
			if character in vowels:
				vowel_count += 1
			else:
				consonant_count += 1
	return (vowel_count, consonant_count)
# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()
def average_vowels_and_consonants(paragraph):
	paragraph = paragraph.replace("!", ".").replace("?", ".")
	sentences = paragraph.split(".")
	total_vowels = 0
	total_consonants = 0
	for sentence in sentences:
		vowels, consonants = counting_vowels_and_consonants(sentence)
		total_vowels += vowels
		total_consonants += consonants
	number_of_sentences = len(sentences)
	average_vowels = total_vowels / number_of_sentences
	average_consonants = total_consonants / number_of_sentences
	return (number_of_sentences, average_vowels, average_consonants)
# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
number_of_sentences, average_vowels, average_consonants = average_vowels_and_consonants(paragraph)
print(f"average vowels per sentence: {average_vowels}")
print(f"average consonants per sentence: {average_consonants}")
