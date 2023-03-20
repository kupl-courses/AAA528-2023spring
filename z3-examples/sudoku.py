from z3 import *

X = [ [ Int ("x_%s_%s" % (i+1,j+1)) for j in range(9) ] for i in range(9) ]

# each cell contains a value in {0,...,9}
cells_c = []
for i in range(9):
    for j in range(9):
        cells_c.append (And (1 <= X[i][j], X[i][j] <= 9))

# each row contains a digit at most once
rows_c = []
for i in range(9):
    for j in range(9):
        for k in range(9):
            rows_c.append (Implies (j!=k, X[i][j]!=X[i][k]))

# each column contains a digit at most once
cols_c = []
for j in range(9):
    for i in range(9):
        for k in range(9):
            cols_c.append (Implies (i!=k, X[i][j]!=X[k][j]))

# each 3x3 square contains a digit at most once
sq_c = []
for i0 in range(3):
    for j0 in range(3):
        for i in range(3):
            for j in range(3):
                for i2 in range(3):
                    for j2 in range(3):
                        sq_c.append (Implies (Or (i!=i2, j!=j2), X[3*i0+i][3*j0+j] != X[3*i0+i2][3*j0+j2]))


c = cells_c + rows_c +cols_c + sq_c

# sudoku instance, we use '0' for empty cells
# easy hard
instance1 = ((5,9,0,1,0,0,6,4,0),
            (0,0,0,9,4,5,0,0,2),
            (0,4,0,0,6,0,9,7,5),
            (0,2,0,3,5,8,0,6,0),
            (0,8,0,0,0,0,0,2,0),
            (0,3,0,2,7,6,0,8,0),
            (6,7,9,0,2,0,0,3,0),
            (2,0,0,6,8,1,0,0,0),
            (0,1,8,0,0,3,0,5,6))

# expert-level
instance2= ((0,8,2,0,0,5,0,0,0),
            (0,0,0,6,0,0,2,0,0),
            (6,0,0,0,0,1,0,0,0),
            (5,0,0,0,0,0,0,0,0),
            (0,0,0,4,0,2,0,0,0),
            (0,0,0,0,0,0,0,0,6),
            (0,0,0,8,0,0,0,0,5),
            (0,0,8,0,0,9,0,0,0),
            (0,0,0,5,0,0,4,3,0))

# evil-level
instance3= ((0,0,0,0,0,4,0,1,9),
            (0,0,7,0,0,3,0,0,8),
            (0,0,0,0,0,2,0,4,5),
            (8,0,0,0,0,0,4,0,0),
            (0,1,6,0,0,0,5,3,0),
            (0,0,5,0,0,0,0,0,7),
            (7,2,0,4,0,0,0,0,0),
            (5,0,0,6,0,0,8,0,0),
            (3,6,0,7,0,0,0,0,0))


instance = instance3

instance_c = [ If(instance[i][j] == 0,
                  True,
                  X[i][j] == instance[i][j])
               for i in range(9) for j in range(9) ]

s = Solver()
s.add (c + instance_c)
if s.check() == sat:
    m = s.model ()
    r = [ [ m.evaluate (X[i][j]) for j in range(9) ] for i in range(9) ]
    print_matrix (r)
else:
    print ("failed to solve")
