
---

## 🧩 **3. Tìm số lớn nhất trong ba số (`Tìm số lớn nhất trong ba số.PY`)**
```markdown
# 🔺 Tìm Số Lớn Nhất Trong Ba Số

## 🧩 Mô tả bài toán
Nhập vào ba số thực `a`, `b`, `c`.  
In ra **số lớn nhất** trong ba số đó.

---

## 🧾 Code mẫu
```python
a = float(input())
b = float(input())
c = float(input())

lst = []
lst.append(a)
lst.append(b)
lst.append(c)

maxx = max(lst)

if maxx.is_integer():
    print(int(maxx))
else:
    print(maxx)
