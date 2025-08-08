num = int(input("Enter a number (1-7): "))

days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

if 1 <= num <= 7:
    print("Day is:", days[num])
else:
    print("Invalid input! Please enter a number from 1 to 7.")