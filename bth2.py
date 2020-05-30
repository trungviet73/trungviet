#bai2.10
a='hi i am python programer'
b=a.split()
print (b)
c=' '.join(b)
print(c)

#bai2.11
l=[1, "python",4, 7]
k=['cse',2, 'guntur',8]
m=[ ]
m.append(l);
m.append(k);
print(m)
d={1:1, 2:k, 'combine_ list':m}
print(d)

#bai2.12
import re
value=[]
items=[x for x in input('nhap mat khau: ').split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.seach('[a-z]', p):
        continue
    elif not re.seach('[0-9]', p):
         continue
    elif not re.seach('[A-Z]', p):
        continue
    elif not re.seach('[$#@]', p):
        continue
    elif not re.seach('[\s]', p):
        continue
    else:
        pass
    value.append(p)
 print(','.join(value))
