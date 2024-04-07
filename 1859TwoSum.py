
def two_sum1(list1, target):
    # 1 Initialize dict (Hold index and value)
    twosum_dict = {}
    # 2 Loop through the list using enumerate func
    # Get both index and value of list
    for index, numb in enumerate(list1):
        # 21 Calculate the complement of target for each numb
        complement = target -numb
        # 22 Check the complement in Dict
        if complement in twosum_dict:
            # 221 If yes return the index of comp and current numb
            result = [twosum_dict[complement], index]
            return result
            # 222 Else Ad numb and its index to dic
        twosum_dict[index] = numb
    # Return empty list
    return []

def two_sum(list1, target):
    # 1 Initialize dict hold index an value
    my_dict = {}
    # 2 Loop through the list1 with enumerate func
    #   it holds both index and value of cuurent list
    for index, numb in enumerate(list1):
        # 21 Calculate the complement of target for each numb
        complement = target - numb
        # 22 Check the complement in dict
        if complement in my_dict:
            # 221 If yes return index of complement and number
            result = [my_dict[complement], index]
            return  result
            # 222 Add to dict numb and its index for future checks
        my_dict[numb] = index
    # return empty list
    return []


print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))