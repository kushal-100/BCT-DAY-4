import copy
original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)
shallow_copy[2][0] = 99
print(original_list)  
print(shallow_copy)
