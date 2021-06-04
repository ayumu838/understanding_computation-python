from . import *

class Machine:
  def __init__(self, expression, environment):
    self.expression = expression
    self.environment = environment
  def step(self):
    self.expression = self.expression.reduce(self.environment)
  def run(self):
    while(self.expression.is_reducible()):
      print(self.expression)
      self.step()
    print(self.expression)
