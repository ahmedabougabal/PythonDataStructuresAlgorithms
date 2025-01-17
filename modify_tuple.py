def insert_item(my_tuple, new_value, index):
    # Your code goes here
    my_list = list(my_tuple)
    my_list.insert(index, new_value)
    result = tuple(my_list)
    return result


# test cases 
sports = ('football', 'basketball', 'cricket', 'hockey', 'tennis', 'volleyball')
new_value1 = 'baseball'
index1 = 2

numbers = (7, 17, 13, 19, 5)
new_value2 = 11
index2 = 3

# result1 = Answer.insert_item(sports, new_value1, index1)
# result2 = Answer.insert_item(numbers, new_value2, index2)