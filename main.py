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
            mod = self.valToHex(n % self.targetBase)
            digits.insert(0, mod)
            n = n // self.targetBase
        return digits

    # Given a list of digits, find its representation in the initial base.
    def fromDigits(self, digits):
        n = 0
        digits = list(digits)
        for d in digits:
            d = self.hexToVal(d)
            n = self.initialBase * n + int(d)
        return n

    # Converts a hexadecimal number (A-F) to its corresponding numeric value.
    def hexToVal(self, a):
        hex_vals = ["A", "B", "C", "D", "E", "F"]
        return 10 + hex_vals.index(a) if a in hex_vals else a

    def valToHex(self, a):
        hex_vals = ["A", "B", "C", "D", "E", "F"]
        return hex_vals[a-10] if a > 9 else a

    def convertBase(self):
        result = ''.join(str(i) for i in self.toDigits(self.fromDigits(self.val)))
        print(f"Initial number in base {self.initialBase}: {self.val}")
        print(f"Result number in base {self.targetBase}: {result}")


converter = NumberConverter("4005", 10, 16)
converter.convertBase()
