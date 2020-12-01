p1 = float(input('largura da parede: '))
p2 = float(input('altura da parede: '))
area = p1 * p2
print('sua parede tem a dimensão de {}x{} e sua area é de {:.2f}m²'.format(p1, p2, area))
tinta = area / 2
print('logo você ira precisar de {}L de tinta'.format(tinta))