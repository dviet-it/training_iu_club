# 🕵️‍♂️ Người Thủ Lĩnh Bí Ẩn Trong Làng Sương Trắng

## 📘 Mô tả chương trình
Chương trình này dùng để **tìm phần tử xuất hiện nhiều nhất trong danh sách số nguyên**.  
Nếu phần tử đó **xuất hiện ít nhất một nửa số phần tử của danh sách**, chương trình in ra giá trị đó.  
Ngược lại, in `"NO"`.

Nói cách khác, đây là bài toán **tìm phần tử chiếm đa số** (Majority Element) — tức là phần tử có tần suất ≥ n/2.

---

## 📜 Code nguồn

```python
t = int(input())

while t > 0:
    n = int(input())

    lst = list(map(int, input().split()))

    dct = {}
    min = -1
    correct = []
    expect = len(lst) // 2

    for index, nums in enumerate(lst):
        if nums not in dct:
            dct[nums] = 1
        else:
            dct[nums] += 1
        
        min = max(min, dct[nums])

    for key, value in dct.items():
        if value == min:
            correct = key    

    if min >= expect:
        print(correct)
    else:
        print("NO")

    t -= 1
