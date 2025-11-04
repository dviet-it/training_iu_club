# 🧩 Kiểm Tra Mã Định Danh Tinh Thể Số

## 📘 Mô tả chương trình
Chương trình kiểm tra xem một chuỗi có phải là **địa chỉ IP hợp lệ (IPv4)** hay không.  
Một địa chỉ IP hợp lệ có dạng:
trong đó:
- Mỗi `xi` là **một số nguyên từ 0 đến 255**.  
- Không được có **số 0 ở đầu** (ngoại trừ số `0` duy nhất).  
- Tổng cộng phải có **4 phần** tách nhau bằng dấu `"."`.

---

## 📜 Code nguồn

```python
t = int(input())

while t > 0:
    string = input().strip()
    lst = string.split(".")

    check = True
    size = 0
    for ch in lst:
        if ch.isdigit():
            size += 1

            # Không được có số 0 ở đầu nếu độ dài > 1
            if len(ch) > 1 and ch[0] == "0":
                check = False

            # Mỗi phần phải nằm trong [0, 255]
            if not (0 <= int(ch) <= 255):
                check = False
        else:
            check = False

    # Phải có đúng 4 phần
    if size != 4:
        check = False

    print("YES" if check else "NO")
    t -= 1
