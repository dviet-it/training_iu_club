# ⚔️ Trận Chiến Cân Bằng Giữa Bóng Tối Và Ánh Sáng

## 📘 Mô tả chương trình
Chương trình kiểm tra xem **đội Ánh Sáng** có thể chiến thắng hoặc cân bằng với **đội Bóng Tối** trong từng vị trí tương ứng hay không.  

Cụ thể, ta có hai danh sách số nguyên `A` và `B` (mỗi danh sách có cùng số phần tử).  
- Mỗi phần tử của `A` và `B` biểu thị **sức mạnh chiến binh**.  
- Nếu sau khi sắp xếp tăng dần, với mọi chỉ số `i`, ta có `A[i] ≤ B[i]`,  
  thì kết quả là **"YES"**, ngược lại là **"NO"**.

---

## 📜 Code nguồn

```python
t = int(input())

while t > 0:
    case = int(input())
    
    lsta = list(map(int, input().split()))
    lstb = list(map(int, input().split()))

    lsta.sort()
    lstb.sort()

    check = True
    for i in range(0, len(lsta)):
        if lsta[i] > lstb[i]:
            check = False

    if check:
        print("YES")
    else:
        print("NO")
    
    t -= 1
