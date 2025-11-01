#  Thuật Toán Kỳ Lạ

##  Mô tả bài toán
Cho một số nguyên dương **t**.  
Yêu cầu:  
- In ra **dãy số** được tạo theo quy tắc sau (còn gọi là **dãy Collatz**):  
  - Nếu `t` là **số chẵn** → chia đôi (`t = t / 2`).  
  - Nếu `t` là **số lẻ** → nhân ba rồi cộng một (`t = t * 3 + 1`).  
- Lặp lại quá trình cho đến khi giá trị của `t` trở về **1**.  
- In toàn bộ dãy ra trên **một dòng**, các số cách nhau bởi dấu cách.

---

##  Ý tưởng
- Dùng vòng lặp `while` để thực hiện phép biến đổi cho đến khi `t == 1`.  
- Mỗi bước in ra giá trị hiện tại của `t`.  
- Cập nhật `t` theo quy tắc Collatz:
  - Nếu chẵn → chia đôi.
  - Nếu lẻ → nhân 3 rồi cộng 1.

---

##  Giải thích thuật toán
1. Đọc vào số nguyên `t`.  
2. In giá trị ban đầu của `t`.  
3. Dùng vòng lặp:
   - Nếu `t` chẵn → `t //= 2`.  
   - Nếu `t` lẻ → `t = t * 3 + 1`.  
   - In ra giá trị `t` sau mỗi lần cập nhật.  
4. Kết thúc khi `t == 1`.

---

##  Code mẫu

```python
t = int(input())

print(t, end = " ")
while t != 1:
    if t % 2 == 0:
        t //= 2
    else:
        t = t * 3 + 1
    print(t, end = " ")
