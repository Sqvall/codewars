def same_structure_as(original, other):
    check = []
    if type(original) == type(other):
        for i, j in zip(original, other):
            if type(i) == type(j):
                if type(i) is list and type(j) is list:
                    if len(i) == len(j) and not None:
                        for q, w in zip(i, j):
                            if type(q) == type(w):
                                check.append(1)
                            else:
                                check.append(0)
                    else:
                        check.append(0)
                check.append(1)
            else:
                check.append(0)
        for i in check:
            if i == 0:
                return False
    else:
        return False
    return True


assert same_structure_as([1, [1, 1]], [2, [2, 2]]) is True
assert same_structure_as([1, [1, 1]], [[2, 2], 2]) is False
assert same_structure_as([1, [1, 1]], [2, [2]]) is False
assert same_structure_as([], 1)
