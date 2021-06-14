from . import *

class Add:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  def is_reducible(self):
    return True
  def reduce(self, environment):
    if self.left.is_reducible():
      return Add(self.left.reduce(environment), self.right)
    elif self.right.is_reducible():
      return Add(self.left, self.right.reduce(environment))
    else:
      return Number(self.left.value + self.right.value)
  def evaluate(self, environment):
    return Number(self.left.evaluate(environment).value + self.right.evaluate(environment).value)
  def __str__(self):
    return '{} + {}'.format(self.left, self.right)
  def __repr__(self):
    return '<<{} + {}>>'.format(self.left, self.right)
