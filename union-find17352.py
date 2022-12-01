import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input()) # 섬의 수 입력 받기

def find(a): # a 노드의 부모 노드 찾기
    if a == parent[a]: # a 노드가 부모 노드이면 a 반환
        return a
    p = find(parent[a]) # a 노드를 따라가면서 부모 노드 찾기
    parent[a] = p # 부모 테이블 갱신
    return parent[a]


def union(a, b): # a집합과 b집합 합치기
    a = find(a) # a 노드의 부모 노드 찾기
    b = find(b) # b 노드의 부모 찾기

    if a == b: # 이미 동일한 집합이면 연결시에 순환이 발생
        return

    if a < b: # a의 부모가 b 부모보다 상위 루트이면
        parent[b] = a # b의 부모를 a의 부모로 변경
    else: # b의 부모가 a 부모보다 상위 루트이면
        parent[a] = b # a의 부모 변경

parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

for y in range(1, N+1):
    maps = list(map(int, input().split()))
    if len(maps)==0:
        break
    for x in range(1, len(maps)+1):
        if maps[x-1] == 1:
            union(y, x)

print(parent)



