from z3 import *

X = [ [ Bool ("x_%s_%s" % (i+1, j+1))  for j in range (3) ] for i in range(3)  ]

######################
# valid assignments
######################

# every person is seated
val_c1 = []
for i in range(3):
    c = False
    for j in range(3):
        c = Or (c, X[i][j])
    val_c1.append (c)

# every seat is occupied
val_c2 = []
for j in range(3):
    c = False
    for i in range(3):
        c = Or (c, X[i][j])
    val_c2.append (c)

# one person per seat
val_c3 = []
for i in range(3):
    for j in range(3):
        c = True
        for k in range(3):
            if k != j:
                c = And(c, X[i][k] == False)
        val_c3.append (Implies (X[i][j] == True, c))

valid = val_c1 + val_c2 + val_c3

######################
# problem constraints
######################

# A does not want to sit next to C
c1 = [ Implies (X[0][0] == True, X[2][1] == False), 
       Implies (X[0][1] == True, And (X[2][0] == False, X[2][2] == False)),
       Implies (X[0][2] == True, X[2][1] == False) ]

# A does not want to sit in the left chair
c2 = [X[0][0] == False]

# B does not want to sit to the right of C
c3 = [ Implies (X[2][0] == True, X[1][1] == False),
       Implies (X[2][1] == True, X[1][2] == False) ]

c = c1 + c2 + c3

print (X)
print (val_c1)
print (val_c2)
print (val_c3)
solve (valid + c)
