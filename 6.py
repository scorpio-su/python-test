s=str(input())
for i in s:
    if str.isalpha(i):
        print(i,end='')
    else:
        print()