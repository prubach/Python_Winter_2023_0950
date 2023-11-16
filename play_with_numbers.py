num_list = [2, 13, 9, 7, 11, 5, 18]

'''
TODO 
1. Print the subsequent 2nd powers of elements in the list
2. Sum the 2nd powers of elements of the list
'''
num_list_2nd_pow = [x*x for x in num_list]
print(num_list_2nd_pow)
num_list_2nd_pow_sorted = sorted(num_list_2nd_pow)
num_list_2nd_pow_sorted = sorted(num_list_2nd_pow, reverse=True)
print(num_list_2nd_pow_sorted)
#sum(num_list_2nd_pow)
print('------ set --------')
set_of_nums = set(num_list_2nd_pow_sorted)
print(set_of_nums)




