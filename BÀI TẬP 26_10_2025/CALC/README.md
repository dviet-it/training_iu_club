#Hướng giải quyết

Bước 1: Đọc input mà đề cho
"""
t = 2
while t > 0:
    lst = list(map(int, input().split()))
    //code xử lí logic
    t -= 1
    

"""
Vì input là 2 câu hỏi độc lập nên ta sẽ đặt biến t = 2
và while t > 0:
    t -= 1

Để ta sẽ lần lượt từng câu hỏi riêng biệt mà đề cho

Bước 2: Xử lý logic
"""
    lst = list(map(int, input().split()))
    lst.sort()

    if lst[0] + lst[1] - lst[2] == 0:
        print("yes")
    else:
        print("no")

    print()
"""

Vì đề hỏi rằng có "tồn tại" hay không một cách sắp xếp để A1 + A2 - A3 = 0

Ta nhận ra rằng A1, A2 phải là 2 số nhỏ nhất trong mảng và A3 là số lớn nhất

vì nếu A1 hoặc A2 là số lớn nhất trong mảng thì sẽ luôn tồn tại A1 + A2 - A3 > 0 với mọi trường hợp

nên ta xét tổng A1 + A2 là tổng 2 số bé nhất trừ đi số lớn nhất là A3