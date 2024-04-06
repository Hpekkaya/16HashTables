def first_non_repeating_char(list1):
    # create empty dict
    my_dict = {}
    # create a loop put the char and repat amount
    for char in list1:
        my_dict[char] = my_dict.get(char, 0) + 1

    # for char, count in my_dict.items():
    #     if count == 1:
    #         return char
    for char in list1:
        if my_dict[char] == 1:
            return char

    return None







print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcce') )