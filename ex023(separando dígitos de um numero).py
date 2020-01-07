num = int(input('digite um número de 0 a 9999:'))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('Milhar:{}'.format(m))
print('Centena:{}'.format(c))
print('Dezena:{}'.format(d))
print('Unidade:{}'.format(u))
