
## Ý tưởng giải

1. Chia chuỗi đầu vào thành các nhóm 2 ký tự liên tiếp.  
2. Lưu từng nhóm vào danh sách `lst`.  
3. Duyệt qua danh sách này, nếu cặp ký tự chưa xuất hiện trong `ans` thì thêm vào.  
4. In ra toàn bộ các phần tử trong `ans`, cách nhau bởi dấu cách.

## Code mẫu

```python
string = input()

lst = []

start = 0

while start < len(string):
    lst.append(string[start : start + 2])
    start += 2

ans = []

for index, nums in enumerate(lst):
    if nums not in ans:
        ans.append(nums)

print(*ans)
