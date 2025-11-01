#  Phần Tử Chiếm Đa Số

##  Mô tả bài toán
Cho một dãy các số nguyên.  
Yêu cầu:  
- Tìm **phần tử xuất hiện nhiều nhất** trong dãy.  
- Nếu có nhiều phần tử cùng tần suất lớn nhất, **in ra phần tử xuất hiện trước tiên** trong dãy ban đầu.

---

##  Ý tưởng
- Duyệt dãy và sử dụng **từ điển (dictionary)** để lưu số lần xuất hiện của từng phần tử.  
- Cập nhật giá trị **tần suất lớn nhất** khi duyệt.  
- Sau khi đếm xong, duyệt lại từ điển để tìm phần tử đầu tiên có tần suất bằng `max_freq`.  
- In ra phần tử đó.

---

##  Giải thích thuật toán
1. Đọc vào dãy số nguyên từ bàn phím, tách bằng khoảng trắng.  
2. Tạo từ điển `dct` để đếm số lần xuất hiện của mỗi phần tử.  
3. Khởi tạo `max_freq = -1` để lưu tần suất lớn nhất.  
4. Khi duyệt qua từng phần tử:
   - Nếu phần tử chưa có trong `dct` → thêm vào với giá trị 1.  
   - Ngược lại → tăng giá trị đếm thêm 1.  
   - Cập nhật `max_freq` = max(`max_freq`, số lần xuất hiện hiện tại).  
5. Sau khi duyệt hết dãy, tìm phần tử đầu tiên có tần suất = `max_freq` và in ra.

---

##  Code mẫu

```python
lst = list(map(int, input().split()))

dct = {}

max_freq = -1
for index, nums in enumerate(lst):
    if nums not in dct:
        dct[nums] = 1
    else:
        dct[nums] += 1
    max_freq = max(max_freq, dct[nums])

for value, frequency in dct.items():
    if frequency == max_freq:
        print(value)
        break
