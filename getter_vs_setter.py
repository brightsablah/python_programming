class ToyCar:
    def __init__(self, color, engine_power):
        self.color = color
        self._engine_power = engine_power  # Protected attribute

    # Getter method for engine_power
    @property
    def engine_power(self):
        return self._engine_power

    # Setter method for engine_power
    @engine_power.setter
    def engine_power(self, value):
        if value > 100:
            print("Power too high! Setting to maximum allowed (100).")
            self._engine_power = 100
        else:
            self._engine_power = value
