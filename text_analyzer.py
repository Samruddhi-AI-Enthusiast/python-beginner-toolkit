print("===== TEXT ANALYZER =====")

text = input("Enter your text: ")

# Word count
words = text.split()
print("Word Count:", len(words))

# Character count
print("Character Count:", len(text))

# Vowel count
vowels = "aeiou"
vowel_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1

print("Vowel Count:", vowel_count)

# Sentence count
sentence_count = 0

for char in text:
    if char in ".!?":
        sentence_count += 1

print("Sentence Count:", sentence_count)