
# FILTER LIST
original_list = [1,2,3,4,5]

def filter_three(number):
    return (number) > 3

filtered = filter(filter_three, original_list)
print(list(filtered))

# another case

filtered_2 = [i  for i in original_list if i > 3]
print(filtered_2)

# MAP LIST

def square(number):
    return number**2

squares = list(map(square,original_list))
print(squares)

# another way

squares_2 = [number ** 2 for number in original_list]
print(squares)

#  ZIP

letters = ['a','b','c','d','e']

combined = list(zip(original_list,letters))
print(combined)

# Reversed

reversed_list = original_list[::-1]
print(reversed_list)

# Nested List
Nested_list = [[1,2,3],[4,5,6],[4,8,9]]

flat_list = [i for j in Nested_list for i in j]
print(flat_list)

# check Unique  
list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5]

def check_unique(li):
    if len(li) == len(set(li)):
        print('Unique')
    else: print('Not Unique')

check_unique(list1)
check_unique(list2)