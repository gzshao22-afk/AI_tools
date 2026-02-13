```python
import random

class VossPinkNoise:
    def __init__(self, n_generators=12):
        self.n = n_generators
        self.generators = [random.uniform(-1, 1) for _ in range(self.n)]
        self.counter = 0

    def next_sample(self):
        self.counter += 1
        # Find index of first set bit (trailing zeros)
        # e.g., 1 (01) -> 0, 2 (10) -> 1, 3 (11) -> 0, 4 (100) -> 2
        idx = (self.counter & -self.counter).bit_length() - 1
        
        if idx < self.n:
            self.generators[idx] = random.uniform(-1, 1)
        
        return sum(self.generators)

# Usage
pink_gen = VossPinkNoise()
sample = pink_gen.next_sample()

```