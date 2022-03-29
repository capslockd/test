my_list = ['p', 'r', 'o', 'b', 'e']

# first item
print(my_list[0])  # p

# third item
print(my_list[2])  # o

# fifth item
print(my_list[4])  # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[1])

print(n_list[0][1])

print(n_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[-1])

# List slicing in Python

my_list2 = ['p','r','o','g','r','a','m','i','z']

# elements from index 2 to index 4
print(my_list2[2:5])

# elements from index 5 to end
print(my_list2[5:])

# elements beginning to end
print(my_list2[:])


odd = [1, 3, 5]

odd.append([7, 8])

print(odd)

odd.extend([9, 11, 13])

print(odd)