from . import *

class DoNothing:
  def evaluate(environment):
    return environment
  def to_s(self):
    return 'do-nothing'
  def is_reducible(self):
    return False
  def __str__(self):
    return self.to_s()
  def __repr__(self):
    return '<<{}>>'.format(self)
  def __eq__(self, other_statement):
    return isinstance(other_statement, DoNothing)
