import sys
n, m, res = map(int, sys.stdin.readline().split())
maps_list = []
for _ in range(n): maps_list += map(int, sys.stdin.readline().split())
answer = 9999999999
floor = 0
min_h = min(maps_list)
max_h = max(maps_list)
_sum = sum(maps_list)

k={}
for t in maps_list:
    if t in k.keys():
        k[t]+=1
    else:
        k[t]=1
for i in range(min_h, max_h + 1):
    if _sum + res >= i * n * m:
        cur_time = 0
        for qwe in k:
            if qwe > i:
                cur_time += (qwe - i)*k[qwe]*2
            elif qwe < i:
                cur_time += (i - qwe)*k[qwe]
        if cur_time <= answer:
                answer = cur_time
                floor = i
print(answer,floor)