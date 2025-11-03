### 🧾 **Kiểm Tra Chia Hết Cho 3 – README.md**
```markdown
# Kiểm Tra Chia Hết Cho 3

## Ý tưởng
- Với mỗi test case, đọc vào số `n`.  
- Nếu `n % 3 == 0` thì in `YES`, ngược lại in `NO`.

## Code mẫu
```python
t = int(input())

while t > 0:
    n = int(input())

    if n % 3 == 0:
        print("YES")
    else:
        print("NO")
    t -= 1
