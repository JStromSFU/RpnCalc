import pytest

from rpn.calc import RpnCalculator

def test_empty():
  '''
  New calculator has an empty stack
  '''
  rpn = RpnCalculator()
  assert rpn.peek(0) is None

def test_push():
  '''
  Pushed values is at the top of the stack
  '''
  rpn = RpnCalculator()
  rpn.push(1)
  assert rpn.peek(0) == 1

def test_push_multiple():
  '''
  Pushed values are FILO
  '''
  rpn = RpnCalculator()
  rpn.push(1)
  rpn.push(2)

  assert rpn.peek(0) == 2
  assert rpn.peek(1) == 1

def test_exchange():
  '''
  Exchange swaps order
  '''
  rpn = RpnCalculator()
  rpn.push(1)
  rpn.push(2)
  rpn.exchange()

  assert rpn.peek(0) == 1
  assert rpn.peek(1) == 2
  
def test_pop():
  '''
  Pop returns and removes from the stack
  '''
  rpn = RpnCalculator()
  rpn.push(1)
  rpn.push(2)
  
  assert rpn.pop() == 2
  assert rpn.peek(0) == 1
