#Hướng dẫn giải:
#
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
#

Đầu tiên ta import một thư viện defaultdict từ collections.
Sau đó ta tạo một defauldict(int) nhằm để lưu trữ tần số xuất hiện của từng chữ cái trong string
Sau đó ta duyệt key, value từ cnt.items() để in ra các tần số xuất hiện của chữ cái trong string