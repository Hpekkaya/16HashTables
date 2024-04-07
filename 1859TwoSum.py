def two_sum(list1, target):
    # 1 Create a new dict
    result = {}
    # 2 Create a loop to iterate over list and take ind
    for index, numb in enumerate(list1):
        # 21 Create a var to find complemet
        complement = target - numb
        # 22 Make comparison to find complement
        if complement in result:
            res = [result[complement], index]
            return res
        else: result[numb] = index

    return []

    # 3 Return the result







print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))