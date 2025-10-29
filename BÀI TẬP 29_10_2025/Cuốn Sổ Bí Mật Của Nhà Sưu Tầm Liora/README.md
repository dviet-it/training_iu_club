
## Ý tưởng giải

1. Duyệt qua `t` dòng nhập.  
2. Nếu chuỗi khác `"-1"` và chưa từng xuất hiện trước đó, thêm vào danh sách lưu trữ (`mp`) và tăng bộ đếm `cnt`.  
3. In ra giá trị `cnt`.

## Code mẫu

```python
t = int(input())

mp = []

cnt = 0

while t > 0:
    string = input()

    if string not in mp and string != "-1":
        cnt += 1
        mp.append(string)
    t -= 1

print(cnt)
