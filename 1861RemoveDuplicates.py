def remove_duplicates(list1):
    list2 = list(set(list1))

    return list2




my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)