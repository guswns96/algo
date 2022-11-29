import sys
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
while (m>0):
    a = nums[0]+nums[1]
    nums[0]=a
    nums[1]=a
    nums.sort()
    m-=1
print(sum(nums))

