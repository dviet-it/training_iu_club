n = int(input())
lst = list(map(int, input().split()))

sum = 0

for index, nums in enumerate(lst):
    if index % 2 == 1:
        sum += nums

print(sum)
