from z3 import *

a = Bool ("a")
b = Bool ("b")
f = Bool ("f")
g = Bool ("g")
h = Bool ("h")

f1 = Or (And (And (Not(a), Not(b)), h), And (Not (And (Not(a), Not(b))), (Or (And (Not(a),g), And (a,f)))))
f2 = Or (And (a,f), And (Not(a), Or (And(b,g), And(Not(b), h))))

solve (Not (f1==f2))
