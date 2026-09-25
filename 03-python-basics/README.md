# Module 03 — Python : les bases

> **Objectif** : écrire tes premiers vrais programmes Python — variables, types,
> conditions, boucles, listes et fonctions. C'est LE socle de toute la formation.
> Tout le reste (data, ML, DL) est du Python.

Durée conseillée : ~2 jours (2-3h/jour avec exercices). Code, code, code.

---

## 1. Pourquoi Python en Data Science ?

- **Simple à lire** : quasi de l'anglais en langage naturel.
- **Énorme écosystème data** : NumPy, Pandas, Scikit-learn, PyTorch, HuggingFace…
- **Communauté géante** : tu trouveras toujours une réponse sur le web.
- Il est le **n°1** de la data science et de l'IA partout dans le monde.

### Vocabulaire bilingue

| English | Français |
|---------|----------|
| Variable | Variable |
| Data type | Type de donnée |
| String | Chaîne de caractères (`str`) |
| Integer / Float / Boolean | Entier / Décimal / Booléen |
| Condition | Condition |
| Loop | Boucle |
| Iterate / Iteration | Itérer / itération |
| Function | Fonction |
| Argument / Parameter | Argument / paramètre |
| Return | Retourner (renvoyer une valeur) |
| Index | Position (en Python, commence à 0) |

---

## 2. Lancement de Python

Deux façons :

### a) Le mode interactif (REPL) — pour tester vite

```bash
python3
```
Tu vois `>>>` : tape `1 + 1` puis Entrée. Pour quitter : `exit()` ou `Ctrl + D`.

### b) Les fichiers `.py` — pour de vrais programmes

```bash
python3 mon_programme.py
```

> **Convention BeCode** : chaque création de fichier → commit Git (tu maîtrises ✅).

---

## 3. Variables et types

Une **variable** = une "boîte" avec un nom qui contient une valeur.

```python
prenom = "Jesus"        # str  : texte
age = 25                # int  : nombre entier
taille = 1.75           # float: nombre décimal
est_data_scientist = True   # bool : Vrai/Faux
```

- On crée une variable avec `nom = valeur` (= s'appelle l'**affectation**).
- Python **devine le type** automatiquement (typage dynamique).

```python
age = 25
age = age + 1           # maintenant 26
print(type(age))        # <class 'int'>
```

| Type | Exemple | Usage |
|------|---------|-------|
| `str` | `"bonjour"`, `'a'` | Textes, colonnes de type catégoriel |
| `int` | `42` | Comptes, index |
| `float` | `3.14`, `2.0` | Poids, prix, mesures |
| `bool` | `True`, `False` | Tests logiques |

> **Règles de nommage** : minuscules + `_` entre mots (`prix_total`, non `prixTotal`),
> jamais d'espace, pas de mot réservé (`if`, `for`, `True`…).

### Conversion de types (casting)

```python
str(25)        # "25"
int("10")      # 10
float("2.5")   # 2.5
int(2.9)       # 2   (tronque, n'arrondit pas !)
round(2.9)     # 3   (arrondit)
bool(0)        # False ; bool(n'importe_quoi_d_autre) -> True
```

---

## 4. Nombres et opérateurs

```python
a, b = 10, 3

a + b    # 13   addition
a - b    # 7    soustraction
a * b    # 30   multiplication
a / b    # 3.333...  division (toujours float)
a // b   # 3    division entière
a % b    # 1    reste de la division (modulo)
a ** b   # 1000 puissance

a += 5   # a = a + 5  (idem -=, *=, /=)
```

> Le **modulo** `%` est très utilisé en data (ex : pair/impair, regroupement).

---

## 5. Les chaînes de caractères (str)

```python
nom = "BeCode"
print(nom.upper())      # "BECODE"
print(nom.lower())      # "becode"
print(nom.strip())      # enlève espaces avant/après
print(len(nom))         # 6  (nombre de caractères)
print(nom[0])           # "B" (premier caractère, index 0)
print(nom[-1])          # "e" (dernier caractère)
print(nom[0:3])         # "BeC" (tranche/slice : de 0 inclus à 3 exclu)
```

### Concaténer et formater

