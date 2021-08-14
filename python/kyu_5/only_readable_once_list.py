""" https://www.codewars.com/kata/53f17f5b59c3fcd589000390 """


class SecureList:
    def __init__(self, lst: list):
        self.lst = lst[:]

    def __getitem__(self, item):
        return self.lst.pop(item)

    def __len__(self):
        return len(self.lst)

    def __repr__(self):
        result = str(self.lst)
        self.lst.clear()
        return result

    def __str__(self):
        return self.__repr__()


base = [1, 2, 3, 4]
a = SecureList(base)

assert a[0] == base[0], "List returned wrong value."
assert a[0] == base[1], "List returned wrong value."
assert len(a) == 2, "List hasn't deleted it's items once accessed"
print("current List: %s" % a)
assert len(a) == 0, "List Should be empty after printing"
a = SecureList(base)
print("current List: %r" % a)
assert len(a) == 0, "List Should be empty after printing a representation"
