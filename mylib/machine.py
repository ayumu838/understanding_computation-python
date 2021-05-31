from mylib import *

class Machine:
  def __init__(self, expression):
    self.expression = expression
  def step(self):
    self.expression = self.expression.reduce()
  def run(self):
    while(self.expression.is_reducible()):
      print(self.expression)
      self.step()
    print(self.expression)
