from . import *

class Machine:
  def __init__(self, statement, environment):
    self.statement = statement
    self.environment = environment
  def step(self):
    self.statement, self.environment = self.statement.reduce(self.environment)
  def run(self):
    while(self.statement.is_reducible()):
      print("{}, {}".format(self.statement, self.environment))
      self.step()
    print("{}, {}".format(self.statement, self.environment))
