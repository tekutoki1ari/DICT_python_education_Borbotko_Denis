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


def without_caret_and_dollar(b, r, s, copy_s):
    final_output = compare(0, r, s)
    if len(copy_s) == b-1:
        return final_output
    elif final_output == "False":
        new_s = copy_s[b:]
        return without_caret_and_dollar(b + 1, r, new_s, copy_s)
    else:
        return final_output


re_input = input('> ')
str_input = input('> ')

if re_input[0] == "^" and re_input[-1] == "$":
    len_r = len(re_input[1:-1])
    if len(str_input) > len_r:
        True_or_False = "False"
    elif re_input[1:-1] == str_input[:len_r] and re_input[1:-1] == str_input[-len_r:]:
        True_or_False = "True"
    else:
        True_or_False = compare(0, re_input[1:-1], str_input)
elif re_input[0] == "^":
    len_r = len(re_input[1:])
    True_or_False = compare(0, re_input[1:], str_input[:len_r])
elif re_input[-1] == "$":
    len_r = len(re_input[:-1])
    True_or_False = compare(0, re_input[-len_r-1:-1], str_input[-len_r:])
else:
    copy_str = str_input
    True_or_False = without_caret_and_dollar(1, re_input, str_input, copy_str)

print(f'Input: "{re_input}|{str_input}"   Output: {True_or_False}')
