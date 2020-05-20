#bai1
s=input(" Nhap chuoi: ")
for ch in s:
    print(ch)

#bai4.10
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        values.append(s)
x=','.join(values)
print(x)

#bai4.11
s = input("Nhập chuoi: ")
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("Số chữ số là:", d["DIGITS"])
print ("Số chữ cái là:", d["LETTERS"])

#bai4.12
s = input("Nhập câu của bạn: ")
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("Chữ hoa:", d["UPPER CASE"])
print ("Chữ thường:", d["LOWER CASE"])

#bafi4.13
values = input("Nhập dãy số của bạn, cách nhau bởi dấu phẩy: ")
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))

#bai4.14
import sys
netAmount = 0
while True:
    s = input("Nhập nhật ký giao dịch: ")
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
         netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print (netAmount)

#bai4.15
s=input(" Nhap chuoi: ")
for ch in s.upper():
    print(ch)

#bai4.16
ds=input(' Danh sách: ').split()
#in cả dãy vừa nhập
print(ds)
# in dãy vừa nhập, mỗi phần tử trên một dòng
for so in ds:
    print(so)

#bai4.17
ds=input(' Danh sách: ').split()
#in cả dãy vừa nhập
print(ds)
# in dãy vừa nhập, mỗi phần tử trên một dòng và đảo ngược lí thuyết
for so in ds.__reversed__():
    print(so)

#bai4.18
name=input('Xin moi nhap ho va ten: ')
ho=name.split()[0]
print('Ho cua ban la:',ho)
ten=name.split()[1]
print('Ten cua ban la: ',ten)

#bai4.19
s=input(' Nhap chuoi: ')
chuoi_moi = ''.join(i for i in s if not i.isdigit())
print('Chuoi moi se la: ',chuoi_moi)
