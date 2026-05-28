class SelfOptimizer:

    def __init__(self):

        self.temperature = 0.7

    def adjust(self, score):

        if score >= 4:
            self.temperature += 0.03

        elif score < 2:
            self.temperature -= 0.05

        self.temperature = max(
            0.1,
            min(self.temperature, 1.0)
        )

    def get_temperature(self):

        return round(self.temperature, 2)