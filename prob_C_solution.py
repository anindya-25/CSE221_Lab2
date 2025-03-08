n, k = map(int, input().split())
inp_list = list(map(int, input().split()))

start = 0
curr = 0
max_length = 0

for end in range(n):
    curr += inp_list[end]

    while curr > k:
        curr -= inp_list[start]
        start += 1

    max_length = max(max_length, end - start + 1)

print(max_length)