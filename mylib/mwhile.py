from . import *

class While:
  def __init__(self, condition, body):
    self.condition = condition
    self.body = body
  def is_reducible(self):
    return True
  def reduce(self, environment):
    return [If( self.condition, Sequence(self.body, self), DoNothing()), environment]
  def evaluate(self, environment):
    if self.condition.evaluate(environment) == Boolean(True):
      return self.evaluate(self.body.evaluate(environment))
    elif self.condition.evaluate(environment) == Boolean(False):
      return environment
  def to_s(self):
    return 'while ({}) {{ {} }}'.format(self.condition, self.body)
  def __str__(self):
    return self.to_s()
  def __repr__(self):
    return '<<{}>>'.format(self.to_s())
