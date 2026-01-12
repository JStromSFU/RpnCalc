import pytest

from rpn.calc import RpnCalculator

def test_add():
  rpn = RpnCalculator()
  rpn.push(20)
  rpn.push(5)
  rpn.add()

  assert rpn.peek(0) == 25

def test_sub():
  rpn = RpnCalculator()
  rpn.push(20)
  rpn.push(5)
  rpn.sub()

  assert rpn.peek(0) == 15

def test_mul():
  rpn = RpnCalculator()
  rpn.push(20)
  rpn.push(5)
  rpn.mul()

  assert rpn.peek(0) == 100

def test_div():
  rpn = RpnCalculator()
  rpn.push(20)
  rpn.push(5)
  rpn.div()

  assert rpn.peek(0) == 4


