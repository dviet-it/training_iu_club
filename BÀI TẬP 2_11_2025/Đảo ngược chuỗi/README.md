
---

## 🧩 **5. Đảo ngược chuỗi (`Đảo ngược chuỗi.py`)**

```markdown
# 🔄 Tổng Chẵn Lẻ Trong Khoảng

## 🧩 Mô tả bài toán
Nhập hai số nguyên `a` và `b`.  
Tính:
- Biến `tc` – gán bằng **số chẵn cuối cùng** trong đoạn `[a, b]`.  
- Biến `tl` – là **tổng các số lẻ** trong đoạn `[a, b]`.  
Sau đó in ra `tc` và `tl`.

---

## 🧾 Code mẫu
```python
a, b = map(int, input().split())

tc = 0
tl = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        tc = i
    else:
        tl += i

print(tc, tl)
