a = 7
b = 4
c = 12
d = (a + c % b)
e = (c // a + b)
f = (a + c % b) * (c // a + b)
result = (a + c % b) * (c // a + b) - a ** 2

print(f'D {d}')
print(f'E {e}')
print(f'F {f}')

print(result)