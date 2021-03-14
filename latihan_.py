from rumus_rumus.rumus_geometry import luas_segitiga

print('heloo my boy')

menu = ['ubi', 'jagung', 'padi', 'kentang']
print(menu)
print(f'menu')
print(f'{menu}')
index = 0

#FAIL CODE print({menu})
#FAIL CODE print(menu.__dict__)
for m in menu:
    print(f'{m}')
print()
print(menu[1])
print(menu[0], menu[1], menu[2], menu[3])
print()
for m in range (0, len(menu)):
    print(f'{m+1} {menu[m]}')
#FAIL CODE menu_makanan = ['nasi goreng', 'gado-gado', 'pete', 'lemper', 'bakso']
#FAIL CODE print(len(menu_makanan))

print()
palawija = ['singkong', 'jagung', 'kentang']
for i in palawija:
    print(i, end = ' ')
res = '\n'.join([str(item) for item in palawija])
res2 = '\n'.join(map(str, palawija))
print()
print(res)
print()
print(res2)

jumlah_anak = 8
for x in range (1, jumlah_anak):
    print(f'hellow {x}')

anak = ['joni', 'budi', 'indra']
for t in range (0, len(anak)):
    print(f'{t+1}. {anak[t]}')
print()
menu = ['bakso', 'sate', 'soto']
for makan in range (0, len(menu)):
    print(f'{makan +1}. {menu[makan]}')
print()
pakaian = ['baju', 'celana', 'syal']
for cloth in range (0, len(pakaian)):
    print(f'{cloth+1}. {pakaian[cloth]}')
print()

#data :
#strength : ragnar    health : 2000
#strength : chaos       health : 1500
#strength : barathrun   health : 1700

print('Hero Strength Dota')
hero_strength_dota = {
    'dota' : 'sentinel',
    'list_hero': [{'strength' : 'ragnar', 'health': 2000},
                  {'strength' :'chaos', 'health' : 1500},
                  {'strength' : 'barrathrun', 'health' : 1700}]}
print(f'{hero_strength_dota}')
print()
print(f"{hero_strength_dota['list_hero'][0]}")
print(f"{hero_strength_dota['list_hero'][1]['strength']}")
print(f"{hero_strength_dota['list_hero'][1] ['health']}")
print(f"strength : {hero_strength_dota['list_hero'][1]['strength']} "
      f"\nhealth : {hero_strength_dota['list_hero'][1] ['health']} "
      f"\nstrength : {hero_strength_dota['list_hero'][0]['strength']} "
      f"\nhealth : {hero_strength_dota['list_hero'][0]['health']} "
      f"\nstrength : {hero_strength_dota['list_hero'][2]['strength']} "
      f"\nhealth : {hero_strength_dota['list_hero'][2]['health']}")
print()
#menghitung luas segitiga
#panjang = 5
#tinggi = 10
#luas segitiga = panjang * tinggi / 2

#def luas_segitiga(panjang, tinggi):
    #rumus_luas_segitiga = panjang * tinggi / 2
    #return rumus_luas_segitiga
#luas_segitiga(5,10)
#print(luas_segitiga(5,10))
#print('luas segitiganya adalah ', luas_segitiga(5,10))
print()

#def luas_persegi(panjang, lebar):
 #   rumus_persegi = panjang * lebar
 #   return rumus_persegi
#luas_persegi(6,3)
#print(luas_persegi(6,3))
#print('luas persegi panjang adalah ', luas_persegi(10, 6))
print(luas_segitiga(6,3))
print()
from rumus_rumus.rumus_geometry import luas_persegi
print(luas_persegi(8,8))