a = list(input().split())
b = list(input().split())

if int(a[0]) > 18 or int(b[0]) > 18:
    if int(a[0]) > 18 and a[1] == 'M':
        print(1)
    elif int(b[0]) > 18 and b[1] == 'M':
        print(1)
else:
    print(0)