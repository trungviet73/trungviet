#bai1
def sum(a, b):
    print("sum=" + str(a+b))
#tinh tong 2 so 4,5
sum(4,5)
#tinh tong 2 so 3,7
sum(3,7)

#bai2
def sum(a,b):
    return a+b
c=sum(4,5);
print("Tong cua 4 va 5 la:" + str(c))

#bai3
a="hello"
def say_hello(): 
    print(a)
print(a)

#bai4
a="Hello Guy!"
def say(a):
    a="Vinh University"
    print(a)
say(a)
print(a)

#bai5
a="Hello Guy!"
def say():
    global a
    a="Vinh University"
    print(a)
say()
print(a)

#bai6
def get_sum(*num):
    tmp=0
    #duyet cac tham so
    for i in num:
        tmp+=i
    return tmp
result=get_sum(1,2,3,4,5)
print(result)

#bai7
def checkValue(n):
    if n%2==0:
        print(" Đây là một số chẵn")
    else:
        print(" Đây là một số lẻ")
checkValue(6)

#bai8
import math
pos=[0,0]
while True:
    s=input()
    if not s:
        break
    movement= s.split(" ")
    direction=movement[0]
    steps=int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
############################
print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))

#bai9
"""Program make a simple calculator that can add, subtract, multiply and divide using functions"""
#This function adds two numbers
def aff(x,y):
    return x+y
#This function subtracts two numbers
def subtract(x,y):
    return x-y
#This function multiplies two numbers
def multiply(x,y):
    returnx*y
#This fuction divides two numbers
def divide(x,y):
    return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#Take input from the user
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if choice=='1':
    print(mum1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid input")

#bai10
import math
def Tinh(R):
   if R<0:
       print("Ban kinh khong nho hon 0")
       print("Ban nhap khong hop le")
   else:
       CV=2*R*math.pi
       DT=R*R*math.pi
       print("Chu vi la :",CV)
       print("Dien tich la :",DT)
 
print("-------Tinh Chu Vi, Dien Tich Hinh Tron---------")  
r=float(input("Nhap ban kinh hinh tron: "))
Tinh(r)

#bai11
def bai1(t,n,k):
 for i in range(k):
    n=n+n*t/100
    print("Tong so tien nhan duoc la:",n)
if __name__=="__main__":
 t=float(input("Nhap lai suat: "))
 n=float(input("Nhap so tien gui ban dau: "))
 k=int(input("Nhap so thang gui: "))
 bai1(t,n,k)
