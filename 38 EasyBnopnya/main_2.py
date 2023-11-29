import sys
from collections import defaultdict
codes = ['KOI8-R', 'CP1251', 'CP866', 'MACCYRILLIC', 'ISO-8859-5', 'CP855']

# test = test.encode('KOI8-R')
# with open('out.out', 'wb') as f_out:
#     f_out.write(test.decode('CP1251').encode('KOI8-R').decode('CP1251').encode('CP866').decode('CP855').encode('MACCYRILLIC'))


all_chars = '\n !"\'(),-.0123456789:;?ABCDEFHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'.encode('KOI8-R') 

all_comb = {all_chars}
all_dict = {all_chars: ()}
prev_it = {all_chars}
while True:
    new_it = set()
    new_dict = dict()
    for st in all_comb:
        for i in codes:
            for j in codes:
                try:
                    new_st = st.decode(i).encode(j)
                    new_it.add(new_st)
                    # print(st)
                    # print(all_dict[st])
                    new_dict[new_st] = all_dict[st] + (i, j)
                except UnicodeError:
                    pass
    if new_it <= all_comb:
        break
    prev_it = new_it - all_comb
    all_comb |= new_it
    all_dict.update(new_dict)



def my_encode(text, arr):
    for i in range(0, len(arr), 2):
        text = text.decode(arr[i]).encode(arr[i + 1])
    return text


data = sys.stdin.buffer.read()
for key in all_comb:
    if my_encode('Левин'.encode('KOI8-R'), all_dict[key]) in data:
        for i in range(len(all_dict[key]) - 1, -1, -2):
            data = data.decode(all_dict[key][i]).encode(all_dict[key][i - 1])
        print(data.decode('KOI8-R'))
        break



