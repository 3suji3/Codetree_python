s = input()

lst = list(s)
lst[1] = 'a'
lst[-2] = 'a'

s = ''.join(lst)
print(s)