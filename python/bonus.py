salary = float(input("Enter your salary: "))
years = int(input("Enter your years of service: "))

if years > 5:
    bonus = salary * 0.05
    print("Net bonus amount:", bonus)
else:
    print("No bonus")