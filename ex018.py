import math
an = float(input('digite um angulo: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print('O angulo {} tem o SENO de {}\nO COSSENO de {}\nA TANGENTE de {} '.format(an, se, co, ta))