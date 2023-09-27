s1 = input()
s2 = input()
shuffle = ["".join([s1[j::i] for j in range(i)]) for i in range(1, len(s1))]
if s2 in shuffle:
    print(shuffle.index(s2) + 1)
else:
    print("No")
