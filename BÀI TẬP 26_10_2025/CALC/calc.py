t = 2
while t > 0:
    lst = list(map(int, input().split()))
    lst.sort()

    if lst[0] + lst[1] - lst[2] == 0:
        print("yes")
    else:
        print("no")

    t -= 1
    print()
