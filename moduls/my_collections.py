from collections import Counter

# Основною ідеєю Counter є те, що він призначений для підрахунку кількості входжень кожного елемента в колекції
s = 'bhgghbzxc'
words = ['pencil', 'phone', 'tech', 'buddy', 'phone']

print(Counter(s))  # ({'b': 2, 'h': 2, 'g': 2, 'z': 1, 'x': 1, 'c': 1})
print(type(Counter(s)))  # <class 'collections.Counter'>

counter_words_dict = (Counter(words))  # Counter({'phone': 2, 'pencil': 1, 'tech': 1, 'buddy': 1})
print(counter_words_dict['phone'])  # 2

for i in counter_words_dict.elements():
    print(i)  # pencil
              # phone
              # phone
              # tech
              # budyy    

print(counter_words_dict['phone'])

print(counter_words_dict.most_common())  # [('phone', 2), ('pencil', 1), ('tech', 1), ('buddy', 1)]
print(counter_words_dict.most_common(3))