"""
Fibonacci test
"""

from fibonacci import FibonacciRange

def str_test():
  
  assert [number for number in FibonacciRange('Hello')] == 'ValueError'
