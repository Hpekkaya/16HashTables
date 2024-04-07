def has_unique_chars(string1):
    # 1 Initialize an empty set
    my_set = set()
    # 2 Loop through the string
    for char in string1:
        # 21 Check whether if char exists in string
        if char in my_set:
            # 211 If yes found duplicate return False
            return False
            # 212 else add to set
        my_set.add(char)
    # If loop comletes without finding return True
    return True

print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False