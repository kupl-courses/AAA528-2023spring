from z3 import *

def print_board (r):
  for i in range(8):
      for j in range(8):
          if r[i] == j+1:
              print (1, end=""),
          else:
              print (0, end=""),
      print ("")

Q = [ Int ("Q_%i" % (i+1)) for i in range(8) ]
  
val_c = [ And (1 <= Q[i], Q[i] <= 8) for i in range(8) ]
col_c = [ Implies (i != j, Q[i] != Q[j]) for i in range(8) for j in range(8) ]
diag_c = [ Implies (i != j, And (Q[i]-Q[j] != i-j, Q[i]-Q[j] != j-i)) for i in range(8) for j in range(i) ]

s = Solver()
s.add (val_c + col_c + diag_c) 
res = s.check()
if res == sat:
   m = s.model ()
   r = [ m.evaluate (Q[i]) for i in range(8) ]
   print_board (r)
   print ("")
