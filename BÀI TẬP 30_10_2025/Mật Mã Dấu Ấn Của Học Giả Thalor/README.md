#  Mật Mã Dấu Ấn Của Học Giả Thalor

##  Mô tả bài toán
Cho **t** bộ test, mỗi test là một chuỗi chỉ gồm các dấu ngoặc tròn `"("` và `")"`.  
Yêu cầu:  
- Đánh số thứ tự cho từng cặp ngoặc mở–đóng theo **thứ tự xuất hiện**.  
- Khi gặp dấu `"("`, gán cho nó một số thứ tự tăng dần.  
- Khi gặp dấu `")"`, in ra **cùng số thứ tự** với dấu `"("` tương ứng.

---

##  Ý tưởng
- Sử dụng **ngăn xếp (stack)** để lưu trữ thứ tự của các dấu `"("`.  
- Mỗi lần gặp `"("`, tăng biến đếm `cnt` và đẩy giá trị đó vào stack.  
- Mỗi lần gặp `")"`, lấy giá trị trên đỉnh stack (cặp tương ứng) rồi in ra.  
- In ra theo đúng thứ tự các ký tự trong chuỗi.

---

##  Giải thích thuật toán
1. Đọc vào số lượng test `t`.  
2. Với mỗi chuỗi:
   - Tạo danh sách rỗng `lst` để làm stack.  
   - Tạo biến `cnt = 0` để đếm số ngoặc `"("` đã gặp.  
   - Duyệt qua từng ký tự `ch` trong chuỗi:
     - Nếu là `"("`:  
       - Tăng `cnt` lên 1.  
       - Thêm `cnt` vào `lst`.  
       - In `cnt` (vì đây là dấu mở mới).
     - Nếu là `")"`:  
       - In giá trị trên đỉnh stack (`lst[-1]`) vì nó khớp với dấu `"("` vừa mở.  
       - Xóa phần tử đó khỏi stack (`pop`).  
   - Sau khi duyệt hết chuỗi, in xuống dòng.

---

##  Code mẫu

```python
t = int(input())

while t > 0:
    string = input().strip()

    lst = []
    cnt = 0

    for ch in string:
        if ch == "(":
            cnt += 1
            lst.append(cnt)
            print(lst[len(lst) - 1], end = " ")
        else:
            print(lst[len(lst) - 1], end = " ")
            lst.pop(len(lst) - 1)
            
    print()
    t -= 1
