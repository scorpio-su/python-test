toa,a,b,c= list(map(int, input().replace('\n','').split(' ')))
toa-=a*15+20*b+30*c
a,toa=toa//50,toa-(toa//50*50)
b,toa=toa//5,toa-(toa//5*5)
print(toa,b,a,sep='\n')