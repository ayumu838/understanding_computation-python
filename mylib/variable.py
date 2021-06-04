from . import *

class Variable:
  def __init__(self, name):
    self.name = name
  def to_s(self):
    return '{}'.format(self.name)
  def is_reducible(self):
    return True
  def reduce(self, environment):
    return environment[self.name]
  def __str__(self):
    return self.to_s()
  def __repr__(self):
    return '<<{}>>'.format(self.name)
