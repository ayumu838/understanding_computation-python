from . import *

class Sequence:
  def __init__(self, first, secound):
    self.first = first
    self.secound = secound
  def evaluate(self, environment):
    return self.secound.evaluate(self.first.evaluate(environment))
  def to_s(self):
    return '{}; {}'.format(self.first, self.secound)
  def is_reducible(self):
    return True
  def reduce(self, environment):
    if self.first == DoNothing():
      return [ self.secound, environment ]
    else:
      rediced_first, reduced_environment = self.first.reduce(environment)
      return [ Sequence(rediced_first, self.secound), reduced_environment]
  def __str__(self):
    return self.to_s()
  def __repr__(self):
    return '<<{}; {}>>'.format(self.to_s())
