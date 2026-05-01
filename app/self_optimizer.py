class SelfOptimizer:
    def __init__(self):
        self.temperature = 0.7

    def adjust(self, score):
        if score < 2:
            self.temperature -= 0.1
        else:
            self.temperature += 0.05

        self.temperature = max(0.1, min(self.temperature, 1.0))