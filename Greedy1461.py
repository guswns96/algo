import sys
import numpy as np

n, m = map(int, input().split())

test= sorted([i for i in map(int,input().split())])




sum= 0
while test :
    print(test)
    i=0
    if len(test) < m:
        sum += abs(test[0]) * 2
        break
    elif len(test) == m:
        for i in range(len(test)):
            sum += abs(test[i])*2
        break
    if abs(test[0]) < abs(test[-1]):
        test.reverse()
    if sum ==0 :
        sum += abs(test[0])
        test = test[m:]
    else:
        sum+= abs(test[0])*2
        test = test[m:]




    print(sum)
print(sum)


#
# 7 2
# -37 2 -6 -39 -29 11 -28

# if abs(test[0]) < abs(test[-1]):
#     test.sort(reverse=True)
# print(test)
# sum =0
# for i in range(m , len(test),m):
#     if abs(test[0]) < abs(test[-1]):
#         test.sort(reverse=True)
#     if test[i] < 0:
#       sum +=  abs(test[i])*2
#       test = test[m:]
#     else:
#         sum+= test[i]*2
#         test = test[m:]
#     print(test[i], sum)
#
#
# if test[0] > 0:
#     sum+=test[0]
# else :
#     sum+= test[0]*(-1)
# test[0]*(-1)
#
#
#
# print(sum)