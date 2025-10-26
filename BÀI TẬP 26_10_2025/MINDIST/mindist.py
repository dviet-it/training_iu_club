n = int(input())
lst = list(map(int, input().split()))

pos = {}

min_index = 10**10

for index, nums in enumerate(lst):
    if(nums not in pos):
        pos[nums] = index
    else:
        min_index = min(min_index, index - pos[nums])
        pos[nums] = index

if min_index == 10**10:
    print(-1)
else:
    print(min_index)
