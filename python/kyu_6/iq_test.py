""" https://www.codewars.com/kata/552c028c030765286c00007d """


def iq_test(numbers):
    d = {'Even': {}, 'Odd': {}}
    count = 1
    for i in numbers.split():
        if int(i) % 2:
            d['Even'][count] = int(i)
            count += 1
        else:
            d['Odd'][count] = int(i)
            count += 1
    print(d)
    if len(d['Even']) < len(d['Odd']):
        return list(d['Even'].keys())[0]
    return list(d['Odd'].keys())[0]


print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 2"))
print(iq_test("41 5 51 29 5 19 19 5 39 1 35 23 21 33 1 35 41 25 19 25 49 33 41 37 35 23 11 9 36 31 51 43 33"))
