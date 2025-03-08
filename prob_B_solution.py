n1 = int(input())
lis1 = list(map(int,input().split()))
n2 = int(input())
lis2 = list(map(int,input().split()))
out_list = []
i,j = 0,0
while i != len(lis1) and j != len(lis2):
    if lis1[i] <= lis2[j]:
        out_list.append(lis1[i])
        i += 1
    else:
        out_list.append(lis2[j])
        j += 1
if i == len(lis1):
    for k in range(j,len(lis2)):
        out_list.append(lis2[k])
elif j == len(lis2):
    for k in range(i,len(lis1)):
        out_list.append(lis1[k])

for idx in range(len(out_list)):
    if idx == len(out_list)-1:
        print(out_list[idx])
    else:
        print(out_list[idx], end = " ")