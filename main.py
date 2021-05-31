from mylib import *

a = Add(Number(23), Add(Number(2), Number(3)))
print(a)
m1 = Machine(a)
m1.run()
