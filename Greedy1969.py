n, m = map(int, input().split())
DNA = []
Hamming_Distance=[] 
for _ in range(n):
    DNA.append(str(input()))
result=''
sum=0
DNA_dict={'A':0,'C':0,'G':0,'T':0}
for i in range(m):
    DNA_dict={'A':0,'C':0,'G':0,'T':0}
    for j in DNA:
        DNA_dict[j[i]]+=1
    result+=max(DNA_dict,key=DNA_dict.get)
    sum+=n-DNA_dict[max(DNA_dict,key=DNA_dict.get)]

print(result)
print(sum)
