import re

file = open('file.txt', 'r')
words = {}
word = re.findall(r'a-zA-Z')
for word in file.read():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# with open('file.txt', 'r') as file:
#     words = {}
#     word = re.findall(r'a-zA-Z')
#     for word in file.read():
#         if word in words:
#             words[word] += 1
#         else:
#             words[word] = 1

print(words)
