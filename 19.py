h,tes=list(map(int,input().replace('\n','').split(' ')))
if tes == 1:
    print(round((h-80)*0.7,1))
else:
    print(round(((h-70)*0.6),1))