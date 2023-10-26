def Remove_non_int_elements(lis):
    new_list = [x for x in lis if isinstance(x, int)]
    return new_list

lis = [1, 3, 'apple', 'banana', 'cherry', 4, [5, 4.6, 4+4j]]
print("before remove non int element from list our list is:",lis)

print("after remove non int element from list our list is:",Remove_non_int_elements(lis))

