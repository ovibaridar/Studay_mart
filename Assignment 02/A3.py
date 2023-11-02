def fahrenheit_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius


fahrenheit = float(input("Enter temperature in Fahrenheit: "))


celsius = fahrenheit_celsius(fahrenheit)


print("Temperature in Celsius:", celsius)
