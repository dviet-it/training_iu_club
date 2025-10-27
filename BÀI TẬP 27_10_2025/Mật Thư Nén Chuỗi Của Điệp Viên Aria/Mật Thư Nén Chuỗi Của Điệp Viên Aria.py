from collections import defaultdict

t = int(input())

while t > 0:
    string = input()
    
    cnt = defaultdict(int)

    for ch in string:
        cnt[ch] += 1
    
    for key, value in cnt.items():
        print(f"{value}{key}", end = "")
    
    print()
    t -= 1