def item_in_common(list1, list2):
    # create an empty dict
    dict1 = {}
    # create a for loop transfer list1 to dict
    for i in list1:
        dict1[i] = True
    # create a second for loop iterate over dict and check in list2
    for j in dict1:
        if j in list2:
            return True
    # Return False
    return False



list1 = [1,3,5]
list2 = [2,4,7]


print(item_in_common(list1, list2))


