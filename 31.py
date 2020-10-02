a=list(map(int,input().replace('\n','').split(' ')))
sum2,sum1=a[0]*a[0]+a[1]*a[1],a[2]*a[2]
#print(sum1,sum2)
if sum2  == sum1:
    print('Right triangle')
elif sum2 > sum1:
    print('Acute triangle')
else:
    print('Obtuse triangle')