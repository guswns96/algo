import sys
from collections import deque

input = input = sys.stdin.readline

n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
degree=[0]*(n+1)
dQ=deque()
temp=[]
for i in range(n):
    temp.append([i for i in map(int, input().split())])
    degree[i+1] = temp[i][1]

for t,k in enumerate(temp):
    for i in k[2:]:
        graph[i][t]=1


for i in range(1,n+1):
    if degree[i]==0:
        dQ.append(i)
print(degree)
print(graph)
while dQ:
    print(dQ)
    x=dQ.popleft()
    for i in range(1,n+1):
        if graph[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                dQ.append(i)





