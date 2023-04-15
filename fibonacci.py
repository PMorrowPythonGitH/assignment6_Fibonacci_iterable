"""
Fibonacci assignment
"""

#n = int(input("Please enter a number"))


class FibonacciRange:

    def __init__(self, fibvalue, step=1):

        self.fibvalue = fibvalue
        self.step = step

        self.n1 = 0
        self.n2 = 1
        self.count = 0
    

    def __iter__(self):
        return self


    def __next__(self):

        if type(self.fibvalue) == int:

            n3 = self.n1


            if self.count > self.fibvalue:
                raise StopIteration

            self.n1, self.n2 = self.n2, self.n1 + self.n2

            self.count += self.step

            return n3
        
        else:

            raise ValueError("ValueError")
