#bai1
imput_file=open('D:/a.txt','r')
for lne in input_file:
    l=len(line)
    s=''
    while(l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input_file.close()

#bai2
k=open('D:/k=opent(a.txt','r')
char,wc,lc=0,0,0
for line in k:
    for k in range(0,len(line)):
        char +=1
        if (line[k]==''):
            wc+=1
        if (line[k]=='\n'):
            wc,lc=wc+1,lc+1
print("The no.of chars is %d\n The no.of words is %d\n The no.of lines is %d"%(char,wc,lc))

#bai3
#bai4
def file_read_form_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)
        file_read_from_head('test.txt',2)
#bai5
import sys
import os
def file_read_from_tail(fname,line):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
            if bufize > fsize :
                bufsize = fsize-1
                data = []
                while True:
                    iter +=1
                    f.seek(fsize-bufsize*iler)
                    data.extend(f.readline())
                    if len(data) >= lines or f.tell() == 0:
                        print(''.join(data[-lines:]))
                        break
file_read_from_tall('test.txt',2)

#bai6
def file_read(fname):
    from itertools import islice
    with open(fname,"w") as mylice:
        myfile.write("python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())
file_read('abc.txt')
