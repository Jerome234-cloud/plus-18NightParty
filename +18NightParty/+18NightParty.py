# Ask user their name
name = input("What's your name? ")
# Ask birth year

print(f"Welcome, {name}! ")

birth_year = input("What year were you born? ")
# Convert to integer
birth_year = int(birth_year)
# Calculate their age assuming the current year is 2025
age = 2025 - birth_year
#Greet and tell them their age
print(f"{name}! You are {age} years old. ")
# The party is only for young adults. Not for underage and Not for 60 years and above
if age >= 60:
    print("Sorry! This party is for young adult only. ")
elif age >= 18:
    print("You can come in! Have fun. ")
else:
    print("Sorry! The party is not for underage.")
