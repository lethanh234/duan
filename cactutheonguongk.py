n = int(input())  
mp = {}  
for _ in range(n):
    s = input().lower()  
    word = ''
    for i in s : 
        if i.isalpha():  
            word += i  
        else:
            if word:  
                if word not in mp:  
                    mp[word] = 1
                else:  
                    mp[word] += 1
            word = ''  
v = []
for key, val in mp.items():
    if not key.isdigit(): 
        v.append((key, val))
v.sort(key=lambda i: (-i[1], i[0]))

for key, val in v:
    print(key, val)



# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.