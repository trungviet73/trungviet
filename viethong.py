 #bai1
  n1= int (input ("enter n1 value:  ))
  n2= int (input ("enter n2 value: ))
  if n1>n2
    print (" n1 is big ")
  else:
    print (" n2 is big ")

 #bai2
  import math;
  x1=int (input("Enter x1--->"))
  y1=int (input("Enter y1--->"))

  x2=int (input("Enter x2--->"))
  y2=int (input("Enter y2--->"))

  d1= ( x2 - x1 ) * ( x2- x1 );
  d1= ( y2 - y1 ) * ( y2- y1 );
  res = math.sqrt (d1+d2)
  print ("Distance between two points:",res);

 #bai3
  n=int (input("Enter a number--->"))
  if n%2==0:
        print ("EVEN Number");
  else
        print ("ODD Number");

 #bai4
 i=1;
 for j in range (2,10):
        print ("i:",i"j:",j);
        print (i,"/",j);
        print (i/j);

 #bai5
 n=int (input("Enter A Number--->"));
 while n>0:
     print (n);
     n = n - 1;

 #bai6
  j= []                
  for i in range (2000,3201):
      if (i%7==0) and (i%5!=0):
          j.append (str(i))
  print (','.join(i))

 #bai7
   n=int (input("Nhập vào một số:"))
   d=dict()
   for i in range (1,n+1):
       d[i]=i*i

   print (d)

 #bai8
  a, b = 1, 2
  total = 0
  print(a,end=" ")
  while (a <=4000000-1):
      if a % 2 == 0:
          total += a
      a, b = b, a+b
      print (a,end=" ")
  print(\ n sum of prime numbers term in fibonacci series:",total)

 #bai9

  #c1
  str =input("Enter a String:"))
  dict = {}
  for n in str:
      keys = dict.keys ()
      if n in keys:
           dict [n] += 1       
      else
            dict [n] = 1
  print (dict)

  #c2
  str =input("Enter a String:"))                
   dict = {}
  for i in str:
       dict [i] = str.count(i)
   print (dict)         
