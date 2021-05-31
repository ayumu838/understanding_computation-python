from mylib import *

class Add:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  def is_reducible(self):
    return True
  def reduce(self):
    if self.left.is_reducible():
      return Add(self.left.reduce(), self.right)
    elif self.right.is_reducible():
      return Add(self.left, self.right.reduce())
    else:
      return Number(self.left.value + self.right.value)
  def __str__(self):
    return '{} + {}'.format(self.left, self.right)
  def __repr__(self):
    return '<<{} + {}>>'.format(self.left, self.right)
