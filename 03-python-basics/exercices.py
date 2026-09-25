# 12. Exercices (module 3)

# =================== 1. Convertisseur ======================
celsius = float(input("Saisissez la température (Celsius) : "))
fahrenheit  = round((celsius * 9/5) + 32)
if celsius > 30:
    print(f"Températue : {fahrenheit}°F - C'est chaud 🥵")
else:
   print(f"Températue : {fahrenheit}°F ") 


# ===================== 2. Pair & Impair =====================
for i in range(1, 11) :
    if i % 2 == 0 :
        print(f"{i} : pair")
    else :
        print(f"{i} : impair")

# ===================== 3. Moyenne ===========================
notes = [12, 17, 8, 15, 19]
somme = 0
compteur = 0
moyenne = 0
min = notes[0]
max = notes[0]

for i in notes:
    somme += i 
    if i > max:
        max = i
    if i < min:
        min = i
    compteur += 1 
print(f"moyenne : {round((somme/compteur), 2)}, max = {max}, min = {min}")
    
# ====================== 4. Compréhension =======================
multiples_3 = [nombre for nombre in range(1, 21) if nombre % 3 == 0]
print(f"{multiples_3}")

# ======================== 5. Fonction =======================
def est_voyelle(lettre):
    voyelles = "aeiouy"
    # Retourne les dans lettres dans voyelles.
    return lettre in voyelles

texte = "hello world people"
nb_voyelles = sum(1 for i in texte if est_voyelle(i))
print(f"Voyelles dans '{texte}' : { nb_voyelles}")

# ======================= Bonus ============================
for celsius in range(0, 41, 5):
    print(f"{celsius:3.0f}  {celsius * 9 / 5 + 32:6.1f}")
