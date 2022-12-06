# import sys
# import numpy as np
#
# n = int(input())
# temp = []
# test=[]
# num = [i for i in range(9, -1, -1 )]
# for i in range(n):
#     s = str(input())
#     temp.append(s)
#     test+=list(s)
# #
# #
# # temp_split = []
# # for i in temp:
# #     temp_split+=list(i)
# print(temp, test)
# # for i in range(len(set(temp_split))):
n = int(input())
words = []
alpha_value = {}
for _ in range(n):
    words.append(list(input().rstrip()))

for word in words:
    for i in range(len(word)):
        if word[i] not in alpha_value:
            alpha_value[word[i]] = 10 ** (len(word) - 1 - i)

        else:
            alpha_value[word[i]] += 10 ** (len(word) - 1 - i)

alpha_value = sorted(alpha_value.items(), key=lambda x: x[1], reverse=True)

alpha_to_num = {}

num = 9
for alpha in alpha_value:
    alpha_to_num[alpha[0]] = num
    num -= 1

ans = 0
for word in words:
    num = ""
    for alpha in word:
        num += str(alpha_to_num[alpha])

    ans += int(num)

print(ans)