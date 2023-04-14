"""
Fibonacci test
"""

from fibonacci import FibonacciRange

def str_test():
  
  assert [number for number in FibonacciRange("Hello")] == ValueError

def zero_test():
  
  assert [number for number in FibonacciRange(0)] == [0]
  
def one_test():
  
  assert [number for number in FibonacciRange(1)] == [0, 1]
  
def two_test():
  
  assert [number for number in FibonacciRange(2)] == [0, 1, 1]
  
def four_test():
  
  assert [number for number in FibonacciRange(4)] == [0, 1, 1, 2, 3]
  
def ten_test():
  
  assert [number for number in FibonacciRange(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
  
def negative_test():
  
  assert [number for number in FibonacciRange(-4)] == []
