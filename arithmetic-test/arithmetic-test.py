import random


def level1(num):
    # for i in range(5):
    #     a = random.randint(2, 9)
    #     b = random.randint(2, 9)
    #     act_list = ['+', '-', '*']
    #     act = random.choice(act_list)
    #     print(f'{a} {act} {b}')
    #     t_answer = str(eval(f'{a}{act}{b}'))
    #     print(t_answer)
    global grade
    for i in range(num):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        act = random.choice(['-', '+', '*'])
        act_pr = f'{a} {act} {b}'
        t_answer = eval(act_pr)
        print(act_pr + ' = ?')
        try:
            answer = int(input('Pls, enter your answer here: '))
            num -= 1
        except ValueError:
            print('Incorrect format!')
            return level1(num)
        if t_answer == answer:
            print('Right!')
            grade += 1
        else:
            print('Wrong!')
    return grade
    # while True:
    #     print(t_answer)
    #     answer = input('Pls, enter your answer: ')
    #     if answer.isnumeric():
    #         if answer == t_answer:
    #             print('Right!')
    #             break
    #         elif answer != t_answer:
    #             print('Wrong!')
    #     else:
    #         print('try again')
    #         continue


def level2(num):
    global grade
    for i in range(num):
        a = random.randint(11, 29)
        t_answer = a ** 2
        print(f'{a}^2 ?')
        try:
            answer = int(input('Pls, enter your answer here: '))
            num -= 1
        except ValueError:
            print('Incorrect format!')
            return level2(num)
        if t_answer == answer:
            print('Right!')
            grade += 1
        else:
            print('Wrong!')
    return grade


def menu():
    global grade
    print('''What you want to do?
            go levels or exit?
            1-Level1
            2-Level2
            3-exit''')
    choose = input('Enter: 1, 2, 3>> ')
    if choose.isnumeric():
        if choose == '1':
            grade = 0
            print('welcome to level 1!')
            level1(5)
            print(f'Your mark is {grade}/5')
            chose_1 = input('Would you like to save your results? 1-yes, 2-no.: ')
            if chose_1.isnumeric():
                if chose_1 == '1':
                    name = str(input('Pls, enter your name: '))
                    with open('result.txt', 'a') as file:
                        file.write(f'{name} - RESULT: {grade}/5 LEVEL 1\n')
                        menu()
            else:
                menu()
        elif choose == '2':
            grade = 0
            print('welcome to level 2!')
            level2(5)
            print(f'Your mark is {grade}/5')
            chose_1 = input('Would you like to save your results? 1-yes, 2-no.: ')
            if chose_1.isnumeric():
                if chose_1 == '1':
                    name = str(input('Pls, enter your name: '))
                    with open('result.txt', 'a') as file:
                        file.write(f'{name} - RESULT {grade}/5 LEVEL 2\n')
            else:
                pass
        elif choose == '3':
            pass
    else:
        print('try again')
        menu()


menu()
