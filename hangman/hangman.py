import random
print("The game will start soon")
print("guess the word")
list = ['python', 'java', 'php', 'javascript']
word = random.choice(list)
len_word = len(word[2:-1])
print(word[:3] + '-' * len_word)
print('ugadai')
answer = str(input())
if answer == word:
    print("u won")
else:
    print("u lose")
