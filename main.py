"""
Converting POSITIVE numbers between two bases, e.g. base 2 to base 10, base 16 to base 2, etc.
Resource: https://cs.stackexchange.com/questions/10318/the-math-behind-converting-from-any-base-to-any-base-without-going-through-base
"""


class NumberConverter:
    def __init__(self, val, base1, base2):
        self.initialBase = base1
        self.targetBase = base2
        self.val = val

    # Given a number in the initial base, find its representation in the target base.
    def toDigits(self, n):
        digits = []
        while n > 0:
            digits.insert(0, n % self.targetBase)
            n = n // self.targetBase
        return digits

    # Given a list of digits, find its representation in the initial base.
    def fromDigits(self, digits):
        n = 0
        digits = list(digits)
        for d in digits:
            n = self.initialBase * n + int(d)
        return n

    def convertBase(self):
        result = ''.join(str(i) for i in self.toDigits(self.fromDigits(self.val)))
        print(f"Initial number in base {self.initialBase}: {self.val}")
        print(f"Result number in base {self.targetBase}: {result}")


converter = NumberConverter("22", 16, 2)
converter.convertBase()
