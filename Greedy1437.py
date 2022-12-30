import math
n= int(input())
num_list=[]
while (n>2):
    print(n,math.ceil(n/2))
    num_list.append(math.ceil(n/2))
    n = n-round(n/2)
    if n<=2:
        num_list.append(n)
        break
sum=0
asd=1
print(num_list)
for i in  num_list:
    sum+=i
    asd*=i
print(sum,asd%10007)

