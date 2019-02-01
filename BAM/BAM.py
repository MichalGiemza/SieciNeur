import numpy as np

# Funkcje
def znajdz_obraz(n, W):
  return (W * n.transpose() > 0).transpose() * 1

def znajdz_nazwe(o, W):
  return (o * W > 0) * 1

def macierz_wag(O, N):
  W = np.matrix([[0 for x in range(N[0].size)] for y in range(O[0].size)])

  for i in range(len(O)):
    W = dodaj_do_macierzy(O[i], N[i], W)
  
  return W
  
def dodaj_do_macierzy(o, n, W):
  for i in range(o.size):
    for j in range(n.size):
      if o[0, i] == n[0, j]:
        W[i, j] += 1
      else:
        W[i, j] += -1
      j += 1
    i += 1
  return W


# Testy
def test_znajdowania_obrazu(n, W):
  print 'Test znajdowania obrazu na podstawie nazwy:'
  print n  
  
  i = 1
  n2 = n
  while True:
    o = znajdz_obraz(n2, W)
    n2 = znajdz_nazwe(o, W)

    if np.array_equal(n, n2):
      print ''
      print 'Obraz znaleziony po ' + str(i) + ' iteracjach.'
      print 'Znaleziony obraz: ' + str(o)
      break
    else:
      print ''
      print 'Obraz po ' + str(i) + ' iteracjach:'
      print 'Aktualna postac obrazu: ' + str(o)
      print 'Aktualna postac nazwy: ' + str(n2)
      
    i += 1

def test_znajdowania_nazwy(o, W):
  print 'Test znajdowania nazwy na podstawie obrazu:'
  print o  
  
  i = 1
  o2 = o
  while True:
    n = znajdz_nazwe(o2, W)
    o2 = znajdz_obraz(n, W)

    if np.array_equal(o, o2):
      print ''
      print 'Nazwa znaleziona po ' + str(i) + ' iteracjach.'
      print 'Znaleziona nazwa: ' + str(n)
      break
    else:
      print ''
      print 'Nazwa po ' + str(i) + ' iteracjach:'
      print 'Aktualna postac nazwy: ' + str(n)
      print 'Aktualna postac obrazu: ' + str(o2)
      
    i += 1

# Obrazy i nazwy do testow
O = [np.matrix([0, 1, 1, 1, 0, 1]), np.matrix([1, 0, 0, 1, 0, 0])]
N = [np.matrix([1, 1, 0, 0]), np.matrix([1, 0, 1, 0])]

# Testowanie
W = macierz_wag(O, N)

test_znajdowania_obrazu(N[0], W)
print ''
test_znajdowania_nazwy(O[0], W)
print ''
