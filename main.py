x = 7 + 8  +\
    10 - 2;
print(x)

help("keywords");
print(1,2,3,4,5 , sep= " and ");
print(1,2,3,4,5 , end= " hi ");
# o = input("what is your name?");
# print("hi to " , o)
a = 20 ; b = 10; c = 3;
print( a , b , c, end=" ") ; print( a!=a)
print( a == a , end=" ") ;
print( a > a)
print(a + b )
print(a - b )
print(a * b )
print(a / b )
print(a // b )
print(a % b )
print(a ** c)
print(not a==a );
u =[1, 2 , 3];
w= [ 1 , 2 ,3];
print(3 not in u)
print(u is not w)
print( (d:=6) > 0 )
#exercise001------------------------
xx = 101 ; yy=202;
print("xx= " , xx); print("yy= " , yy)
xx,yy = yy, xx;
print("xx= " , xx); print("yy= " , yy)
#exercise002------------------------
aa= 8; bb= 3;
area = aa * bb;
print("This is the area" , area);
#exercise003------------------------
celsius = 30
fahrenheit = (celsius * 9 / 5) + 32
print("fahrenheit =", fahrenheit)
#exercise004------------------------
pi = 3.14 ; radius= 100;
circumference= 100 *2 *3.14;
area=radius**2 *pi;
print("areaALL = ",area); print("circumferenceALL= " ,circumference);
pox = 100.5
mox = 5 +8j
dox ={"ali" : "boy" }
pox = int(pox)
print(pox)
print(type(pox))
print(type(dox))
print(type(mox))
from  decimal import Decimal
print(Decimal ('0.6') + Decimal('0.3'))
import fractions
print(fractions.Fraction(0.75))
io= 1e+7
print(io)

