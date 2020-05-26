#bai1
lớp  Cricle ( đối tượng ):
    def  __init__ ( tự , r ):
        tự . r = r
     khu vực def ( tự ):
         tự trở về . r ** 2 * 3.14
r = int ( đầu vào ( "nhap ban kinh:" ))
c = Cricle ( r )
in ( "dien tich hinh tron ​​la:" , c . area ())

#bai2
lớp  hinhchunhat ( đối tượng ):
    def  __init__ ( tự , a , b ):
        tự . a = a
        tự . b = b
    def  dien_tich ( tự ):

#bai3
lớp  Nguoi ( đối tượng ):
    def  getGender ( tự ):
        trả lại  "Unkn"

lớp  Nam ( Nguoi ):
    def  getGender ( tự ):
        trả lại  "Nam"
lớp  Nu ( Nguoi ):
    def  getGender ( tự ):
        trả lại  "Nu"
    
a  Nam =  Nam ()
aNu  =  Nu ()
in ( a Nam . getGender ())
in ( aNu . getGender ())

#bai7
lớp  Cricle ( đối tượng ):
    def  __init__ ( tự , r ):
        tự . r = r
    def  chu_vi ( tự ):
        trả lại  2 * tự . r * 3,14
    def  dien_tich ( tự ):
         tự trở về . r ** 2 * 3.14
r = int ( đầu vào ( "nhap ban kinh:" ))
c = Cricle ( r )
in ( "chu vi hinh tron ​​la:" , c . chu_vi ())
in ( "dien tich hinh tron ​​la:" , c . dien_tich ())

