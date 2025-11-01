#  Ba Số Lớn Nhất

##  Mô tả bài toán
Cho một dãy các số nguyên.  
Yêu cầu:  
- Tìm **số lớn thứ 3** trong dãy.  
- Nếu dãy có **ít hơn 3 giá trị khác nhau**, hãy in ra **số lớn nhất**.

---

##  Ý tưởng
- Loại bỏ các phần tử trùng nhau bằng **`set()`**.  
- Sắp xếp danh sách các số khác nhau theo **thứ tự giảm dần**.  
- Nếu số lượng phần tử < 3 → in ra phần tử đầu tiên (lớn nhất).  
- Ngược lại → in ra phần tử thứ 3 trong danh sách đã sắp xếp.

---

##  Giải thích thuật toán
1. Đọc vào dãy số nguyên từ bàn phím, tách bằng khoảng trắng.  
2. Dùng `set()` để loại bỏ trùng lặp.  
3. Dùng `sorted(..., reverse=True)` để sắp xếp giảm dần.  
4. Kiểm tra độ dài danh sách:
   - Nếu nhỏ hơn 3 → in ra phần tử đầu tiên (`distinct[0]`).  
   - Nếu đủ 3 hoặc hơn → in ra phần tử thứ 3 (`distinct[2]`).

---

##  Code mẫu

```python
lst = list(map(int, input().split()))

distinct = sorted(set(lst), reverse=True)

if len(distinct) < 3:
    print(distinct[0])
else:
    print(distinct[2])
