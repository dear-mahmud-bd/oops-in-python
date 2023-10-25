class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius_temp):
        def convert(celsius_temp):
            return (celsius_temp * 9/5) + 32
        return convert(celsius_temp)

converter = TemperatureConverter()
result = converter.celsius_to_fahrenheit(36)
print(result)