```python
# Concaténation (déconseillée)
message = "Bonjour " + nom

# f-string (LA manière moderne, à privilégier)
message = f"Bonjour {nom}, tu as {age} ans !"
print(f"Prix : {taille:.2f}")   # 2 décimales
```

---

## 6. Comparaisons et logique

```python
x = 5
x == 5     # True   égalité
x != 6     # True   différence
x > 4      # True
x >= 5     # True
x < 3      # False
```

```python
âge = 18
a_permis = True

âge >= 18 and a_permis        # True  (ET : les deux)
âge < 18 or a_permis          # True  (OU : au moins un)
not a_permis                  # False (NON : inverse)
```

> En data science, `and`/`or`/`not` servent à filtrer et construire des règles.

---

## 7. Les conditions : `if / elif / else`

```python
note = 72

if note >= 85:
    print("Excellent")
elif note >= 60:
    print("Bien")
elif note >= 50:
    print("Passable")
else:
    print("Échec")
```

Points clés :
- **Indentation de 4 espaces** = le bloc de code (Python n'utilise PAS d'accolades).
- `elif` = *else if* (autre cas). Le `else` final est optionnel.

### Conditions avec `in`

```python
couleurs = ["rouge", "bleu", "vert"]
if "bleu" in couleurs:
    print("Bleu présent !")
```

---

## 8. Les boucles (loops)

### `for` : parcourir une séquence

```python
for i in range(5):          # 0, 1, 2, 3, 4 (range(5) : de 0 inclus à 5 exclu)
    print(i)

for i in range(2, 8, 2):    # début, fin (exclue), pas : 2, 4, 6
    print(i)

noms = ["ana", "bob", "cara"]
for n in noms:
    print(f"Salut {n} !")
```

### `while` : tant que

```python
compte = 0
while compte < 3:
    print(compte)
    compte += 1
```

### `break` / `continue`

```python
for i in range(10):
    if i == 3:
        continue        # saute l'itération (n'affiche pas 3)
    if i == 6:
        break           # sort de la boucle
    print(i)            # 0,1,2,4,5
```

---

## 9. Les listes (liste / array)

Une liste = une suite ordonnée d'éléments `[ ... ]`.

```python
fruits = ["pomme", "banane", "kiwi"]

fruits[0]        # "pomme"   (index 0 !)
fruits[-1]       # "kiwi"
fruits[0:2]      # ["pomme", "banane"]  (slice, 2 exclu)
len(fruits)      # 3

fruits.append("orange")    # ajoute à la fin
fruits.insert(0, "mangue") # insère à l'index 0
fruits.remove("kiwi")      # retire l'élément
fruits.pop()               # retire et renvoie le dernier
fruits.sort()              # trie en place
"pomme" in fruits          # True
```

Parcours de liste avec index (`enumerate`) :

```python
for i, fruit in enumerate(fruits):
    print(i, fruit)        # 0 pomme, 1 mangue, ...
```

### Compréhensions de listes (glisse-t-on ? … OUI, indispensable)

```python
nombres = [1, 2, 3, 4, 5]
double = [n * 2 for n in nombres]        # [2, 4, 6, 8, 10]
pairs  = [n for n in nombres if n % 2 == 0]  # [2, 4]
```

Une ligne = boucle + collecte + filtre. C'est du Python "data" pur.

---

## 10. Les fonctions

Une fonction = un bloc réutilisable avec un nom.

```python
def aire_rectangle(longueur, largeur):
    """Calcule l'aire d'un rectangle."""   # docstring (documentation)
    return longueur * largeur

resultat = aire_rectangle(5, 3)
print(resultat)          # 15
```

- `def nom(paramètres):` puis **bloc indenté**.
- `return` renvoie une valeur (ou `None` si absent).
- Les paramètres peuvent avoir une **valeur par défaut** :

```python
def saluer(nom, ponctuation="!"):
    return f"Bonjour {nom}{ponctuation}"

saluer("Ana")            # "Bonjour Ana!"
saluer("Ana", "?")       # "Bonjour Ana?"
```

### Fonction pure vs effets de bord

