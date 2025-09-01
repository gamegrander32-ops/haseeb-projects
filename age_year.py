
birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year  

choice = input("Aapko kya dekhna hai? ('age' ya 'year'): ")

if choice.lower() == "age":
    print("Your Age is:", age, "years")
elif choice.lower() == "year":
    print("Your Birth Year is:", birth_year)
else:
    print("Invalid choice! Sirf 'age' ya 'year' likho.")