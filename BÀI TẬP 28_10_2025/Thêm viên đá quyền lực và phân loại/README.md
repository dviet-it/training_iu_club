(các giá trị cách nhau bằng dấu cách)

---

##  Ý tưởng giải

1. Đọc vào số lượng test `t`.
2. Với mỗi test:
- Đọc `n` (số viên đá hiện có) và `k` (viên đá mới).
- Tìm viên đá mạnh nhất trong danh sách → lấy chỉ số `index`.
- **Chèn** viên đá mới `k` vào ngay **trước** viên đá mạnh nhất.
3. Duyệt danh sách mới:
- Nếu giá trị âm → đưa vào danh sách `lst_am`.
- Nếu giá trị dương → đưa vào danh sách `lst_duong`.
4. In ra hai danh sách nối liền: `lst_am` trước, rồi `lst_duong`.

---

##  Độ phức tạp

- Tìm `max` và `index`: **O(n)**  
- Chèn phần tử: **O(n)**  
- Duyệt tách âm/dương: **O(n)**  
→ Tổng thể: **O(n)** cho mỗi test.

---

##  Code minh họa

```python
t = int(input())

while t > 0:
 n, k = map(int, input().split())
 lst = list(map(int, input().split()))

 max_strength = max(lst)
 index = lst.index(max_strength)

 lst.insert(index, k)

 lst_am = []
 lst_duong = []


 for i in lst:
     if i > 0:
         lst_duong.append(i)
     else:
         lst_am.append(i)


print(*lst_am, *lst_duong)
