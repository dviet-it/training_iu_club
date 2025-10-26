#Hướng giải quyết
Bước 1: Đọc input đề cho
"""
n = int(input())
lst = list(map(int, input().split()))
"""

Bước 2: Xử lý Logic bài yêu cầu

"""
pos = {}

min_index = 10**10

for index, nums in enumerate(lst):
    if(nums not in pos):
        pos[nums] = index
    else:
        min_index = min(min_index, index - pos[nums])
        pos[nums] = index

if min_index == 10**10:
    print(-1)
else:
    print(min_index)
"""


Đề hỏi rằng đâu là khoảng cách nhỏ nhất giữa 2 phần tử trong nhau trong 1 mảng.

Đầu tiên ta sẽ tạo 1 dictionary pos = {} để lưu giá trị và vị trí của phần tử trong lst

Ta sẽ duyệt index và nums trong enumerate(lst)

-Kiểm tra xem giá trị nums đã có trong dictionary pos chưa.
+Nếu chưa có thì ta sẽ thêm giá trị nums là key trong pos và value chính là index
+Nếu có rồi thì ta hiểu rằng, lúc này trong vòng lặp đã gặp 1 giá trị nums trùng với key trong dictionary pos
và nhận ra ngay rằng đây sẽ là lúc để ta tính toán khoảng cách giữa 2 giá trị trùng nhau trong mảng
Ta sẽ tìm "khoảng cách nhỏ nhất" bằng cách dùng câu lệnh """min_index = min(min_index, index - pos[nums])"""
bởi vì, sẽ có trường hợp rất nhiều giá trị trùng nhau và khoảng cách cũng khác nhau nên ta dùng min để tìm khoảng cách nhỏ nhất
Và khi tìm ra rồi ta sẽ gắn giá trị value của key hiện tại là index