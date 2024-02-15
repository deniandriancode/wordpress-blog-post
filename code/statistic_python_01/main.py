############################################
###
### Author: Deni Andrian Prayoga
### Email: deniandriancode@gmail.com
###
############################################

# our function will return a list of modes
def mode(l):
    return []


# we return a dictionary for now, we will
# change it to return list later
def mode(l):
    count_dict = {}
    for i in l:
        count_dict[i] = 1 if count_dict.get(i) == None else count_dict[i] + 1

    return count_dict


def mode(l):
    count_dict = {}
    for i in l:
        count_dict[i] = 1 if count_dict.get(i) == None else count_dict[i] + 1
    max_count = max(count_dict.values())

    return [i for i, j in count_dict.items() if j == max_count]


# shorter and more concise version
def mode(l):
    count_dict = {x: l.count(x) for x in l}
    max_count = max(count_dict.values())
    return [i for i, j in count_dict.items() if j == max_count]
