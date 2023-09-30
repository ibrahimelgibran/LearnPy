# perulangan incerment
for i in range(1, 101, 2):
    print(f'ke-{i}: saya tidak akan mengulangi perbuatan ini lagi.')

# perulangan decrement
for i in range(100, 0, -1):
    print(i)

# perulangan kondisional
for i in range(1,100):
    print(i)
    if( i % 10) == 0:
        print(50 * "=")

# menghilangkan faktor 3
for i in range(0, 101):
    if (i % 3) !=0:
      print(i)

#praktek 1
for i in range(0,5):
  for j in range(0,5):
    print('i:',i, 'j:',j, '', end='')
  print()

#praktek 2
for i in range(0,5):
  for j in range(0,5):
    if i <= j:
      print('*', end='')
    else:
      print('', end='')
  print()

#praktek 3
def hello():
  print("hello world!")
def tambah(a, b):
      return a+b;

h = tambah(5, 7)
X = hello()

#praktek 4
def hasil_bagi(a=4, b=3):
  return a%b

x = hasil_bagi(b=2,a=4)
print(x)

#praktek 5
def fToC(f):
  c = (f - 32) * 5/9
  return c

h = fToC(212)
print(h)

#praktek 6
def counter(star=0, step=1):
  x = [star]
  def _inc():
      x[0] += step
      return x[0]
  return _inc
  
c1 = counter()
c2 = counter(100, -10)
a = c1()
b = c2()
print(a)
print(b)

# kotak bintang
def kontak(p, l):
    for i in range(l):
        for j in range(p):
         print('*', end='')
        print()

kontak(5, 4)
        
# lebih mudah pakai for loop
for x in range(0, 10):
   for y in range(0, 10):
        if x == y or (x + y) == 9:
            print('@', end='')
        else:
            print('*', end='')
   print()

# percobaan pakai while seperti diatas ini
x = 0
while x < 10:
   y = 0
   while y < 10:
        if x == y or (x + y) == 9:
            print('@', end='')
        else:
            print('*', end='')
        y+=1
   print()
x+=1
# BENCI BANGET SAMA WHILE FULL LOOPING GA BERHENTI-HENTI