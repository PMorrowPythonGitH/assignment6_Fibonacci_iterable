"""
Fibonacci test
"""

import pytest

from fibonacci import FibonacciRange

#def test_str():
  
  #assert [number for number in FibonacciRange("Hello")] == ValueError

#def test_zero():
  
  #assert [number for number in FibonacciRange(0)] == [0]
  
#def test_one():
  
  #assert [number for number in FibonacciRange(1)] == [0, 1]
  
def test_two():
  
  [number for number in FibonacciRange(2)] == [0, 1, 1]
  
#def test_four():
  
  #assert [number for number in FibonacciRange(4)] == [0, 1, 1, 2, 3]
  
#def test_ten():
  
  #assert [number for number in FibonacciRange(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
  
#def test_negative():
  
  #assert [number for number in FibonacciRange(-4)] == []
