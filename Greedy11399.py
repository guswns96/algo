import sys
n = int(input())
time_list = list(map(int, sys.stdin.readline().split()))
time_list.sort()
time_sum=0
for i in range(n):
    time_sum+=sum(time_list[0:i+1])
print(time_sum)
