# 1. Reverse string
"""
text = 'Hello World'
print(text[::-1])

# Output
dlroW olleH

"""

# 2.Split string

"""
sentence = 'Hi, my name is Hai'
new_string = sentence.split()
print(new_string)

# Output 
['Hi,', 'my', 'name', 'is', 'Hai']

"""
# 3.Tạo một chuỗi đơn
"""
original = ['Hi,', 'my', 'name', 'is', 'Hai']
print(' '.join(original))

# Output
Hi, my name is Hai

----------------
original = ['My', 'name', 'is', 'Hai']
print('-'.join(original))

# Output
My-name-is-Hai

"""

# 4. Kiểm tra các chữ cái của 1 string có giống nhau (đảo chữ cái)
"""
from collections import Counter
Counter('bike') == Counter('ekbi')  # True
Counter('bike') == Counter('ekbj')  # False

"""

# 5. Format string
"""
def say_hello(name)
    print(f"Hello {name}"

say_hello('Hai')
say_hello('Tokuda')

# Output
Hello Hai
Hello Tokuda

"""
# 6. Hợp nhất các phần tử trong list
"""
import itertools
original = [[1, 2], [3, 4], [5, 6]]
handled = list(itertools.chain.from_iterable(a))
print(handled)

# Output
[1, 2, 3, 4, 5, 6]

"""

# 7. Reverse list
"""
original = ['a', 'b', 'd', 'e', '3']
# Cách 1 
original.reverse()

# Cách 2
original[::-1]

"""

# 8. Kết hợp 2 lists
"""
list_1 = ['a', 'b', 'c', 'd']
list_2 = ['e', 'f', 'g', 'h']

for x, y in zip(a, b):
    print(x, y)
    
# Output
a e
b f
c g
d h

"""

# 9. Negative Indexing List
"""
original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
original[-3:-1] 

Output
[8, 9]

"""
# 10. Phần tử lặp lại nhiều lần nhất trong list
"""
original = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(original), key = original.count))

# Output
4 

"""

# 11.  Unpack list

"""
one, two, three = ['Car', 'Bike', 'Plane']
print(one)
print(two)
print(three)

# Output
Car
Bike
Plane

"""
# 12. Phần tử trùng / khác nhau giữa 2 Sets
"""
set_a = {1,2,3}
set_b = {3,4,5}
intersect = set_a.intersection(set_b)
difference = set_a.difference(set_b)
print(intersect)
print(difference)

# Output
{3}
{1, 2}

"""
# 13. Tạo giá trị cho nhiều biến
"""
a = b = c = 'sample'
print(a, b, c)

# Output
sample sample sample

"""

# 14. So sánh theo chuỗi
"""
x = 10
5 < x < 15  # True
5 > x < 15  # False

"""