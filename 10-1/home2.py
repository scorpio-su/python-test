import math as m

x,y=list(map(int, input().replace('\n','').split(' ')))
c=m.sqrt(x**2+y**2)
if c>=100: 
    print('outside')    
else: 
    print('inside')
