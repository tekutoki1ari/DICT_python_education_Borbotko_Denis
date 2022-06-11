re_input = input('> ')
str_input = input('> ')

def compare(n, regular_expression, string):
    if len(regular_expression) > len(string):
        output = "False"
        return output
    elif regular_expression[n] == string[n]:
        output = "True"
    elif regular_expression[n] != string[n] and regular_expression[n] != ".":
        output = "False"
        return output
    elif regular_expression[n] == ".":
        output = "True"
    else:
        output = "False"
        return output

    if n+1 == len(regular_expression):
        return output
    else:
        return compare(n+1, regular_expression, string)


def new_func(b, r, s, copy_s):
    final_output = compare(0, r, s)
    if len(copy_s) == b-1:
        return final_output
    elif final_output == "False":
        new_s = copy_s[b:]
        return new_func(b+1, r, new_s, copy_s)
    else:
        return final_output


copy_str = str_input
True_or_False = new_func(1, re_input, str_input, copy_str)
print(f'Input: "{re_input}|{str_input}"   Output: {True_or_False}')
