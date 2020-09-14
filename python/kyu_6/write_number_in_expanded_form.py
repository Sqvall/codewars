""" https://www.codewars.com/kata/5842df8ccbd22792a4000245 """


def expanded_form(num):
    count = len(str(num))
    r = []
    for i in str(num):
        if int(i) > 0:
            r.append(i + '0' * (count - 1))
        count -= 1
    return " + ".join(r)
