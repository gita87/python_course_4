red_pill = False

if red_pill:
    print('awakenned')
else:
    print('keep sleeping')

jumlah_anak = 10

for jumlah_anak in range(0, 11):
    print(f'halo {jumlah_anak}')
print()
nama = ['adi', 'beby', 'charlie', 'delta']
print(f'yaba daba dooooo {nama[2]}')
for item in nama:
    print(f'{item}')
print()
for i in range(1, 11):
    print(i)
print()
menu = ['bakwan', 'tempe', 'ubi']
for item in menu:
    for i in range (1, 4) :
        print (f'{i} {item}')
print()
for i in range (0, len(menu)) :
    print(f'{i+1}. {menu[i]}')

print()
a = ['b']
c = ['d']
e = [a,c]
print(f"{e}")

a= ['b', 'd']
print(f'{a}')
for item in a :
    print(item)

a = ('b', 'c', 'd', 'e')
print(f'{a}')
print()
a = 1, 2, 3, 4
print(f'[a]')
print()
print(f"{a}")
print()
print(f'{a} {a}')
print()
print(a)
for item in a:
    print(f'{item}')
a = 123
print(a)
x = [1, 2, 3]
print(x)
print(f'{x}')
print()
for x in (1, 2, 3):
    print(x, end = '')
# FAIL CODE for x in (1, 2, 3)
    print("x, end = '' ")
print()
for x in (1, 2, 3):
    print(x, end = '')
