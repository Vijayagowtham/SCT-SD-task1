def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

def convert_temperature(value, from_scale, to_scale):
    scale_aliases = {
        'c': 'celsius',
        'f': 'fahrenheit',
        'k': 'kelvin'
    }

    from_scale = from_scale.strip().lower()
    to_scale = to_scale.strip().lower()

    # Expand short forms (c, f, k) to full names
    from_scale = scale_aliases.get(from_scale, from_scale)
    to_scale = scale_aliases.get(to_scale, to_scale)

    if from_scale == to_scale:
        return value

    if from_scale == 'celsius':
        if to_scale == 'fahrenheit':
            return celsius_to_fahrenheit(value)
        elif to_scale == 'kelvin':
            return celsius_to_kelvin(value)

    elif from_scale == 'fahrenheit':
        if to_scale == 'celsius':
            return fahrenheit_to_celsius(value)
        elif to_scale == 'kelvin':
            return fahrenheit_to_kelvin(value)

    elif from_scale == 'kelvin':
        if to_scale == 'celsius':
            return kelvin_to_celsius(value)
        elif to_scale == 'fahrenheit':
            return kelvin_to_fahrenheit(value)

    raise ValueError("Invalid temperature scale provided.")

# Interactive prompt
def main():
    print("🌡️ Welcome to the Temperature Converter!")
    try:
        value = float(input("Enter the temperature value (e.g., 25): "))
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value for the temperature.")
        return

    from_scale = input("Convert from (Celsius/C, Fahrenheit/F, Kelvin/K): ")
    to_scale = input("Convert to (Celsius/C, Fahrenheit/F, Kelvin/K): ")

    try:
        result = convert_temperature(value, from_scale, to_scale)
        print(f"\n✅ {value:.2f}° {from_scale.capitalize()} is equal to {result:.2f}° {to_scale.capitalize()}")
    except ValueError as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
