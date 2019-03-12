import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
'''
lis1 = [0, 1, 2, 3]
lis2 = [4, 5, 6, 7]

test1 = zip(lis1, lis2)
# print(test1)
d = dict()
for k,v in test1:
    d[k] = v
print(d)
'''
lower_list = list(string.ascii_lowercase)
# print(lower_list)
# list(range(1, 26+1))

z = zip(lower_list, list(range(1, 26+1)))
d = dict()
for k,v in z:
    d[k] = v
print(d)
rev_d = {v:k for k,v in d.items()}
# shift字母编号
shift = 2

'''
# 约束在[1, 26]
if result > 26:
    while result > 26:
        result -= 26
if result < 1:
    while result < 1:
        result += 26
'''
word = "apple"
new_word = []
for letter in word:
    index = d[letter] # 索引值
    index += shift# 索引值加shift，加密
    if index > 26:
        while index > 26:
            index -= 26
    if index < 1:
        while index < 1:
            index += 26
    new_letter = rev_d[index]# 反查，变成密文
    new_word.append(new_letter)
    # str化
new_word = ''.join(c for c in new_word)
print(new_word)

index = d[letter] # 索引值
index += shift# 索引值加shift，加密
if index > 26:
    while index > 26:
        index -= 26
if index < 1:
    while index < 1:
        index += 26
new_letter = rev_d[index]# 反查，变成密文

