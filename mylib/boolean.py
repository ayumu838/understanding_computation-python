from . import *

class Boolean:
  def __init__(self, value):
    self.value = value
  def evaluate(environment):
    return self
  def to_s(self):
    return '{}'.format(self.value)
  def is_reducible(self):
    return False
  def __str__(self):
    return self.to_s()
  def __repr__(self):
    return '<<{}>>'.format(self.value)
  def __eq__(self, other):
    return self.to_s() == other.to_s()
