""" https://www.codewars.com/kata/584c3e45710dca21be000088 """


def find_longest(st):
    my_list = []
    count = 0
    for i in st:
        if i == '(':
            my_list.append(i)
        elif i == ')':
            if my_list and my_list[-1] == '(':
                count += 2
                my_list.pop()
            else:
                my_list.append(i)
    return print(count)


find_longest("()")  # 2
find_longest(")()")  # 2
find_longest("()()")  # 4
find_longest("()()(")  # 4
find_longest("(()())")  # 6
find_longest("(()(())")  # 6
find_longest("())(()))")  # 4
