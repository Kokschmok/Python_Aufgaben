celsius = input("Zu angebende Temperatur: ")


def fktCelsiusToKelvin(celsius):
    kelvin = float(celsius) + 273.15
    celsius = round(float(celsius), 2)
    kelvin = round(kelvin, 2)
    print("Eine Temperatur von:\t", str(celsius), "°C\n\nentspricht:\t\t\t\t", str(kelvin), "K")


def fktCelsiusToFahrenheit(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    celsius = round(float(celsius), 2)
    fahrenheit = round(fahrenheit, 2)
    print("bzw.:\t\t\t\t\t", str(fahrenheit), "°F")


fktCelsiusToKelvin(celsius)
fktCelsiusToFahrenheit(celsius)

print("\nDie Berechnung wurde durchgeführt von Elyesa Sentürk.")
