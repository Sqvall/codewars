def sequence_sum(begin_number, end_number, step):
    print(sum(range(begin_number, end_number + 1, step)))
    return sum([i for i in range(begin_number, end_number + 1, step)])


print(sequence_sum(0, 6, 2))
