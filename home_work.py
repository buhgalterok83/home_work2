def second_largest_number(lst):
    if len(lst) < 2 or all(elem == lst[0] for elem in lst):
        return None
    largest = second_largest = float('-inf')
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else largest


lst1 = [4, 2, 1, 5, 2, 5, 7]
lst2 = [4, 4]
lst3 = [0, 0, 0]
lst4 = [4, 2, 1, 5, 2, 5, 7, 10, 10, 1]

print(second_largest_number(lst1))  # 5
print(second_largest_number(lst2))  # None
print(second_largest_number(lst3))  # None
print(second_largest_number(lst4))  # 7
