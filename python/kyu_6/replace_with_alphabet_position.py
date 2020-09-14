""" https://www.codewars.com/kata/546f922b54af40e1e90001da """

from string import ascii_lowercase


def alphabet_position(text):
    score = 1
    score_dict = {}
    for i in ascii_lowercase:
        score_dict[i] = score
        score += 1
    t = text.lower()
    out = ''
    for i in t:
        if i in score_dict:
            out += repr(score_dict[i]) + " "
    return out[0:-1]


print(alphabet_position("The sunset sets at twelve o' clock."))

# '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'
# '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'
