# 🧩 Giải Mã Bức Thư Hoang Ngữ

## 📘 Mô tả chương trình
Chương trình đọc **một dòng dữ liệu đầu vào** gồm các từ (hoặc chuỗi ký tự) được **phân tách bởi dấu cách**, sau đó **in ra từng phần tử trên một dòng riêng biệt**.  

Đây là ví dụ đơn giản về cách **xử lý chuỗi nhập vào, tách và duyệt từng phần tử** trong Python.

---

## 📜 Code nguồn

```python
lst = list(map(str, input().split()))

for index, nums in enumerate(lst):
    print(nums, end = "\n")
