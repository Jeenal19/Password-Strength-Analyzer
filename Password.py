import re
import math
from datetime import datetime


# Calculate password entropy
def calculate_entropy(password):
    charset = 0

    if re.search(r'[a-z]', password):
        charset += 26

    if re.search(r'[A-Z]', password):
        charset += 26

    if re.search(r'[0-9]', password):
        charset += 10

    if re.search(r'[^A-Za-z0-9]', password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)

    return round(entropy, 2)


# Analyze password strength
def password_strength(password):

    score = 0
    feedback = []


    # Length check
    if len(password) >= 12:
        score += 2

    elif len(password) >= 8:
        score += 1

    else:
        feedback.append("Use minimum 8 characters")


    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")


    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")


    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers")


    # Special character check
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Add special characters")


    # Strength result
    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    else:
        strength = "Strong"


    entropy = calculate_entropy(password)


    return strength, entropy, feedback



# Main Program

print("🔐 Password Strength Analyzer")
print("-----------------------------")


password = input("Enter password: ")


strength, entropy, feedback = password_strength(password)



# Display result

print("\n----- Password Analysis Report -----")

print("Password Strength :", strength)

print("Entropy Score     :", entropy, "bits")



if feedback:

    print("\nRecommendations:")

    for item in feedback:
        print("-", item)

else:

    print("\nExcellent password!")




# Save result into password result.txt

with open("password result.txt", "a") as file:


    file.write("\n====================================\n")

    file.write("Password Analysis Report\n")

    file.write("Date: " + str(datetime.now()) + "\n")

    file.write("Password: " + password + "\n")

    file.write("Strength: " + strength + "\n")

    file.write("Entropy: " + str(entropy) + " bits\n")



    if feedback:

        file.write("\nRecommendations:\n")

        for item in feedback:

            file.write("- " + item + "\n")

    else:

        file.write("\nNo recommendations. Strong password.\n")


    file.write("====================================\n")



print("\n✅ Result saved in password result.txt")