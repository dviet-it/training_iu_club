#  So Sánh Sức Mạnh Hai Đội

##  Mô tả bài toán
Cho **t** bộ test, mỗi test là một chuỗi chữ số.  
Mỗi chuỗi biểu diễn sức mạnh của một đội.  
Pháp sư cần xác định xem đội đó có “sức mạnh cân bằng” hay không, dựa trên **2 quy tắc** sau:

1. Hiệu tuyệt đối giữa hai chữ số liên tiếp luôn **bằng 2**.  
2. Tổng tất cả các chữ số trong chuỗi chia hết cho **10**.

Nếu **cả hai điều kiện** đều đúng → in `YES`,  
ngược lại → in `NO`.

---

##  Ý tưởng
- Duyệt qua các cặp chữ số liên tiếp trong chuỗi, kiểm tra điều kiện `|a[i] - a[i-1]| == 2`.  
- Nếu điều kiện này đúng cho mọi cặp, tiếp tục kiểm tra tổng các chữ số.  
- Nếu tổng chia hết cho 10, kết luận “hai đội cân bằng”.

---

##  Giải thích thuật toán
1. Nhập số lượng test `t`.  
2. Với mỗi chuỗi `string`:
   - Kiểm tra hiệu tuyệt đối giữa các cặp liên tiếp:
     ```python
     is_valid_diff = all(abs(int(string[i]) - int(string[i - 1])) == 2 for i in range(1, len(string)))
     ```
   - Tính tổng các chữ số:
     ```python
     total = sum(int(ch) for ch in string)
     is_valid_sum = (total % 10 == 0)
     ```
   - In `"YES"` nếu cả hai điều kiện đều đúng, ngược lại `"NO"`.

---

##  Code mẫu

```python
t = int(input())

while t > 0:
    string = input().strip()

    is_valid_diff = all(abs(int(string[i]) - int(string[i - 1])) == 2 for i in range(1, len(string)))

    total = sum(int(ch) for ch in string)
    is_valid_sum = (total % 10 == 0)

    if is_valid_diff and is_valid_sum:
        print("YES")
    else:
        print("NO")
    t -= 1
