from z3 import *

def print_board (r):
  for i in range(8):
      for j in range(8):
          if r[i] == j+1:
              print (1, end="")
          else:
              print (0, end="")
      print ("")

Q = [ Int ("Q_%i" % (i+1)) for i in range(8) ]
val_c = [ And (1 <= Q[i], Q[i] <= 8) for i in range(8) ]
col_c = [ Implies (i != j, Q[i] != Q[j]) for i in range(8) for j in range(8) ]
diag_c = [ Implies (i != j, And (Q[i]-Q[j] != i-j, Q[i]-Q[j] != j-i)) for i in range(8) for j in range(i) ]
 
solutions = []
b = True
num_of_sols = 0

while b:
  diff_c = []
  for sol in solutions:
    c = True
    for i in range(8):
      c = And(c, sol[i] == Q[i])
    diff_c.append (Not(c))
  s = Solver()
  s.add (val_c + col_c + diag_c + diff_c)
  res = s.check()
  if res == sat:
     num_of_sols = num_of_sols + 1
     m = s.model ()
     r = [ m.evaluate (Q[i]) for i in range(8) ]
     print_board (r)
     print ("")
     solutions.append (r)
  else:
     if res == unsat:
        print ("no more solutions")
     else:
        print ("failed to solve")
     b = False

print ("Number of solutions : " + str(num_of_sols))
