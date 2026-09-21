# 1. PRÉSENTATION
# first_name = input("Enter your first name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {first_name}, you are {age} years old.")

# 2. CALCUL
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

total = a + b
produit = a * b
division = a / b

print(f"Sum - ({a} + {b}) = {total}")
print(f"Product - ({a} * {b}) = {produit}")
print(f"Division - ({a} / {b}) = {division:.2f}")

# 3. VOCABULAIRE
# supervised : On a les réponses (labels) et on apprend à partir de ces réponses
# unsupervised : On n'a pas les réponses et on cherche à identifier des patterns dans les données

# 4. ENVIRONNEMENT
# cd 01-terminal
# python3 -m venv .venv
# source .venv/bin/activate
# pip install numpy
# pip freeze > requirements.txt
# deactivate