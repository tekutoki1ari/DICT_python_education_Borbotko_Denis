def compare(g, regular_expression, string):
    if len(regular_expression) > len(string):
        output = "False"
        return output
    elif regular_expression[g] == string[g]:
        output = "True"
    elif regular_expression[g] != string[g] and regular_expression[g] != ".":
        output = "False"
        return output
    elif regular_expression[g] == ".":
        output = "True"
    else:
        output = "False"
        return output

    if g + 1 == len(regular_expression):
        return output
    else:
        return compare(g + 1, regular_expression, string)


def without_caret_and_dollar(b, r, s, copy_s):
    final_output = compare(0, r, s)
    if len(copy_s) == b - 1:
        return final_output
    elif final_output == "False":
        new_s = copy_s[b:]
        return without_caret_and_dollar(b + 1, r, new_s, copy_s)
    else:
        return final_output


def check_meta(re_input, str_input, original_r):
    copy_re = re_input
    while "\\" in re_input:
        index_slash = copy_re.index("\\")
        slash = copy_re[index_slash]
        symbol_after_slash = copy_re[index_slash + 1]
        copy_re = copy_re.replace(f'{slash}{symbol_after_slash}', '░', 1)
        re_input = re_input.replace(f'{slash}', "", 1)
        if symbol_after_slash == slash:
            re_input = re_input.replace(f'{slash}', '▓', 1)
    re_input = re_input.replace('▓', '\\')
    if copy_re[0] == "^" and copy_re[-1] == "$":
        len_r = len(re_input[1:-1])
        if len(str_input) > len_r:
            true_or_false = "False"
        elif re_input[1:-1] == str_input[:len_r] and re_input[1:-1] == str_input[-len_r:]:
            true_or_false = "True"
        else:
            true_or_false = compare(0, re_input[1:-1], str_input)
    elif copy_re[0] == "^":
        len_r = len(re_input[1:])
        true_or_false = compare(0, re_input[1:], str_input[:len_r])
    elif copy_re[-1] == "$":
        len_r = len(re_input[:-1])
        true_or_false = compare(0, re_input[-len_r-1:-1], str_input[-len_r:])
    else:
        copy_str = str_input
        true_or_false = without_caret_and_dollar(1, re_input, str_input, copy_str)

    print(f'Input: "{original_r}|{str_input}"   Output: {true_or_false}')


def check_dot(r, r_copy, pr_ch, str_inp, m):
    print_r = r
    if pr_ch == ".":
        str_copy = str_inp.split(sep=" ")
        r_copy = r_copy.split(sep=" ")
        while m not in r_copy[0]:
            del r_copy[0]
        r_copy = r_copy[0]
        i = r_copy.index(m)
        part_of_str = r_copy[:len(r_copy[:(i - 1)])]
        part_of_str_2 = r_copy[i + 1:]
        while part_of_str not in str_copy[0] and part_of_str_2 not in str_copy[0]:
            del str_copy[0]
        str_copy = str_copy[0]
        str_copy = str_copy.replace(str_copy[:len(r_copy[:(i - 1)])], "")
        if len(r_copy[i + 1:]) != 0:
            str_copy = str_copy.replace(r_copy[i + 1:], "")
        if len(str_copy) == 0 and m == "?":
            r = r.replace(f'{pr_ch}{m}', "")
        elif len(str_copy) == 0 and m == "*":
            r = r.replace(f'{pr_ch}{m}', "")
        elif len(str_copy) == 0 and m == "+":
            r = r.replace(f'{m}', "")
        elif len(str_copy) > 1 and m == "?":
            r = r.replace(f'{m}', "")
        else:
            r = r.replace(f'{pr_ch}{m}', str_copy)
        return r, r_copy, print_r, 1
    elif pr_ch == "\\":
        r = r.replace(f'{pr_ch}', "")
        return r, r_copy, print_r, 1
    else:
        return r, r_copy, print_r, 0


