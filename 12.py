'''for x in '0123456789ABCDEF':
    for y in '0123456789ABCDEF':
        t = int('8' + '3' + x + y, 16)
        r = int('3' + x + y + '8', 16)
        if t - r == int('45D8', 16):
            print(int('3' + x + y + '8', 16))'''
'''for n in range(5, 30):
    if (int('34', n) + int('43', n)) == int('110', n):
        print(n)'''
'''for n in range(10, 60):
    if 39 % n == 3:
        print(n)'''
'''for n in range(8, 30):
    if 57 % n == 1 and len(str(int('57', n))) == 3:
        print(n)'''
'''count = 0
for x in range(1, 32768):
    if bin(x)[2:].count('1')//bin(x+1)[2:].count('1') == 4:
        count += 1
print(count)'''

'''for x in range(1, 1500):
    print(5.6552734375 * x, x)'''

'''for x in range(3, 30):
    for y in range(8, 30):
        if (int('17', y) - int('2', y) * int('22', x)) == int('3', y):
            print(x, y)'''

