a=['thousand','hundred','ten','dollar'] 

ans=''
num=str(input())
n=0
n1=len(num)
if n1 == 4: n=0
elif n1 == 3: n=1
elif n1 == 2: n=2
else: n=3

for i in range(len(num)):
    ans+=num[i]+' '+a[i+n]+' '
print(ans)

