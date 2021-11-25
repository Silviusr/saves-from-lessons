class Recursion():
    def __init__(self, n):
        self.n = n
    def rfacult(self):
        if self.n == 1:
            return self.n
        else:
            count = self.n
            for i in range(1, self.n):
                f = count
                f *= (self.n-i)
                count = f
        return count
b = Recursion(6)
print(b.rfacult())
class new(Recursion):
    def square(self):
