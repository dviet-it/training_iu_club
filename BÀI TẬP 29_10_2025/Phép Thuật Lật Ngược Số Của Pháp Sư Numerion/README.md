
## Ý tưởng giải

1. Với mỗi test, đọc số `nums`.  
2. Nếu `nums` chưa chia hết cho `7`, thực hiện:  
   - Đảo ngược các chữ số của `nums`.  
   - Cộng giá trị đảo ngược vào `nums`.  
3. Lặp lại quá trình đến khi `nums % 7 == 0`.  
4. In ra kết quả cuối cùng.

## Code mẫu

```python
t = int(input())

while t > 0:
    nums = int(input())

    while nums % 7 != 0:
        string = str(nums)

        new_nums = int(string[::-1])

        nums += new_nums

    print(nums)
    t -= 1
