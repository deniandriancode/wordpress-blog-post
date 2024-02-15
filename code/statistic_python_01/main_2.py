# we return a dictionary for now, we will
# change it to return list later
def mode(l):
    count_dict = {}
    for i in l:
        count_dict[i] = 1 if count_dict.get(i) == None else count_dict[i] + 1

    return count_dict
