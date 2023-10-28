def linear_search_dictionary(dict, target):
    for key, value in dict.items():
        if value == target:
            print("Found at key " + key)
            return value

    print("Target is not in the dictionary")
    return -1


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
