import math


def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)  # Area in square centimeters
    area_square_meters = area / 10000  # Convert area to square meters
    unit_price = price / area_square_meters  # Price per square meter
    return unit_price


def main():
    print("Enter details for Pizza 1:")
    diameter1 = float(input("Diameter in cm: "))
    price1 = float(input("Price in euros: "))

    print("Enter details for Pizza 2:")
    diameter2 = float(input("Diameter in cm: "))
    price2 = float(input("Price in euros: "))

    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    print(f"Pizza 1 unit price: {unit_price1:.2f} euros/m²")
    print(f"Pizza 2 unit price: {unit_price2:.2f} euros/m²")

    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


if __name__ == "__main__":
    main()