```python
# PURE (recommandé) : même entrée -> même sortie, ne modifie rien à l'extérieur
def double(x):
    return x * 2

# AVEC EFFET DE BORD : modifie quelque chose à l'extérieur
liste_globale = []
def ajouter(x):
    liste_globale.append(x)
```

---

## 11. Résumé : les 5 piliers de ce module

1. **Variables & types** (str, int, float, bool) + `cast`.
2. **Conditions** (`if/elif/else`, `and/or/not`).
3. **Boucles** (`for`, `while`, `break`, `continue`).
4. **Listes** (`append`, index, slices, compréhensions).
5. **Fonctions** (`def`, `return`, paramètres par défaut).

---

## 12. Exercices (module 3)

Crée `03-python-basics/exercices.py` et un dossier de travail Git.

1. **Convertisseur** : demande température en Celsius, affiche en Fahrenheit
   (formule : `F = C * 9/5 + 32`), avec message "chaud" si > 30.
2. **Pair/Impair** : un nombre, affiche "pair" si divisible par 2, sinon "impair".
   Utilise la boucle `for` pour tester de 1 à 10.
3. **Liste & boucle** : `notes = [12, 17, 8, 15, 10]`. Calcule et affiche la **moyenne**
   (sans `sum` ni `statistics`, avec une boucle), puis le **max** et le **min**.
4. **Compréhension** : à partir de `nombres = range(1, 21)`, fais la liste des multiples
   de 3.
5. **Fonction** : écris `est_voyelle(lettre)` qui renvoie `True` si la lettre est une
   voyelle, puis teste-la dans une boucle sur `"hello world"` en comptant les voyelles.
6. **Bonus (f-string)** : affiche un tableau de conversion 0→40°C par pas de 5, aligné,
   en utilisant une f-string avec `:.1f`.

---

## 13. Solutions

<details>
<summary>Cliquer pour révéler</summary>

```python
# Exercice 1
c = float(input("Température en °C : "))
f = c * 9 / 5 + 32
message = "chaud !" if f > 86 else ""   # 30°C = 86°F
print(f"{c}°C = {f:.1f}°F {message}")

# Exercice 2
for n in range(1, 11):
    if n % 2 == 0:
        print(f"{n} est pair")
    else:
        print(f"{n} est impair")

# Exercice 3
notes = [12, 17, 8, 15, 10]
total = 0
mini, maxi = notes[0], notes[0]
for n in notes:
    total += n
    if n > maxi:
        maxi = n
    if n < mini:
        mini = n
print(f"Moyenne = {total / len(notes):.2f}, max = {maxi}, min = {mini}")

# Exercice 4
multiples_3 = [n for n in range(1, 21) if n % 3 == 0]
print(multiples_3)   # [3, 6, 9, 12, 15, 18]

# Exercice 5
def est_voyelle(lettre):
    return lettre in "aeiouy"

texte = "hello world"
nb_voyelles = sum(1 for l in texte if est_voyelle(l))
print(f"Voyelles trouvées : {nb_voyelles}")

# Exercice 6
print(" C     F")
for c in range(0, 41, 5):
    print(f"{c:3.0f}  {c * 9 / 5 + 32:6.1f}")
```

</details>

---

## 14. Auto-évaluation

Passe au Module 04 si tu sais :
- [ ] Déclarer str/int/float/bool et convertir entre types.
- [ ] Écrire des conditions et utiliser `and`/`or`/`not`.
- [ ] Boucler avec `for`/`while` + `break`/`continue`.
- [ ] Manipuler des listes (index, `append`, slices).
- [ ] Écrire une compréhension de liste.
- [ ] Définir et appeler une fonction avec `return`.

### Aide-mémoire

| Concept | Exemple |
|---------|---------|
| Variable | `x = 3` |
| f-string | `f"{x:.2f}"` |
| Condition | `if x > 0: ...` |
| Boucle | `for i in range(5):` |
| Liste | `[i*2 for i in range(10)]` |
| Fonction | `def f(a): return a + 1` |

**Prochaine étape → Module 04 : Python intermédiaire** (dicts, fichiers, modules,
gestion des erreurs, POO). Dis-moi quand c'est fait et envoie-moi `git log --oneline` 😉