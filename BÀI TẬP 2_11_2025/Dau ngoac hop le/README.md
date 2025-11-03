# 🧮 Dấu Ngoặc Hợp Lệ

## 🧩 Mô tả bài toán
Cho một chuỗi ký tự gồm các dấu ngoặc `()`, `{}`, `[]`.  
Xác định xem chuỗi đó có **hợp lệ** hay không, nghĩa là:
- Mỗi dấu mở phải có dấu đóng tương ứng.
- Các cặp ngoặc phải **lồng đúng thứ tự**.

---

## 💡 Ý tưởng
- Duyệt từng ký tự:
  - Nếu là ngoặc mở → thêm vào danh sách theo dõi.  
  - Nếu là ngoặc đóng → kiểm tra xem có dấu mở tương ứng không.  
  - Nếu không có hoặc sai loại → chuỗi **không hợp lệ**.
- Sau khi duyệt xong:
  - Nếu còn dấu mở chưa đóng → **không hợp lệ**.
  - Ngược lại → **hợp lệ**.

---

## 🧾 Code mẫu
```python
string = input()

dct = {}
check = True

for ch in string:
    if ch == "{" or  ch == "[" or ch == "(":
        if ch not in dct:
            dct[ch] = 1
        else:
            dct[ch] += 1
    else:
        if ch == "}":
            if "{" not in dct:
                check = False
            else:
                dct["{"] -= 1

        elif ch == "]":
            if "[" not in dct:
                check = False
            else:
                dct["["] -= 1

        elif ch == ")":
            if "()" not in dct:
                check = False
            else:
                dct["("] -= 1
            
cnt = 0
for key, value in dct.items():
    cnt += value

if cnt == 0 and check == True:
    print("true")
else:
    print("false")
