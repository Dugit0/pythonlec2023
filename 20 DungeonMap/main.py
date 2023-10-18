from collections import defaultdict

dangeons = defaultdict(set)
while len(s := input().split()) == 2:
    if s[0] != s[1]:
        dangeons[s[0]].add(s[1])

begin = s[0]
end = input()

used = defaultdict(bool)
buf = {begin}

while buf:
    cur_dan = buf.pop()
    if cur_dan == end:
        print("YES")
        break
    for dan in dangeons[cur_dan]:
        if not used[dan]:
            buf.add(dan)
            used[dan] = True
else:
    print("NO")
