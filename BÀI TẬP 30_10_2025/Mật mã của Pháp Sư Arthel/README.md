#  Mật Mã Của Pháp Sư Arthel

##  Mô tả bài toán
Cho **t** bộ test, mỗi test gồm một chuỗi số (gọi là "mật mã").  
Yêu cầu:  
- Kiểm tra xem các chữ số trong chuỗi đó có **tăng dần hoặc không giảm dần** từ trái sang phải hay không.  
- Nếu đúng → in `YES`  
- Nếu sai → in `NO`

---

##  Ý tưởng
- Duyệt từng ký tự trong chuỗi, so sánh mỗi chữ số với chữ số đứng trước nó.  
- Nếu phát hiện một chữ số **nhỏ hơn** chữ số trước đó ⇒ chuỗi **không hợp lệ**.  
- Ngược lại, nếu không có trường hợp nào như vậy ⇒ chuỗi **hợp lệ**.

---

##  Giải thích thuật toán
1. Đọc vào số lượng test `t`.  
2. Lặp lại `t` lần:
   - Nhập chuỗi `string`.
   - Giả sử ban đầu chuỗi hợp lệ (`check = True`).
   - Duyệt từ vị trí thứ 2 trở đi:
     - Nếu `string[i] < string[i-1]` ⇒ gán `check = False`.
   - Sau vòng lặp:
     - Nếu `check` vẫn là `True` ⇒ in `"YES"`.
     - Ngược lại ⇒ in `"NO"`.

---

##  Code mẫu

```python
t = int(input())

while t > 0:
    string = input().strip()

    check = True

    for i in range(1, len(string)):
        if int(string[i]) < int(string[i - 1]):
            check = False

    if check:
        print("YES")
    else:
        print("NO")

    t -= 1
