# shorter and more concise version
def mode(l):
    count_dict = {x: l.count(x) for x in l}
    max_count = max(count_dict.values())
    return [i for i, j in count_dict.items() if j == max_count]

