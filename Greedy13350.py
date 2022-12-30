import sys
n = int(input())
street_list = list(map(int, sys.stdin.readline().split()))
price_list = list(map(int, sys.stdin.readline().split()))
first=price_list[0]
all_price=0
for i in range(0, n-1):
    if first > price_list[i] :
        first =price_list[i]
    all_price += first * street_list[i]


print(all_price)
