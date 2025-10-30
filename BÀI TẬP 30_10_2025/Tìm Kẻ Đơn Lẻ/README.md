#  Tìm Kẻ Đơn Lẻ

##  Mô tả bài toán
Cho **t** bộ test, mỗi test gồm:  
- Một số nguyên `n` – số lượng phần tử trong mảng.  
- Một dãy `n` số nguyên.

Yêu cầu:  
- Mỗi số trong mảng có thể xuất hiện **nhiều lần**.  
- Hãy **in ra các số xuất hiện số lần lẻ** (1, 3, 5, ...).  
- Các số được in **theo thứ tự xuất hiện trong từ điển (dict)**.

---

##  Ý tưởng
- Dùng **từ điển (`dict`)** để đếm số lần xuất hiện của từng phần tử.  
- Sau khi đếm xong, duyệt lại từ điển và in ra những phần tử có tần suất xuất hiện **lẻ**.  

---

##  Giải thích thuật toán
1. Nhập số lượng test `t`.  
2. Với mỗi test:
   - Nhập `n` – số lượng phần tử.  
   - Nhập danh sách `lst` gồm `n` số nguyên.  
   - Tạo một từ điển `dct` để lưu số lần xuất hiện của từng phần tử.  
   - Với mỗi phần tử:
     - Nếu chưa có trong `dct` → gán giá trị 1.  
     - Nếu đã có → tăng giá trị thêm 1.  
   - Sau khi đếm xong, in ra các phần tử có tần suất `% 2 != 0`.

---

##  Code mẫu

```python
t = int(input())

while t > 0:
    n = int(input())

    lst = list(map(int, input().split()))

    dct = {}

    for index, nums in enumerate(lst):
        if nums not in dct:
            dct[nums] = 1
        else:
            dct[nums] += 1
    
    for key, freq in dct.items():
        if freq % 2 != 0:
            print(key, end = " ")
    
    print()
    t -= 1
