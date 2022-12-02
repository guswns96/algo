import sys
from itertools import combinations
n ,m= map(int, sys.stdin.readline().split())
map_list=[list(map(int, input().split())) for _ in range(n)]
house=[]
chicken =[]
result = 999999
for i in range(n):
    for j in range(n):
        if map_list[i][j]==1:
            house.append([i,j])
        if map_list[i][j]==2:
            chicken.append([i,j])

for c in combinations(chicken, m):
    all_distance = 0 
    for i in house:
        distance =9999

        for k in range(m):
            distance = min(distance, abs(i[0] - c[k][0]) + abs(i[1] - c[k][1]))
        all_distance += distance
    result = min(result, all_distance)
    
print(result)
