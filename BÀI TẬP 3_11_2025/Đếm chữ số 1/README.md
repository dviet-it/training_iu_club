# Đếm chữ số 1

## Ý tưởng
- Duyệt tất cả các số từ 1 đến `n`.
- Với mỗi số, chuyển sang chuỗi rồi đếm số lần xuất hiện của ký tự `'1'`.
- Cộng dồn toàn bộ kết quả.

## Code mẫu
```python
def check(nums):
    cnt = 0
    string = str(nums)

    for ch in string:
        if ch == "1":
            cnt += 1

    return cnt

nums = int(input())
cnt = 0

for i in range(1, nums + 1):
    cnt += check(i)

print(cnt)
