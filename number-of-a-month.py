def main():
    seasons = ("Winter", "Spring", "Summer", "Autumn")

    month = int(input("Enter the month number (1-12): "))

    if month < 1 or month > 12:
        print("Invalid month number. Please enter a number between 1 and 12.")
        return

    if month in (12, 1, 2):
        season = seasons[0]  # Winter
    elif month in (3, 4, 5):
        season = seasons[1]  # Spring
    elif month in (6, 7, 8):
        season = seasons[2]  # Summer
    else:  # months 9, 10, 11
        season = seasons[3]  # Autumn

    print(f"The season for month {month} is: {season}")


if __name__ == "__main__":
    main()
