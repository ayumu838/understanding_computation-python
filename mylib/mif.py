from . import *

class If:
  def __init__(self, condition, consequence, alternative):
    self.condition = condition
    self.consequence = consequence
    self.alternative = alternative
  def is_reducible(self):
    return True
  def reduce(self, environment):
    if self.condition.is_reducible():
      return [If(self.condition.reduce(environment), self.consequence, self.alternative), environment]
    else:
      if self.condition == Boolean(True):
        return [self.consequence, environment]
      elif self.condition == Boolean(False):
        return [self.alternative, environment]
  def evaluate(self, environment):
    if self.condition.evaluate(environment) == Boolean(True):
      return self.consequence.evaluate(environment)
    elif self.condition.evaluate(environment) == Boolean(False):
      return self.alternative.evaluate(environment)
  def to_s(self):
    return 'if ({}) {{ {} }} else {{ {} }}'.format(self.condition, self.consequence, self.alternative)
  def __str__(self):
    return self.to_s()
  def __repr__(self):
    return '<<if ({}) {{ {} }} else {{ {} }}>>'.format(self.condition, self.consequence, self.alternative)
