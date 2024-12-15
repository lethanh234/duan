import math 
class hoadon :
    def __init__(self,ten,id,gia):
        self.id = id
        self.ten = ten 
        self.gia = gia
        if gia <= 50 :
            self.kq = (gia*100) + (gia*100)*0.02
        if gia > 50 and gia <= 100 :
            self.kq = ((50*100) + (gia-50)*150) + ((50*100) + (gia-50)*150)*0.03
        if gia > 100 :
            self.kq = ((50*100) + (50*150) + (gia - 100) * 200) + ((50*100) + (50*150) + (gia - 100) * 200)*0.05

a = []
t = int(input()) 
for i in range(t):
    id = "KH{:02d}".format(i + 1)
    ten = input()
    cu = int(input())
    moi = int(input())
    gia = moi - cu
    a.append(hoadon(ten,id,gia))
a.sort(key = lambda i : -i.kq)
for i in a :
    print("{} {} {}".format(i.id,i.ten,round(i.kq)))


# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612