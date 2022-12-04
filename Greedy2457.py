import sys
n = int(input())
end_day = 301
day_list=[]
for _ in range(n):
    start_m, start_d, end_m, end_d = map(int, sys.stdin.readline().split())
    day_list.append([start_m * 100 + start_d, end_m * 100 + end_d])
day_list.sort()
count_flo=0
for i in range(len(day_list)):
    max_num = 0
    temp=[]
    for j in range(len(day_list)):
        if day_list[j][0]<=end_day and day_list[j][1]>end_day:
            
            if max_num<day_list[j][1]:
                max_num = day_list[j][1]

                temp.append(1)

        elif day_list[j][0]>end_day:
            break
    end_day = max_num
    print(end_day)
    del day_list[:len(temp)]
    count_flo+=1   
    if end_day>1201:
        break
if end_day<1201:
    print(0) 
else:
    print(count_flo) 



