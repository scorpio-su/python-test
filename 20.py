tot,a,b,c=list(map(int,input().replace('\n','').split(' ')))
tot-=a*15+b*20+c*30
if tot < 0:
    print('0')
else:
    a=tot//50
    b=(tot-a*50)//5
    tot-=a*50+b*5
    print(a,b,tot)