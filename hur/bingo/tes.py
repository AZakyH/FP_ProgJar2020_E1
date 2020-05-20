matrix = []
duamatrix = [None, None]
if not matrix:
    for i in range(5):          # A for loop for row entries 
        a =[] 
        for j in range(5):      # A for loop for column entries 
            a.append(int(input())) 
        matrix.append(a)

for i in range(5): 
    for j in range(5): 
        print(matrix[i][j], end = " ") 
    print()

if not duamatrix[0]:
    duamatrix[0] = matrix
if not duamatrix[1]:
    duamatrix[1] = matrix
print(duamatrix)