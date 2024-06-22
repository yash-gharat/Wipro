class TestPowerOfTwo:
    def __init__(self, max=0):
        self.max = max
 
    def __iter__(self):
        self.n = 0
        return self
 
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
 
 
number = TestPowerOfTwo(3)
i = iter(number)
print(next(i))
 
print(next(i))
 
print(next(i))
 
print(next(i))