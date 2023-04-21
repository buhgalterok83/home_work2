def to_dict(lst):
    my_dict = {}
    for i in range(0, len(lst), 2):
        my_dict[lst[i]] = lst[i+1]
    return my_dict

lst = [1, 2, 3, 4, 5, 6, 7, 8]
my_dict = to_dict(lst)
print(my_dict)  # {1: 2, 3: 4}
