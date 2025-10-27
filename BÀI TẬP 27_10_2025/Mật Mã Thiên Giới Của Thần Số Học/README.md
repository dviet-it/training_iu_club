#Hướng dẫn giải:

def check(string):
    cnt_another_num = 0

    for ch in string:
        if ch.isdigit() and int(ch) != 4 and int(ch) != 7:
            cnt_another_num += 1

    if cnt_another_num == 0:
        return True

    return False

t = int(input())

while(t > 0):
    string = input()

    if check(string):
        print("YES")
    else:
        print("NO")
    t -= 1

Vì đề yêu cầu 1 mật mã chính là 1 dãy số chỉ có 4 hoặc 7 và không tồn tại các số nào khác
Nên ta chỉ cần tạo 1 hàm check và đặt biến cnt_another_num(tức đếm xong trong dãy có bao nhiêu số khác 4 và khác 7)
Nếu cnt_another_num == 0 thì tức là trong dãy chỉ có 4 và 7 còn nếu cnt_another_num > 0 thì có nghĩa trong dãy đã tồn tại ít nhất 1 số khác 4 và 7