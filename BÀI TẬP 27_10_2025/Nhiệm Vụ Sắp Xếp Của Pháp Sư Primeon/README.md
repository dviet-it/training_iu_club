#Hướng dẫn giải:

my code:

def check(n):
    if n < 2: return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False

    return True

n = int(input())
lst = list(map(int, input().split()))

isprime = []

for index, nums in enumerate(lst):
    if check(nums):
        isprime.append(nums)

isprime.sort()

start = 0
end = len(isprime)

for index, nums in enumerate(lst):
    if check(nums) and start < end:
        print(isprime[start], end = " ")
        start += 1
    else:
        print(nums, end = " ")


#Bước 1:
Viết hàm check kiểm tra số nguyên tố

#Bước 2:
Duyệt trong danh sách lst xem đâu là số nguyên tố và ta sẽ thêm số nguyên tố tìm thấy vào trong mảng isprime
Sau khi thêm hết số nguyên tố từ mảng lst vào trong mảng isprime. Ta sẽ sắp xếp các số nguyên tố trong mảng isprime lại theo thứ tự tăng dần và đặt biến start = 0 và end = len(isprime)

#Bước 3:
Duyệt 1 vòng nữa trong mảng lst và kiểm tra lại xem đâu là số nguyên tố. Nếu thấy số nguyên tố ta sẽ in số nguyên tố trong mảng isprime ra theo index start và tăng dần start lên
Nếu không phải số nguyên tố ta sẽ in các số bình thường.