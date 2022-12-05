import heapq
import sys
from collections import deque
input = sys.stdin.readline

# n = 학생의 수
print ('rsi의 w를 입력하시오' )
n = int(input())
print(n)
print ('macd의 s를 입력하시오' )
s = int(input())
print(s)
graph = [[] for i in range(n)]
indegree=[0] * (n)
for i in range(0, n):
    a, b = map(int, input().split())
    graph[i].append(a)
    graph[i].append(b)
    indegree[a-1] += 1
    indegree[b-1] +=1
    print(graph)
    print(indegree)

# print(graph)

def topology_sort():
    result=[]
    q = deque()
    for i in range(0,n):
        if indegree[i]  >2:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        print(now)

        for i in graph[now]:
            indegree[i-1]-=1
            if indegree[i-1]==0:
                q.append(i)
    for i in result:
        print(i,end= ' ')
topology_sort()






