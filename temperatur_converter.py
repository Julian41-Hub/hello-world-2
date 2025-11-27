def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def main():
    print("=== Temperatur-Umrechner ===")

    try:
        celsius = float(input("Gib eine Temperatur in Celsius ein: "))
    except ValueError:
        print("Fehler: Bitte gib eine gültige Zahl ein.")
        return

    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)

    print(f"\nErgebnisse für {celsius}°C:")
    print(f"- Fahrenheit: {fahrenheit:.2f}°F")
    print(f"- Kelvin: {kelvin:.2f} K")


if __name__ == "__main__":
    main()
