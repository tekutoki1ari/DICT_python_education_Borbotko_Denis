print("Hello! My name is ssBot")
print("I was created in 2021")
name = str(input("Please, remind me ur name"))
print("What a great name u have,", name + '!')
print("Let me guess your age")
print("Enter remainders of divining your age by 3, 5 and 7")
a = int(input())
b = int(input())
c = int(input())
age = (a*70+b*21+c*15) % 105
print("Your age is " + str(age) + " that's a good time to start programming!"
print("Now I will prove to you that I can count to any number you want.")
num = int(input()) + 1
for i in range(num):
    print(i, end="!\n")
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("""
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
""")
def answers(n_answer):
    answer = int(input())
    if answer == 2:
        print("Congratulations, have a nice day!")
    else:
        print("Please, try again.")
        answers("1")
answers("2")
