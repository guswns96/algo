import sys
n= int(input())
nums = list(map(int, sys.stdin.readline().split()))
m= int(input())

if m <= 0:
    print(*nums)
else:
    for i in range(m):
        for j in range(n+1):
            if nums[j]<nums[j+1]:
                a=nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = a
                break
    print(*nums)

        