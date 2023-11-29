import sys
import zlib

data = sys.stdin.buffer.read()
flag_zlib = False
try:
    data = zlib.decompress(data)
    flag_zlib = True
except zlib.error:
    pass

if flag_zlib:
    if data[:4] == b'blob':
        ind = data.find(b'\x00')
        size = str(data[5:ind], encoding='utf-8')
        print(f"blob: {size}")
    elif data[:4] == b'tree':
        print("tree: ")
        splited = data.split(sep=b'\x00')[1:]
        new_data = []
        for i in range(len(splited)):
            if i % 2 == 0:
                new_data.append(splited[i])
            else:
                new_data.append(splited[i][:20])
                new_data.append(splited[i][20:])
        for i in range(0, len(new_data) - 1, 2):
            print(new_data[i + 1].hex(), new_data[i].decode('utf-8'))
    elif data[:6] == b'commit':
        print("commit:", data.split(sep=b'\x00')[1][5:45].decode('utf-8'))
    elif data[:3] == b'tag':
        name = data.split(sep=b'tag')[2][1:-1].decode('utf-8')
        print(f"tag: {name}")

    pass
else:
    if data[:4] == b'PACK':
        print(f"pack: {int.from_bytes(data[4:8], 'big')} {int.from_bytes(data[8:12], 'big')}")
    elif data[:4] == b'\xff\x74\x4f\x63':
        offset = 2*4 + 255*4
        print(f"index: {int.from_bytes(data[offset:offset + 4], 'big')}")
    else:
        print("unknown: ")
