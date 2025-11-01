#  Tìm Số Nhỏ Nhất Trong Ba Số

##  Mô tả bài toán
Cho ba số thực (hoặc nguyên).  
Yêu cầu:  
- Tìm **số nhỏ nhất** trong ba số đó.  
- Nếu kết quả là **số nguyên**, chỉ in phần nguyên (không có `.0`).  
- Nếu không, in ra **giá trị thực đầy đủ**.

---

##  Ý tưởng
- Đọc ba số từ đầu vào (có thể là số nguyên hoặc số thực).  
- Dùng hàm **`min()`** để tìm giá trị nhỏ nhất trong danh sách.  
- Kiểm tra xem kết quả có phải số nguyên bằng `is_integer()`.  
  - Nếu đúng → in ra bằng `int(m)`.  
  - Ngược lại → in ra giá trị `m` gốc.

---

##  Giải thích thuật toán
1. Đọc toàn bộ dữ liệu từ `stdin` và tách thành danh sách `data`.  
2. Chuyển từng phần tử trong `data` sang dạng `float`.  
3. Dùng `min(nums)` để lấy giá trị nhỏ nhất trong danh sách.  
4. Nếu kết quả là số nguyên (`m.is_integer() == True`) → ép kiểu và in phần nguyên.  
5. Ngược lại → in ra số thực ban đầu.

---

##  Code mẫu

```python
import sys

data = sys.stdin.read().strip().split()
nums = [float(x) for x in data]

m = min(nums)

print(int(m) if m.is_integer() else m)
