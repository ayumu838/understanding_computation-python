from . import *

class Assign:
  def __init__(self, name, expression):
    self.name = name
    self.expression = expression
  def is_reducible(self):
    return True
  def reduce(self, environment):
    if self.expression.is_reducible():
      return [Assign(self.name, self.expression.reduce(environment)), environment]
    else:
      return [DoNothing(), environment | {self.name : self.expression}]
  def evaluate(self, environment):
    return environment | {self.name : self.expression.evaluate(environment)}
  def to_s(self):
    return '{} = {}'.format(self.name, self.expression)
  def __str__(self):
    return self.to_s()
  def __repr__(self):
    return '<<{} = {}>>'.format(self.name, self.expression)
