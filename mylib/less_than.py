from . import *

class LessThan:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  def to_s(self):
    return '{} < {}'.format(self.left, self.right)
  def is_reducible(self):
    return True
  def reduce(self, environment):
    if self.left.is_reducible():
      return LessThan(self.left.reduce(environment), self.right)
    elif self.right.is_reducible():
      return LessThan(self.left, self.right.reduce(environment))
    else:
      return Boolean(self.left.value < self.right.value)
  def __str__(self):
    return self.to_s()
  def __repr__(self):
    return '<<{} < {}>>'.format(self.left, self.right)
