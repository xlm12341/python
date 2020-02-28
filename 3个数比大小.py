a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
c = int(input('Enter the third number'))

if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
if a < b:
    a, b = b, a
if a != b and b != c:
    print('The largest number is {}'.format(a))
elif a == b:
    print('Have the same number:{}'.format(a))
else:
    print('Have the same number:{}'.format(b))
