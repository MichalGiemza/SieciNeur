

x = 4
y = 5

N = x * y
hi = 0

def element(m, el):
  return m[el / y][el % x - 1]

def wypisz(X):
  for a in X:
    print a

def kopiuj(src):
  dst = [[0 for i in range(x)] for j in range(y)]
  for i in range(y):
    for j in range(x):
      dst = src
  return dst

def sgn(x):
  if x < 0:
    return -1
  return 1

def pole_wypadkowe(t, W, i):
  suma = 0
  for j in range(N):
    if i != j:
      suma += W[i][j] * element(t, j) + hi
  return suma

def odtworz(te):
  t = kopiuj(te)

  while True:
    t_poprz = kopiuj(t)

    for i in range(N):
        t[i / y][i % x - 1] = sgn(pole_wypadkowe(t_poprz, W, i))

    if t_poprz == t:
      break

  return t

tr = [[
  [1, 1, 1, 1],
  [-1, -1, -1, -1],
  [1, 1, 1, 1],
  [-1, -1, -1, -1],
  [1, 1, 1, 1]
  ],[
  [-1, 1, 1, -1],
  [-1, 1, 1, -1],
  [-1, 1, 1, -1],
  [-1, 1, 1, -1],
  [-1, 1, 1, -1]
  ]]

te1 = [
  [1, 1, 1, -1],
  [1, -1, 1, -1],
  [1, -1, -1, 1],
  [1, -1, -1, 1],
  [1, 1, 1, 1]
  ]

te2 = [
  [1, -1, -1, -1],
  [1, -1, -1, -1],
  [1, -1, 1, -1],
  [1, -1, -1, 1],
  [1, 1, -1, -1]
  ]

print "Trening:"
wypisz(tr[0])
print ""
wypisz(tr[1])
print "\n"

# Wyznaczanie wag
W = [[0 for i in range(N)] for j in range(N)]
for t in tr:
  # Suma
  for i in range(N):
      for j in range(N):
          W[i][j] += element(t, i) * element(t, j)
  # 1 / N
  W[i][j] /= N

# Test
t = odtworz(te1)
print "\nTest:"
wypisz(t)

t = odtworz(te2)
print "\nTest:"
wypisz(t)