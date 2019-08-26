""" https://www.codewars.com/kata/57eb8fcdf670e99d9b000272 """


import string


def high(word_string):
    _count = 1
    _score_dic = {}
    score_string = {}
    for i in string.ascii_lowercase:
        _score_dic[i] = _count
        _count += 1
    for word in word_string.lower().split():
        score_count = 0
        for i in word:
            score_count += _score_dic[i]
        score_string[word] = score_count

    x = [k for k, v in score_string.items() if score_string[k] == max(score_string.values())]

    return x[0]


print(high('man i need a taxi up to ubud'))
# test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
# test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
# test.assert_equals(high('take me to semynak'), 'semynak')
