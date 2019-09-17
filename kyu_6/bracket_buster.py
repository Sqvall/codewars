""" https://www.codewars.com/kata/56ff322e79989cff16000e39 """

import re


def bracket_buster(string):
    if isinstance(string, str):
        result = re.findall(r'\[(.*?)\]', string)
        return result
    return "Take a seat on the bench."


print(bracket_buster("Don't [pass to Ramone]"))  # ["pass to Ramone"]
print(bracket_buster("Don't [test] [pass to Ramone]"))  # ['test', 'pass to Ramone']
print(bracket_buster(1337))  # Take a seat on the bench.
print(bracket_buster("[I'm] glad y'all [set it]] off"))  # ["I'm", 'set it']
