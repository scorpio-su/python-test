s=str(input())
s1=''
for i in s: s1+=str((int(i)+7)%10)
print(s1[2],s1[3],s1[0],s1[1],sep='')