#  Toan tu ba  ngooi

""""
def condition_True(condition):
    if condition:
        return True
    else:
        return False
"""
    # rut gon
"""    def condition_True_1(condition):
        return True if condition else False

"""
# 2 if ... in
"""verhicles = ['bike','car','motobike','bus','train','boat']
verhicle = 'bike'
if verhicle in verhicles:
    print('Matched')
"""
# hoac
"""print('Matched') if verhicle in verhicles"""


# dieu kien nguoc 
"""if condition:
    <statements>
else:
    break

=> """
"""if not Condition:
    break
<statement>"""

# Kiem tra empty

"""
if len(list) > 0:
    <statements>
    
hay là:
if list != []:
    <statements>

"""

# thay vao do chi can down gian
"""
if list:
    <statements>

"""

# -------------
# List Comprehension

"""
list_numbers = []
for i in range(5):
    list_numbers.append(i)

"""
# thay the
"""
list_numbers = [i for i in range(5)]

# co dieu kien
list_number_even = [i for i in range(5) if i % 2 == 0]

"""

# -----------------
# any() va all()

# any() được sử dụng khi chỉ cần một thỏa mãn điều kiện:
"""
for i in list_numbers:
    if i > 0 and i < 10:
        return True

"""

"""
# dung any()

list_numbers = [0, 5, 15]
any(i > 0 and i < 10 for i in list_numbers)

# True
Lí do kết quả ra True bởi vì đã có 5 thỏa mãn điều kiện
"""
# all()
"""all() thì hoạt động ngược lại với any(). 
Kết quả trả về True khi và chỉ khi tất cả các phần tử thỏa mãn điều kiện được đưa ra:"""

"""
list_numbers = [0, 5, 15]
all(i > 0 and i < 10 for i in list_numbers)

# False
0 và 15 không thỏa mãn điều kiện nên hàm all() trả về False .
"""

# ------------------------
# Merge hai hay nhiều lists

"""
Ta có list_a = [1,2,3] và list_b = [4,5,6] Để không phải xử lý cồng kềnh như:
for i in list_b:
    list_a.append(i)

"""

"""
# thay the
list = list_a + list_b


"""

# -----------------------------
# Hoán đổi giá trị của hai biến không sử dụng biến trung gian

"""
. Giả sử ta có a = 4, b = 5

code:

a = a + b # a = 9
b = a - b # b = 4
a = a - b # a = 5

"""
"""
# Thay the

a, b = b, a

"""

# ---------------------
# Lấy giá trị của dict dựa vào key

"""
Chúng ta vẫn có thói quen lấy giá trị trong dict dựa vào key như:

var = dict['key']
=>Nhưng trong dict của chúng ta không tồn tại key đó thì sẽ bị tạch luôn ở case này
"""

"""
# thay the
var = dict.get('key')
=> Trong trường hợp không tồn tại key đó cũng ko sao var của chúng ta không có bất kỳ giá trị nào cả.
"""