n = int(input())
input_list = [list(map(str, input().split())) for _ in range(n)]


emp = [(0,'')]
result_str=''
for i in input_list:
    flag =False

    if i[0] =='type':
        result_str+=i[1]
        emp.append((int(i[2]),result_str))

        
    else:
        time_b= int(i[2])-int(i[1])
        for k in range(len(emp)-1,-1,-1):
            if emp[k][0] >= time_b:
                continue
            flag = True
            result_str =emp[k][1]
            emp.append((int(i[2]),result_str))
            break
        if not flag:
            result_str = ''
            emp.append((int(i[2]), result_str))

print(emp[-1][1])

