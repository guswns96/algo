import sys
import math
n= int(input())
nums = list(map(int, sys.stdin.readline().split()))
list = [i+1 for i in range(n)]
temp = []
if nums[0]==1:
    result = nums[1]-1
    for i in range(n):
        temp.append(list[result // math.factorial(n-1)])
        list.pop(result // math.factorial(n-1))
        result%= math.factorial(n-1)
        n-=1
    print(*temp)
elif nums[0]==2:
    total_sum=0
    for i in nums[1:]:
        for k,j in enumerate(list):
            if i == j:
                total_sum+=math.factorial(n-1)*k
                list.pop(k)
                n-=1
    print(total_sum+1)





