n = int(input())
a = (i**2 for i in range(1, n+1))
print(a)
for i in a:
  print(i)