#Hướng dẫn giải:
#
n = int(input())
lst = list(map(int, input().split()))

lst.sort()

minn = lst[0]
maxn = lst[n - 1]

if minn != 1:
    print(1)
else:
    sum_ovr = maxn * (maxn + 1) / 2

    sum_lst = sum(lst)

    if(sum_ovr - sum_lst == 0):
        print(maxn + 1)
    else:
        print(int(sum_ovr - sum_lst))
#
Ta sắp xếp mảng lst và kiểm tra xem có tồn tại phần tử 1 trong mảng không. Nếu có thì in ra 1 luôn còn không thì ta sẽ tính tổng từ 1 tới maxn và trừ đi tổng hiện tại của toàn bộ mảng lst để tìm ra số bị thiếu