import bisect
n,q = map(int,input().split())
list1 = list(map(int,input().split()))
for i in range(q):
    start,end = map(int,input().split())
    start_idx = bisect.bisect_left(list1,start)
    end_idx = bisect.bisect_right(list1,end)
    print(end_idx-start_idx)