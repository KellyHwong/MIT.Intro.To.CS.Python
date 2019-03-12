import string

text = 'Did you see a purple     cow?'

text = text.lower()
# 去掉标点
# text = ''.join(c for c in text if c not in string.punctuation)
_ = lambda c : c if c not in string.punctuation else ' '
text = list(map(_, text))
text = ''.join(text)
# 去掉重复空格
text = text.split()
text = ' '.join(text)
print(text)

'''
phrase = "purple cow"
phrase_list = phrase.split()
text_list = text.split()
sub_slices = []
print(len(text_list))
print(len(phrase_list))
if len(text_list) > len(phrase_list):
    for i in range(len(text_list)-len(phrase_list)):
        print('aaaa')
        sub_slices.append(text_list[i:i+len(phrase_list)])
elif len(text_list) == len(phrase_list):
    return text_list == phrase_list
else:
    return False
# 如果一样长，上面就不跑了
print(phrase_list)
print(text_list)
print(sub_slices)
print(phrase_list in sub_slices)
# print(text_list[0:2])
'''
