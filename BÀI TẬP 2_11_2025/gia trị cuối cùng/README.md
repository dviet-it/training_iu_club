
---

## 🧩 **2. Giá trị cuối cùng (`gia trị cuối cùng.py`)**
```markdown
# 🔢 Giá Trị Cuối Cùng

## 🧩 Mô tả bài toán
Cho nhiều câu lệnh dạng:
- `"++X"` hoặc `"X++"` → tăng biến `x` thêm 1  
- `"--X"` hoặc `"X--"` → giảm biến `x` đi 1  

Yêu cầu: Tính **giá trị cuối cùng của `x`** sau khi thực hiện tất cả các lệnh.

---

## 🧾 Code mẫu
```python
import sys

x = 0
for s in sys.stdin.read().split():
    if "++" in s:
        x += 1
    else:
        x -= 1
print(x)
