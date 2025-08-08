city = input("Enter city name: ").strip().lower()

monuments = {
    "delhi": "Red Fort",
    "agra": "Taj Mahal",
    "jaipur": "Jal Mahal"
}

if city in monuments:
    print("Monument of", city.title(), "is:", monuments[city])
else:
    print("Monument information not available for", city.title())