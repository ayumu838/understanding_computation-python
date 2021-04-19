class Number:
  def __init__(self, value):
    self.value = value

class Add:
  def __init__(self, left, right):
    self.left = left
    self.right = right

class Multiply(Struct):
  def __init__(self, left, right):
    self.left = left
    self.right = right

a = Add(
  Multiply(Number(1), Number(2)),
  Multiply(Number(3), Number(4))
)
