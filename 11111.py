'''
Набор из пар чисел.
Из каждой пары ровно 1 число так, чтобы сумма выбранных чисел делилась на 3 и была максимальной

6
1 3   1 3
5 11  6 12 8 14
6 9   12 14 18 20 15 19 21 23
5 4
3 3
1 1
'''

f = open('27.txt')
n = int(f.readline())
for i in range(n):
    p = [int(x) for x in f.readline().split()]
    s = [a + b for a in s for b in p]