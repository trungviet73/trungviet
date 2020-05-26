#bai1
## File: mymath.py ##
def square(n):
    return n*n
def cube(n):
    return n*n
def average(values):
    nvals=len(values)
    sum=0.0
    for v in values:
        sum += v
    return float(sum)/nvals

# use 'import'
## My script using the math module ##
import mymath   # note no .py

values=[2,4,6,8,10]
print('Squares: ')
for v in values:
    print(mymath.square(v))
print('Cubes:')
for v in values:
    print(mymath.cube(v))
print('Average: '+ str( mymath.average(values)))


# import module as new-name
import mymath as mt
print(mt.square(2))
print(mt.square(3))

#bai2
import datetime as dt
format= '%Y-%m-%dT%H:%M:%S'
t1= dt.datetime.strptime('2008-10-12T14:45:52',format)
print('Day'+str(t1.day))
print('Day'+str(t1.day))
print('Month'+str(t1.month))
print('Minute'+str(t1.minute))
print('Second'+ str(t1.second))

# Define todays date and time
t2=dt.datetime.now()
diff=t2-t1
print('How many days difference? '+ str(diff.days))

#bai3
import numpy as np
x= np.arange(12,38)
print(x)

#bai4
a=[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
a=a[::-1]
print(a)

#bai5
lst = []
num = int(input('Co bao nhieu gia tri: '))
for n in range(num):
    gia_tri = input('Nhap gia tri: ')
    lst.append(gia_tri)
    print(lst)
print("Phan tu lon nhat :", max(lst))


#bai7
import numpy as np
data_type =[('name','S15'),('class','int'),('height',float)]
students_details=[('Jame',5,48.5),('Nail',6,52.5),('Paul',5,42.10),('Pit',5,40.1)]
# create a structured array
students=np.array(students_details, dtype=data_type)
print('Original array: ')
print(students)
print(" Sort by height ")
print(np.sort(students, order='height'))


