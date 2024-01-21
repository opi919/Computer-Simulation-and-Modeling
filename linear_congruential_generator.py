class LinearCongruentialGenerator:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def generate(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state


# Example usage:
seed = 27
a = 17
c = 43
m = 100

lcg = LinearCongruentialGenerator(seed, a, c, m)

# Generating 10 pseudorandom numbers
for _ in range(10):
    print(lcg.generate() / m)
