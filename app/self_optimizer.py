class SelfOptimizer:
    def __init__(self):
        self.temperature = 0.7
        self.min_temperature = 0.1
        self.max_temperature = 1.0

        self.total_requests = 0
        self.successful_requests = 0

    def adjust(self, score: int):
        """
        Adjust model temperature based on response quality score.
        """

        self.total_requests += 1

        if score >= 4:
            self.temperature += 0.03
            self.successful_requests += 1

        elif score >= 2:
            self.temperature += 0.01

        else:
            self.temperature -= 0.05


        self.temperature = max(
            self.min_temperature,
            min(self.temperature, self.max_temperature)
        )

    def get_temperature(self):
        return round(self.temperature, 2)

    def get_stats(self):
        success_rate = 0

        if self.total_requests > 0:
            success_rate = (
                self.successful_requests / self.total_requests
            ) * 100

        return {
            "temperature": round(self.temperature, 2),
            "total_requests": self.total_requests,
            "successful_requests": self.successful_requests,
            "success_rate": round(success_rate, 2)
        }