n = int(input())
for i in range(n):
    st = input()
    s,e = 0,len(st)-1
    idx = -1
    while s<=e:
        mid = (s+e)//2
        if st[mid] == "1":
            idx = mid
            e = mid-1
        else:
            s = mid+1
    if idx == -1:
        print(-1)
    else:
        print(idx+1)