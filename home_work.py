lst = []
def second_largest_number(lst):
    if len(lst) < 2 or all(elem == lst[0] for elem in lst):
        return None
    largest = float('-inf')
    for num in lst:
        if num > largest:
            largest = num
    second_largest = float('-inf')
    for num in lst:
        if num != largest and num > second_largest:
            second_largest = num
    if lst.count(largest) > 1 and second_largest != float('-inf'):
        return second_largest
    else:
        return largest if second_largest == float('-inf') else second_largest

print(second_largest_number(lst))
