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
# asdasdas




# n = int(input())
# lst = list(map(int, input().split()))
# s = int(input())

# for i in range(n-1):
#     maxx = lst[i]
#     val = 0
#     if s == 0:
#         break
#     for j in range(i+1, n):
#         x = j-i
#         if lst[j] > maxx:
#             maxx = lst[j]
#             val = x
#         if x >= s:
#             break
#     if val:
#         s -= val
#         lst.remove(maxx)
#         lst.insert(i, maxx)

# for x in lst:
#     print(x, end=' ')        