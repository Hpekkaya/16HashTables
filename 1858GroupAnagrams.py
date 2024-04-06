
def group_anagrams(list1):
    # 1. Create empty dict
    my_dict = {}
    # 2. Create a loop to iterate over list
    for word in list1:
        # 21 Sort the each word
        sorted_word = "".join(sorted(word))
        # 22 Map the sorted words in dict
        #  Check the sorted in list
        if sorted_word in my_dict:
        # 221 if Yes append
            my_dict[sorted_word].append(word)
        # 222 else new list to the dict
        else:
            my_dict[sorted_word] = [word]


    # 3 Collect the groups in dict
    result = []
    for key in my_dict:
        result.append(my_dict[key])

    # 4 Return result
    return result

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )