#Hướng giải quyết

Bước 1: Đọc input mà đề bài cho:
n = int(input())
lst = list(map(int, input().split()))

Bước 2: giải quyết Logic

"""
sum = 0

for index, nums in enumerate(lst):
    if index % 2 == 1:
        sum += nums
"""

-Đầu tiên tạo biến sum = 0 để lưu tổng
-Vì đề hỏi "Tính tổng ở những vị trí lẻ của dãy nên ta sẽ duyệt mảng lst và tạo 2 cặp key-value đó chính là
index và nums in enumerate(lst)

-Ta hãy kiểm tra xem khi nào index chia 2 dư 1 thì đó chính là số lẻ.
Khi biết được index là số lẻ ta sẽ cộng sum với giá trị nums của lst

Bước 3: In kết quả
print(sum)


