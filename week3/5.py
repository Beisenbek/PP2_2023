def myfunc(n):
  return lambda a : a * n

m2 = myfunc(2)
m3 = myfunc(3)
m4 = myfunc(4)

print(m2(11))
print(m3(11))
print(m4(11))
print(myfunc(5)(11))