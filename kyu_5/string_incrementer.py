""" https://www.codewars.com/kata/54a91a4883a7de5d7800009c """

def increment_string(strng):
    if not strng:
        return strng + '1'
    if not strng[-1].isdigit():
        strng += '1'
        return strng
    x = []
    for i in strng[::-1]:
        if not i.isdigit():
            break
        x.append(i)
    x = ''.join(x[::-1])
    y = strng.rstrip(x)
    x = str(int(x) + 1).rjust(len(x), '0')

    return y + x


print(increment_string("foo"))
print(increment_string("foobar00"))
print(increment_string("foobar99"))
print(increment_string("foobar099"))
print(increment_string(""))
print(increment_string("~H968583520=y0000000010"))
