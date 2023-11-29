import sys
from collections import defaultdict
codes = ['KOI8-R', 'CP1251', 'CP866', 'MACCYRILLIC', 'ISO-8859-5', 'CP855']

# with open('text.txt') as f_inp:
#     test = f_inp.read()
# print(test)
# test = test.encode('KOI8-R')
# with open('out.out', 'wb') as f_out:
#     f_out.write(test.decode('CP1251').encode('KOI8-R').decode('CP1251').encode('CP866').decode('CP855').encode('MACCYRILLIC'))

def long_decoding(text, arr):
    for i in range(len(arr) - 1, -1, 2):
        text = text.decode(arr[i]).encode(arr[i + 1])
    return text

data = sys.stdin.buffer.read()
buf = set()
buf.add('Левин'.encode('KOI8-R'))
used = defaultdict(bool)
code_path = {'Левин'.encode('KOI8-R'): ()}
# data = data.decode('KOI8-R')

while len(buf) != 0:
    print(len(used))
    cur_text = buf.pop()
    if cur_text in data:
        cur_code = code_path[cur_text]
        print(long_decoding(data, cur_code).decode('KOI8-R'))
        break
    if not used[cur_text]:
        used[cur_text] = True
        cur_code = code_path[cur_text]
        for i in codes:
            for j in codes:
                try:
                    new_text = cur_text.decode(i).encode(j)
                except UnicodeError:
                    continue
                if not used[new_text]:
                    buf.add(new_text)
                    code_path[new_text] = cur_code + (i, j)

# print(data.decode('MACCYRILLIC').encode('CP855').decode('CP866').encode('CP1251').decode('KOI8-R').encode('CP1251').decode('KOI8-R'))



