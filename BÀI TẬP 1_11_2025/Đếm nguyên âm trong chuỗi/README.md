#  Đếm Nguyên Âm Trong Chuỗi

##  Mô tả bài toán
Cho một chuỗi ký tự bất kỳ.  
Yêu cầu:  
- Đếm xem trong chuỗi có bao nhiêu **nguyên âm** (a, e, i, o, u).  
- Không phân biệt chữ hoa hay chữ thường.

---

##  Ý tưởng
- Đưa toàn bộ chuỗi về dạng **chữ thường** bằng `lower()`.  
- Duyệt qua từng ký tự trong chuỗi:
  - Nếu ký tự đó thuộc tập các nguyên âm `"a", "e", "i", "o", "u"` → tăng biến đếm.  
- In ra tổng số nguyên âm đếm được.

---

##  Giải thích thuật toán
1. Nhập vào một chuỗi ký tự từ bàn phím.  
2. Chuyển chuỗi sang chữ thường để tránh phân biệt hoa – thường.  
3. Khởi tạo biến `cnt = 0` để đếm số nguyên âm.  
4. Duyệt từng ký tự `ch` trong chuỗi:
   - Nếu `ch` nằm trong `{a, e, i, o, u}` → tăng `cnt` lên 1.  
5. Sau khi duyệt hết chuỗi, in ra giá trị `cnt`.

---

##  Code mẫu

```python
string = input()
string = string.lower()

cnt = 0

for ch in string:
    if ch == "a" or ch == "e" or ch == "o" or ch == "i" or ch == "u":
        cnt += 1
print(cnt)
