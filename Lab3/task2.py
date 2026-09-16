def to_fahrenheit(self):
    return self.celsius * 9 / 5 + 32

def to_kelvin(self):
    return self.celsius + 273.15

def show_info(self):
    print("Celsius:", self.celsius)
    print("Fahrenheit:", round(self.to_fahrenheit(), 2))
    print("Kelvin:", round(self.to_kelvin(), 2))
