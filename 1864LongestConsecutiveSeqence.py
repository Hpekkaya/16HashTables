def longest_consecutive_sequence(list1):
    # 1 Convert list to set to eliminate duplications
    num_set = set(list1)
    # 2 Initialize the max length
    max_len = 0
    # 3 Loop through the the each number
    for numb in num_set:
        # 31 Check the numb-1 is not in set
        if numb-1  not in num_set:
            # 311 Initialize Current Number and length
            current_numb, current_length = numb, 1
            # 312 Keep incrementing the curnumb until end of seq
            # while loop if cur num+1 in set (to find consecutive numbers)
            while current_numb + 1 in num_set:
                # 3121 Update (inc) current number and length
                current_numb += 1
                current_length += 1
            # 313 update the max length
            max_len = max(max_len, current_length)
    # 4 return max length
    return max_len


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )