segments = list(eval(input()))

segments.sort(key=lambda a: a[0])
# print(segments)

ans = 0
cur_beg = segments[0][0]
cur_end = segments[0][1]
for seg in segments[1:]:
    # print(cur_beg, cur_end)
    if cur_end < seg[0]:
        ans += cur_end - cur_beg
        cur_beg = seg[0]
        cur_end = seg[1]
    else:
        cur_end = max(seg[1], cur_end)

ans += cur_end - cur_beg
print(ans)
