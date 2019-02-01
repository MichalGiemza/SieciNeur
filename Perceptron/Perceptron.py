import random
import numpy as np

# Perceptron

def wczytaj(plik):
  d = []

  f = open(plik, 'r')
  c = f.read();
  f.close();

  c = c.strip().split('\n')

  for l in c:
    k = []
    l = l.strip().split('\t')
    for x in l:
      k.append(float(x))
    d.append(k)
  return d

def obl_klase(W, X):
  suma = 0.0
  for i in range(4):
    suma += W[0, i] * X[0, i] + b
  return suma / abs(suma)

def trening(tr, st_ucz, b, Max_iter):
  # 0
  W = np.matrix([random.random() * 0.4 - 0.2 for x in range(4)])
  W_kiesz = []
  b_kiesz = 0
  wiek = 0
  wiek_kiesz = 0

  while wiek_kiesz < Max_iter:
    # 1
    X = random.choice(tr)
    C = X[4]
    X = np.matrix([X[0], X[1], X[2], X[3]])
  
    # 2
    klasa = obl_klase(W, X)

    # 3
    if klasa == C:
      # a)
      wiek += 1

      if (wiek > wiek_kiesz):
        wiek_kiesz = wiek
        W_kiesz = W
        b_kiesz = b

    else:
      # b)
      W += st_ucz * C * X
      b += st_ucz * C
    
  return W_kiesz

def test(te, W):
  wyniki = []
  for x in te:
    C = x[4]
    X = np.matrix([x[0], x[1], x[2], x[3]])
  
    klasa = obl_klase(W, X)
  
    wynik = True
    if (klasa == C):
      wynik = True
    else:
      wynik = False

    wyniki.append(wynik)

  suma = 0
  for x in wyniki:
    if (x == True):
      suma += 1

  return float(suma) / len(wyniki)

# Program
st_ucz = 0.3
b = 1
Max_iter = 3000

dane = []
dane.append(["A", wczytaj("iris_2vs3_A_tr.txt"), wczytaj("iris_2vs3_A_te.txt")])
dane.append(["B", wczytaj("iris_2vs3_B_tr.txt"), wczytaj("iris_2vs3_B_te.txt")])
dane.append(["C", wczytaj("iris_2vs3_C_tr.txt"), wczytaj("iris_2vs3_C_te.txt")])
dane.append(["D", wczytaj("iris_2vs3_D_tr.txt"), wczytaj("iris_2vs3_D_te.txt")])
dane.append(["E", wczytaj("iris_2vs3_E_tr.txt"), wczytaj("iris_2vs3_E_te.txt")])

for t in dane:
  W = trening(t[1], st_ucz, b, Max_iter)
  wynik = test(t[2], W)

  print "Test dla zbioru " + t[0]
  print "Poprawnosc: " + str(wynik * 100) + "%"
  print ""