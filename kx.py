#cau8
color=['Red','Green','White','Black','Pink','Yellow']
with open('cau8',"w")as myfile:
    for c in color:
        myfile.write("%s\n"%c)
content=open('cau8.txt')
print(content.read())

#tamgiac
print("Nhập vào độ dài canh đáy tam giác")
a = int(input())
print("Nhập vào chiều cao tam giác")
h = int(input())
s = float(a * h * 1) / 2
print("Diện tích tam giác là")
print(s
