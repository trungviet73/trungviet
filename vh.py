#bai 1
input_file=open ('D:/a.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[l-1]
        l=l-1
    print (s)
input_file.close()

#bai 2
k=open(('D:/a.txt','r')
char,wc,lc=0,0,0
for line in k:
    for k in range(0,len(line)):
        char +=1
       if(line[k]==''):
            wc+=1
       if(line[k]=='n'):
            wc,lc=wc+1,lc+1
print("the no.of chars is %d\n the no.of words is %d\n the no.of line is %d"%(char,wc,lc))

# bai 4
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f,nlines):
                       print(line)
file_read_from_head('test.txt',2)
#bai5
def file_read(fname):
         from itertools import islice
         with open(fname, 'w') as myfile:
                 myfile.write("Python Exercises\n")
                 myfile.write("Java Exercises")
         txt = open(fname)
         print(txt.read())
file_read('abc.txt')
#bai6
import sys
import os
def def file_read_from_tail(fname,lines):
        bufsiez = 8192
        fsize =os.stat(fname).st_size:
        inter = 0
       with open (fname) as f:
               if bufsize > fsize:
                       bufsize = fsize-1
                       data= []
                       while True
                               iter +=1
                               f.seek(fsize-bufsize*iter)
                               data.extend(f.readline())
                               if len(data) >= lines or f.tell() == 0:
                                       print (''.join(data[-lines:]))
                                       break
    file_read_from_tail('test.txt',2)

    #bai7
       
