#1 Create a Python script that reads a text file and counts the frequency of each word in the file

file = open("assi1.txt", "r")

text = file.read()

file.close()

words = text.lower().split()

word_count = {}

for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(word, ":", count)

#2 Store the word frequencies in a dictionary.

file = open("assi1.txt", "r")

text = file.read()
file.close()

words = text.lower().split()

word_freq = {}

for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    word_freq[word] = word_freq.get(word, 0) + 1

print(word_freq)

#3 Print out the top 5 most common words and their frequencies.

file = open(".txt", "r")

text = file.read()
file.close()

words = text.lower().split()

# Store word frequencies in a dictionary
word_freq = {}

for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    word_freq[word] = word_freq.get(word, 0) + 1

sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

print("Top 5 most common words:")
for word, count in sorted_words[:5]:
    print(word, ":", count)
