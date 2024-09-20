def gallons_to_liters(gallons):
    return gallons * 3.78541  # 1 gallon = 3.78541 liters

def main():
    while True:
        try:
            gallons = float(input("Enter the volume in gallons (or a negative number to exit): "))
            if gallons < 0:
                print("Exiting the program.")
                break
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is equal to {liters:.2f} liters.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
