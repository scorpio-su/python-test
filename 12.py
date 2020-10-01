a,b=list(map(int,input().replace('\n','').split(' ')))
print('{0}+{1}={2}\n{0}*{1}={4}\n{0}-{1}={3}\n{0}/{1}={5}...{6}'.format(a,b,a+b,a-b,a*b,a//b,a%b))