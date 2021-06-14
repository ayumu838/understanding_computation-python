from mylib import *

# sequence
# Machine(
#   Sequence(
#     Assign('x', Add(Number(1), Number(1))),
#     Assign('y', Add(Variable('x'), Number(3)))
#   ),
#   {}
# ).run()


# while
# Machine(
#   While(
#     LessThan(Variable('x'), Number(5)),
#     Assign('x', Multiply(Variable('x'), Number(3)))
#   ),
#   {'x': Number(1)}
# ).run()

# big step
statement = Sequence(
  Assign('x', Add(Number(1), Number(1))),
  Assign('y', Add(Variable('x'), Number(3)))
)
print(statement)
statement.evaluate({})
print(statement.evaluate({}))



statement = While(
  LessThan(Variable('x'), Number(5)),
  Assign('x', Multiply(Variable('x'), Number(3)))
)

print(statement.evaluate({'x': Number(1)}))
