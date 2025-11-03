a, b = map(int, input().split())

tc = 0
tl = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        tc = i
    else:
        tl += i

print(tc, tl)