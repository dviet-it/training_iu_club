# 🔮 Phép Thuật Số Nguyên Tố Của Pháp Sư Digitus

## 🧩 Đề bài
Pháp sư **Digitus** có một chuỗi ký tự chỉ gồm các chữ số (`0–9`).  
Mỗi chữ số có thể là **số nguyên tố** (2, 3, 5, 7) hoặc **không nguyên tố** (0, 1, 4, 6, 8, 9).

Pháp sư muốn kiểm tra xem một chuỗi có phải là **chuỗi ma thuật** hay không, theo hai điều kiện:

1. Độ dài của chuỗi phải là **số nguyên tố**.  
2. Số lượng **chữ số nguyên tố** trong chuỗi phải **nhiều hơn** số lượng chữ số **không nguyên tố**.

Nếu cả hai điều kiện đều đúng → in `YES`, ngược lại → in `NO`.

---

##  Ý tưởng giải

1. Viết hàm `isprime(n)` để kiểm tra một số có phải số nguyên tố hay không.  
   - Nếu `n < 2` → không nguyên tố.  
   - Duyệt từ `2` đến `√n` để kiểm tra ước chia.
2. Viết hàm `check(string)` để kiểm tra xem chuỗi có “ma thuật” không:
   - Đếm số lượng ký tự nguyên tố (`cnt_isprime`).
   - Tính số lượng ký tự không nguyên tố (`not_isprime`).
   - Nếu độ dài chuỗi là **số nguyên tố** và `cnt_isprime > not_isprime` → trả về `True`.
3. Duyệt qua từng test case và in `YES` hoặc `NO` tương ứng.

---

##  Độ phức tạp

- Kiểm tra số nguyên tố: `O(√n)`  
- Duyệt toàn chuỗi để đếm: `O(len(string))`  
- Tổng thể: **O(t × len(string))**, đủ nhanh cho giới hạn thông thường.

---


```python
def isprime(n):
    if n < 2: return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def check(string):
    size = len(string)

    cnt_isprime = 0

    for ch in string:
        if isprime(int(ch)):
            cnt_isprime += 1
    
    not_isprime = size - cnt_isprime

    if isprime(size) and  cnt_isprime > not_isprime:
        return True

    return False

t = int(input())

while t > 0:

    string = input()

    if check(string):
        print("YES")
    else:
        print("NO")

    t -= 1
