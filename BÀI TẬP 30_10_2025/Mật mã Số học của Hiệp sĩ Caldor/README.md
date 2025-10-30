# ⚔️ Mật Mã Số Học Của Hiệp Sĩ Caldor

## 🧩 Mô tả bài toán
Cho **t** bộ test, mỗi test là một chuỗi các chữ số.  
Yêu cầu:  
- Kiểm tra xem chuỗi có thỏa **2 điều kiện** sau hay không:
  1. Hiệu tuyệt đối giữa hai chữ số liên tiếp luôn **bằng 2**.  
  2. Tổng tất cả các chữ số trong chuỗi chia hết cho **10**.  
- Nếu cả hai điều kiện đều đúng → in `YES`  
- Ngược lại → in `NO`.

---

## 💡 Ý tưởng
- Duyệt qua các cặp chữ số liên tiếp trong chuỗi, kiểm tra điều kiện `|a[i] - a[i-1]| == 2`.  
- Nếu **mọi cặp đều hợp lệ**, tiếp tục kiểm tra tổng chữ số.  
- Nếu tổng chia hết cho 10, in `YES`, ngược lại in `NO`.

---

## 🧠 Giải thích thuật toán
1. Đọc vào số lượng test `t`.  
2. Với mỗi chuỗi `string`:
   - Kiểm tra điều kiện 1 bằng cách duyệt qua các cặp liên tiếp:
     ```python
     all(abs(int(string[i]) - int(string[i - 1])) == 2 for i in range(1, len(string)))
     ```
     Nếu đúng với mọi cặp → `is_valid_diff = True`, ngược lại `False`.  
   - Tính tổng các chữ số:
     ```python
     total = sum(int(ch) for ch in string)
     ```
   - Kiểm tra điều kiện 2:  
     ```python
     is_valid_sum = (total % 10 == 0)
     ```
   - Nếu **cả hai điều kiện đều đúng** → in `"YES"`, ngược lại `"NO"`.

---

## 🧾 Code mẫu

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
