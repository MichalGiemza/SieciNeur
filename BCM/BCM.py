import numpy as np

def buduj_macierz(x, W):
  W += x.transpose() * x
  return (W > 0) * 1

def czy_znany(x, W):
  t = np.matrix([0 for i in range(x.size)])

  for i in range(x.size):
    if x[0,i] > 0:
      for k in range(x.size):
        if W[k,i] > 0:
          t[0,i] += 1;
  
  t -= 1;
  t = (t > 0) * 1

  return np.array_equal(t, x)
        

X = [np.matrix([1, 1, 0, 0, 0, 0]), np.matrix([0, 1, 0, 0, 0, 1])]
W = np.matrix([[0 for x in range(X[0].size)] for y in range(X[0].size)])

for x in X:
  W = buduj_macierz(x, W)

print W
print ""

print "Czy wektor ", X[1], " jest znany?"
print czy_znany(X[1], W)
print ""

print "Czy wektor ", X[0], " jest znany?"
print czy_znany(X[0], W)
print ""

v = np.matrix([0, 1, 0, 1, 0, 0])
print "Czy wektor ", v, " jest znany?"
print czy_znany(v, W)
print ""