
---

### 🧾 **Ký tự duy nhất đầu tiên trong một chuỗi – README.md**
```markdown
# Ký tự duy nhất đầu tiên trong một chuỗi

## Ý tưởng
- Dùng dictionary đếm số lần xuất hiện của từng ký tự.  
- Duyệt lại chuỗi, tìm ký tự có số lần xuất hiện bằng 1 đầu tiên.  
- Nếu không có, in `-1`.

## Code mẫu
```python
string = input()

dct = {}

for index, ch in enumerate(string):
    if ch not in dct:
        dct[ch] = 1
    else:
        dct[ch] += 1

pos = 1000000000
for index, ch in enumerate(string):
    if dct[ch] == 1:
        pos = min(pos, index)

if pos == 1000000000:
    print(-1)
else:
    print(pos)
