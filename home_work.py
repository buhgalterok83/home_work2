lst = [4, 2, 1, 5, 2, 5, 7]

def second_largest_number(lst):
    if len(list(lst)) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in lst:
        if num >= largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None

print(second_largest_number(lst))