cur_num = int(input())
cur_max = cur_num
cur_sum = cur_num


while cur_num != 0:
    cur_num = int(input())
    if cur_num == 0:
        break
    cur_sum = max(cur_sum + cur_num, cur_num)
    cur_max = max(cur_max, cur_sum)
    

print(cur_max)


    