h1,m1,h2,m2= list(map(int, input().replace('\n','').split(' ')))
m1+=h1*60
m2+=h2*60
sums=0
if m1<=m2: sums=m2-m1
else: sums=1440-m1+m2
sums//=30
#print(sums)
if sums<4: print(30*sums)
elif 4<=sums<8:print(40*(sums-4)+120)
else:print(60*(sums-8)+280)