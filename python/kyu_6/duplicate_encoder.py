""" https://www.codewars.com/kata/54b42f9314d9229fd6000d9c """


def duplicate_encode(word):
    word = word.lower()
    s = set(word)
    balance = [i for i in word if i not in s or s.remove(i)]
    result = [')' if i in balance else '(' for i in word]
    return ''.join(result)


assert duplicate_encode("din") == "((("
assert duplicate_encode("recede") == "()()()"
assert duplicate_encode("Success") == ")())())"
assert duplicate_encode("(( @") == "))(("
