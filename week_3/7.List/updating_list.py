my_list = [45, 56, 44, 23, 99, 11, "Mew", True]
print(my_list)
print(id(my_list))

my_list[0] = 100
my_list[-1] = 100
print(my_list)
print(id(my_list))
