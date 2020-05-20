#bai4.2
ds=input('nhap chuoi:').split()
x=ds[0:-1]
ds.append('abc')
for ch in ds:    
     print(ch)

#bai4.20
s=input(' Nhap chuoi: ')
print(s)

#bai4.21
ds=input("Nhap chuoi: ").split()

#bai4.22
ds=input('nhap chuoi:').split()
x=ds[0:2]
ds.remove('123')
print(ds)

#bai4.3
s=input(" Nhap chuoi: ")
for ch in s.split():
    print(ch)

#bai4
value = []
items=[x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)
print (','.join(value))
