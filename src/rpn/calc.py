class RpnCalculator:
  '''
  Maintain internal state of an RPN calculator
  '''

  def __init__(self):
    self.stack = []

  def peek(self, n):
    '''
    Return the nth value on the stack
    '''
    if n >= len(self.stack):
      return None

    return self.stack[-n - 1]

  def push(self, v):
    '''
    Push a value onto the top of the stack
    '''
    self.stack.append(v)

  def pop(self):
    '''
    Return the value from the top of the stack
    '''
    return self.stack.pop()

  def exchange(self):
    '''
    Swap the top two values on the stack
    '''
    a = self.pop()
    b = self.pop()

    self.push(a)
    self.push(b)

  def add(self):
    '''
    Add the top two values on the stack
    '''
    a = self.pop()
    b = self.pop()

    self.push( b + a )

  def sub(self):
    '''
    Subtract the top value from the second value on the stack
    '''
    a = self.pop()
    b = self.pop()

    self.push( b - a )

  def mul(self):
    '''
    Multiply the top two values on the stack
    '''
    a = self.pop()
    b = self.pop()

    self.push( b * a )

  def div(self):
    '''
    Divide the top value into the second value on the stack
    '''
    a = self.pop()
    b = self.pop()

    self.push( b / a )

