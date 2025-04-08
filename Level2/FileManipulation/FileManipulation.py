import re
import os
print("Current Working Directory:", os.getcwd())


with open('text.txt', 'r') as file:
    content = file.read()

words = {}

word_list = re.findall(r'\b[a-zA-Z]+\b', content)

for word in word_list:
    word = word.lower()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(words)