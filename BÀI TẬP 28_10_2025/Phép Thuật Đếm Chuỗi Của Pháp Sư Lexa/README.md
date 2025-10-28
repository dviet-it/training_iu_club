
Nếu **tính chồng lặp**, có 4 lần xuất hiện (`aa` ở vị trí 0, 1, 2, 3).  
Nhưng vì bài yêu cầu **không tính chồng lặp**, nên kết quả chỉ là **2** (`aa` ở vị trí 0 và 2).

---

##  Ý tưởng giải
- Duyệt từng vị trí `i` trong chuỗi `s`.
- Nếu đoạn `s[i:i+len(n)]` trùng với chuỗi `n` → tăng biến đếm lên 1.
- Sau khi đếm được một chuỗi con, **nhảy qua toàn bộ độ dài của chuỗi con** (`i += len(n)`) để tránh đếm chồng lặp.
- Nếu không khớp thì chỉ tăng `i` thêm 1 và tiếp tục kiểm tra.

---

##  Độ phức tạp
- Duyệt qua từng ký tự của `s` ⇒ O(len(s))
- Mỗi lần so sánh substring dài len(n) ⇒ O(len(n))
- Tổng thể: **O(len(s) × len(n))**, đủ nhanh cho chuỗi có độ dài vừa phải.

---

##  Code minh họa

```python
t = int(input())

for _ in range(t):
    s = input().strip()
    n = input().strip()
    count = 0
    i = 0
    while i <= len(s) - len(n):
        if s[i:i+len(n)] == n:
            count += 1
            i += len(n)
        else:
            i += 1
    print(count)
