def expanded_form(num,):
    count = len(str(num))
    r = []
    for i in str(num):
        r.append(i+'0'*(count-1))
        # count = count - 1
    print(r)


