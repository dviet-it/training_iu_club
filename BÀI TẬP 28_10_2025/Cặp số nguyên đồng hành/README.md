# Giải thích bài toán: Cặp số nguyên đồng hành

## Đề bài
Cho một danh sách các số nguyên.  
Hai số được gọi là **đồng hành** nếu **ước chung lớn nhất (GCD)** của chúng bằng **1**.

Nhiệm vụ của chương trình là:
- Đọc vào số lượng phần tử `n` và danh sách `n` số nguyên.
- In ra tất cả các cặp số đồng hành (mỗi cặp trên một dòng).

---

## Ý tưởng giải
1. Viết hàm `gcd(a, b)` để tính **ước chung lớn nhất** bằng thuật toán Euclid.
2. Duyệt qua tất cả các cặp `(i, j)` với `i < j`.
3. Với mỗi cặp, nếu `gcd(lst[i], lst[j]) == 1` thì in ra cặp đó.

---

## Độ phức tạp
- Có `n` phần tử, mỗi lần ta so sánh một cặp nên có tổng cộng **O(n²)** cặp cần kiểm tra.
- Thuật toán Euclid có độ phức tạp trung bình **O(log(min(a, b)))**.  
→ Tổng thể: **O(n² * log(max(a, b)))** – phù hợp với kích thước nhỏ và trung bình.

---

## Code minh họa

```python
def gcd(a, b):
    while(b != 0):
        tmp = a % b
        a = b
        b = tmp

    return a
n = int(input())
lst = list(map(int, input().split()))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if gcd(lst[i], lst[j]) == 1:
            print(lst[i], lst[j], end = "\n")
