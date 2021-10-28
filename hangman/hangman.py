import random
print("""HANGMAN
The game will be available soon.""")
my_list = ["python", "java", "javascript", "php"]

def restart(replay):
    global start_game
    start_game = str(input("Enter y if you want to start the game, or n if not"))
    if start_game == 'y':
        start('')
    elif start_game == 'n':
        print('see you latter')
    else:
        print('Please, try again')
        restart('')

def start(message):
    global letter, tries, line
    name = random.choice(my_list)
    cut_word = list(name)
    line = len(cut_word)
    answer = ["-" for letter in cut_word]
    print('start game')
    tries = 8
    while True:
        if tries <=0:
            print('You lost')
            tries = 8
            restart('')
            break
        print(''.join(answer))
        print('Tries - ' + str(tries))
        letter = input('Write a letter:').strip('')
        line = len(letter)
        if letter.isalpha():
            if letter.islower():
                if line == 1:
                    if letter in cut_word:
                        for i, c in enumerate(cut_word):
                            if letter in answer[i]:
                                tries -= 1
                                print('You have already guessed this letter.')
                                continue
                            if letter == c:
                                answer[i] = letter
                            if '-' not in answer:
                                print('You word: ' + ' '.join(answer))
                                print('You won')
                                print('''Thanks for playing!  We'll see how well you did in the next stage''')

                                restart('')
                                break
                    elif letter not in cut_word:
                        tries -= 1
                        print('That letter does not appear in the word')
                        continue
                else:
                    print('You should input a single letter.')
            else:
                print('Please enter a lowercase English letter.')
        else:
            print('Please enter a lowercase English letter.')
start('')
