print(" Password Strength Checker")

password = input("Enter your password: ")

length_ok = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "@#$%&" for char in password)


if length_ok and has_digit and has_special:
    print("Strong password")

elif length_ok and (has_digit or has_special):
    print("Moderate password")

else:
    print("Weak password")


print("\nSuggestions to improve your password:")

if not length_ok:
    print(" Make it at least 8 characters long")

if not has_digit:
    print("Add at least one digit")

if not has_special:
    print("Add a special character (@, #, $, %, &)")
