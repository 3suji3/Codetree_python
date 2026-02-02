num = 0;
N = int(input())

for i in range(1, N+1):
    if i%2!=0 and i%3!=0 and i%5!=0:
        num +=1
    else:
        continue

print(num)