#bai5.6
import numpy as np
data_type= [('name','S15'),('class',int),('height',float)]
students_details=[('James',5,48.5),('Nail',6,5.25),('Paul',5,42.10),('Pit',5,40.11)]
#create a structured array
students=np.array(students_details,dtype=data_type)
print("Original array:")
data_type =[('name','S15'),('class','int'),('height',float)]
students_details=[('Jame',5,48.5),('Nail',6,52.5),('Paul',5,42.10),('Pit',5,40.1)]
# create a structured array
students=np.array(students_details, dtype=data_type)
print('Original array: ')
print(students)
print("Sort by height")
print(np.sort(students,order='height'))
print(" Sort by height ")
print(np.sort(students, order='height'))

#bai5.8
def Sequential_Search(arr, n, x):
    for i in range(n):
        if (arr[i] == x):
            return i
    return -1

arr=[]
n =int(input('Co bao nhieu item: '))
for k in range(n):
    item=input('Nhap item: ')
    arr.append(item)
x =input('Nhap vao item can tim: ')
n= len(arr)
result = Sequential_Search(arr, n, x)
if (result == -1):
    print("Phan tu khong co trong mang")
else:
    print("Phan tu co trong mang", 'va co vi tri:',result)
