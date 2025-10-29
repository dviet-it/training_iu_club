
## Ý tưởng giải

1. Đọc `t` dòng và lưu lại thành danh sách `lst`.  
2. Tạo ma trận ký tự từ danh sách này.  
3. Duyệt từng hàng và từng cột để đếm số lượng ký tự `'C'`.  
4. Với mỗi hàng và cột, cộng vào tổng kết quả `cnt` theo công thức  
   `cnt += cnt_left // 2 + cnt_down // 2`.  
5. In ra tổng kết quả cuối cùng.

## Code mẫu

```python
t = int(input())

lst = []
for _ in range(t):
    string = input().strip()
    lst.append(string)

n = len(lst)
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(len(lst[i])):
        matrix[i][j] = lst[i][j]


cnt = 0

for rows in range(0, len(lst)):
    cnt_left = 0
    cnt_down = 0

    for cols in range(0, len(lst)):
        if matrix[rows][cols] == "C":
            cnt_left += 1
        if matrix[cols][rows] == "C":
            cnt_down += 1
    cnt += cnt_left // 2 + cnt_down // 2


print(cnt)
