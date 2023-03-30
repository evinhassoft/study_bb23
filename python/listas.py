aves = ['gaviota', 'pardal', 'galinha', 'ema']
x = input()
aves.insert(0, x)
print(aves.pop())
print(aves)
aves2 = aves.copy()
aves.sort()
aves.reverse()
print(aves)