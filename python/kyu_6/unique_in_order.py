""" https://www.codewars.com/kata/54e6533c92449cc251001667 """


def unique_in_order(iterable):
    result = list()
    for i in iterable:
        if len(result) == 0 or result[-1] != i:
            result.append(i)
    return result


print(unique_in_order('AAAABBBCCDAABBB'))  # ['A','B','C','D','A','B']
