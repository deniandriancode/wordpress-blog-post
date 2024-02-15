def mode(l):
    count_dict = {}
    for i in l:
        count_dict[i] = 1 if count_dict.get(i) == None else count_dict[i] + 1
    max_count = max(count_dict.values())

    return [i for i, j in count_dict.items() if j == max_count]
