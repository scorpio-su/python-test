import math as m

x,y=list(map(int,input().replace('\n','').split(' ')))
c=m.sqrt(x*x+y*y)
if c <=100:
    print('inside')
else:
    print('outside')