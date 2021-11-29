x = [[1,12,2],
     [4,5,12],
     [8,10,15]]
y = [[1,12,2],
     [4,5,12],
     [8,10,15]]
res = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(x)):
  for j in range(len(x[0])):
    res[i][j] = x[i][j] + y[i][j]
for r in res:
  print(r)
