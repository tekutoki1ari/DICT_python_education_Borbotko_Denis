
regular_expression = input('> ')
string = input('> ')

if len(regular_expression) == len(string):
    output = "True"
    for i in range(len(regular_expression)):
        if regular_expression[i] == string[i]:
            output = "True"
        elif regular_expression[i] == ".":
            output = "True"
        else:
            output = "False"
else:
    output = "False"

print(f'"{regular_expression}|{string}"   Output: {output}')