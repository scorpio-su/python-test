a=list(map(int,input().replace('\n','').split(' ')))
if a[0]<=a[1] and a[1]<=a[2]:
    a.sort()
    #print(a)
    if a[0]+a[1]> a[2]:
        print('True')
    else:
        print('False')
else:
    print('False')


