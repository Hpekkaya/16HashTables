def find_pairs(list1, list2, target):
    # 1 Initialize an empty list
    list_pairs = []
    # 2 Iterate over the list1
    for numb in list1:
        # 21 Calculate the complement
        complement = target - numb
        # 22 Check whether complement exists in list2
        if complement in list2:
            # 221 If yes append list_pairs
            list_pairs.append((complement,numb))
    # 3 return list_pairs
    return list_pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)