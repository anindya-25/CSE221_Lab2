n,s = map(int,input().split())
lis1 = list(map(int,input().split()))
i,j = 0,n-1
found = False
while i<j:
    if lis1[i] + lis1[j] < s:
        i += 1
    elif lis1[i] + lis1[j] > s:
        j -= 1
    elif lis1[i] + lis1[j] == s:
        print(f"{i+1} {j+1}")
        found = True
        break
if not found:
    print(-1)