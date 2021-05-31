class Number:
  def __init__(self, value):
    self.value = value
  def to_s(self):
    return '{}'.format(self.value)
  def __str__(self):
    return self.to_s()
  def __repr__(self):
    return '<<{}>>'.format(self.value)

class Add:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  def __str__(self):
    return '{} + {}'.format(self.left, self.right)
  def __repr__(self):
    return '<<{} + {}>>'.format(self.left, self.right)

class Multiply:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  def __str__(self):
    return '{} * {}'.format(self.left, self.right)
  def __repr__(self):
    return '<<{} * {}>>'.format(self.left, self.right)

a = Add(
  Add(Number(1), Number(2)),
  Multiply(Number(3), Number(4))
)

b = Multiply(
  Number(1),
  Multiply(
    Add(Number(2), Number(3)),
    Number(4)
  )
)
