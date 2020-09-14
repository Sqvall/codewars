""" https://www.codewars.com/kata/550498447451fbbd7600041c """

def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    array1 = [i ** 2 for i in array1]
    if sorted(array1) == sorted(array2):
        return True
    return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
(comp(a1, a2))
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
(comp(a1, a2))
