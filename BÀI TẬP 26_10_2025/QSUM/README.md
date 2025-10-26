#Hướng xử lý
Bước 1: Đọc input đề cho
"""
n, q = map(int, input().split())
lst = list(map(int, input().split()))
"""

Bước 2: Xử lý logic
"""
prefix = [0] * (n + 1)
for i in range(1, n + 1):
prefix[i] = prefix[i - 1] + lst[i - 1]

for _ in range(q):
l, r = map(int, input().split())
print(prefix[r] - prefix[l - 1])
"""

Vì đề sẽ cho q truy vấn và tính tổng từ đoạn l tới r của mảng
tức là lst[l] + lst[l + 1] + ... + lst[r]

với 0 <= l <= r <= n(với n là kích cỡ mảng)

ở dây ta sử dụng Prefix sum để lưu tổng giá trị từng bước
Và công thức để tính tổng từ lst[l] tới lst[r] của Prefix sum là Prefix[r] - Prefix[l - 1]