def meta_question_mark(re, r_copy, st, p_ch, i):
    pr = re
    count_ch = st.count(p_ch)
    if count_ch == 0:
        re = re.replace(f'{p_ch}?', "")
    elif count_ch >= 1:
        st_copy = st.replace(st[:len(re[:i - 1])], "")

        if len(r_copy[i + 1:]) != 0 and r_copy[i + 1] == p_ch:
            st_copy = st_copy.replace(r_copy[i + 1:], "")
            new_c = st_copy.count(p_ch)
            if new_c == 0:
                new_c = 1
        else:
            new_c = 0
            for symbol in st_copy:
                if symbol == p_ch:
                    new_c += 1
                else:
                    break
        if new_c == 1:
            re = re.replace(f'{p_ch}?', p_ch * new_c)
        else:
            re = re.replace('?', "")
    check_meta(re, st, pr)


def meta_star_mark(re, r_copy, st, p_ch, i):
    pr = re
    count_ch = st.count(p_ch)
    if count_ch == 0:
        re = re.replace(f'{p_ch}*', "")
    elif count_ch >= 1:
        st_copy = st.replace(st[:len(re[:i - 1])], "")

        if len(r_copy[i + 1:]) != 0 and r_copy[i + 1] == p_ch:
            st_copy = st_copy.replace(r_copy[i + 1:], "")
            new_c = st_copy.count(p_ch)
            if new_c == 0:
                new_c = 1
        else:
            new_c = 0
            for symbol in st_copy:
                if symbol == p_ch:
                    new_c += 1
                else:
                    break

        re = re.replace(f'{p_ch}*', p_ch * new_c)
    check_meta(re, st, pr)


def meta_plus_sign(re, r_copy, st, p_ch, i):
    pr = re
    count_ch = st.count(p_ch)
    if count_ch >= 1:
        st_copy = st.replace(st[:len(re[:i - 1])], "")

        if len(r_copy[i + 1:]) != 0 and r_copy[i + 1] == p_ch:
            st_copy = st_copy.replace(r_copy[i + 1:], "")
            new_c = st_copy.count(p_ch)
            if new_c == 0:
                new_c = 1
        else:
            new_c = 0
            for symbol in st_copy:
                if symbol == p_ch:
                    new_c += 1
                else:
                    break

        re = re.replace(f'{p_ch}+', p_ch * new_c)
    else:
        re = re.replace('+', "")
    check_meta(re, st, pr)


regular = input('Input Regular Expression:\n> ')
sr = input('Input String:\n> ')
re_copy = regular
if re_copy[-1] == "$":
    re_copy = re_copy.replace(re_copy[-1], "")
if re_copy[0] == "^":
    re_copy = re_copy.replace(re_copy[0], "")

if "?" in re_copy:
    ind = re_copy.index("?")
    previous_character = re_copy[ind - 1]
    meta = "?"
    regular, re_copy, p_r, n = check_dot(regular, re_copy, previous_character, sr, meta)
    if n == 1:
        check_meta(regular, sr, p_r)
    elif n == 0:
        meta_question_mark(regular, re_copy, sr, previous_character, ind)
elif "*" in re_copy:
    ind = re_copy.index("*")
    previous_character = re_copy[ind - 1]
    meta = "*"
    regular, re_copy, p_r, n = check_dot(regular, re_copy, previous_character, sr, meta)
    if n == 1:
        check_meta(regular, sr, p_r)
    elif n == 0:
        meta_star_mark(regular, re_copy, sr, previous_character, ind)
elif "+" in re_copy:
    ind = re_copy.index("+")
    previous_character = re_copy[ind - 1]
    meta = "+"
    regular, re_copy, p_r, n = check_dot(regular, re_copy, previous_character, sr, meta)
    if n == 1:
        check_meta(regular, sr, p_r)
    elif n == 0:
        meta_plus_sign(regular, re_copy, sr, previous_character, ind)
else:
    p_r = regular
    check_meta(regular, sr, p_r)
