# Module 00 — Introduction à l'IA & Data Science

> **Objectif** : comprendre de quoi on parle, connaître les métiers, adopter le bon
> mindset, et préparer ta machine pour coder. À la fin, tu auras écrit ton premier
> programme et tu sauras lancer du code Python de façon propre.

Durée conseillée : ~2 h (théorie + installation + exercices).

---

## 1. C'est quoi l'IA, le ML, le Deep Learning, la Data Science ?

Ces mots sont souvent mélangés. Voici la hiérarchie, du plus large au plus précis :

```
Intelligence Artificielle (IA / AI)
└── Machine Learning (ML)            ← la machine apprend à partir de données
    └── Deep Learning (DL)           ← ML avec des réseaux de neurones profonds
        ├── NLP (texte)
        ├── Computer Vision (images)
        └── Generative AI / LLM (créer du contenu)
```

### Analogies simples

- **Data Science** : extraire des **connaissances** et des **prédictions** à partir de
  données. C'est le métier global (statistiques + code + domaine métier).
- **Machine Learning** : au lieu de programmer des règles à la main
  (`si température > 30 alors canicule`), on donne des **exemples** à l'ordinateur et
  il **apprend la règle tout seul**.
- **Deep Learning** : une famille de modèles ML (réseaux de neurones) très puissants,
  utilisés pour images, texte, son.
- **Generative AI** : des modèles (LLM comme ceux derrière les chatbots) qui
  **génèrent** du texte, des images, du code.

> **À retenir** : tout ML repose sur des **données**. Sans données de qualité,
> pas d'IA. C'est pour ça qu'on commence par Python, les données, puis le ML.

### Vocabulaire bilingue (EN → FR)

| English | Français | Idée |
|---------|----------|------|
| Artificial Intelligence (AI) | Intelligence artificielle | Faire faire à une machine des tâches "intelligentes" |
| Machine Learning (ML) | Apprentissage automatique | Apprendre à partir de données |
| Deep Learning (DL) | Apprentissage profond | ML via réseaux de neurones |
| Dataset | Jeu de données | La table/collection de données |
| Features | Variables / attributs | Les colonnes d'entrée |
| Label / Target | Étiquette / cible | La réponse à prédire |
| Model | Modèle | Ce qui a été "appris" |
| Training | Entraînement | La phase d'apprentissage |
| Prediction / Inference | Prédiction / inférence | Utiliser le modèle |
| Supervised | Supervisé | On a les réponses (labels) |
| Unsupervised | Non supervisé | Pas de réponses, on cherche des groupes |
| Overfitting | Surapprentissage | Le modèle apprend par cœur, généralise mal |

---

## 2. Les métiers visés après BeCode

| Métier | Ce qu'il/elle fait | Outils |
|--------|--------------------|--------|
| **Data Analyst** | Analyse les données, crée des tableaux de bord, répond à des questions business | SQL, Python, Excel, Power BI |
| **Data Scientist** | Construit des modèles prédictifs (ML/statistiques) | Python, Scikit-learn, stats |
| **Data Engineer** | Construit les "tuyaux" (pipelines) qui transportent et nettoient les données | SQL, Airflow, Spark, Cloud |
| **ML Engineer** | Met les modèles en production, les industrialise | Python, Docker, API, Cloud |

Tu n'as **pas besoin de choisir maintenant**. La formation BeCode te fait goûter à tout,
et tu te spécialises vers la fin (souvent pendant les projets et le stage).

---

## 3. Le mindset du futur Data/AI (le plus important)

L'IA, c'est **beaucoup de débogage et de patience**. Voici les 6 habitudes qui font la différence :

1. **Curiosité** : "pourquoi ça marche / ça plante ?" → tu cherches, tu testes.
2. **Décomposition** : un gros problème = plein de petits problèmes résolus un par un.
3. **Habitude de coder tous les jours** : 45 min/jour > 8 h une fois par semaine.
4. **Lire les erreurs** : un message d'erreur n'est pas un échec, c'est un **indice**.
5. **Chercher par soi-même** : savoir googler / lire la doc est LA compétence n°1.
6. **Expliquer simplement** : si tu peux l'expliquer, tu l'as compris (technique du canard en plastique).

> BeCode valorise énormément l'**auto-apprentissage** (self-learning) et l'**agilité**.
> Tu seras jugé·e autant sur ta capacité à apprendre que sur ton code.

---

## 4. Installation de l'environnement de travail

### 4.1 Vérifications

Ouvre le **Terminal** (sur macOS : `Cmd + Espace` puis tape "Terminal"), et tape :

```bash
python3 --version
git --version
```

Tu devrais voir, sur ta machine :
- `Python 3.14.0`
- `git version 2.50.1`

Si tu vois un numéro de version → c'est bon. Sinon, installe les outils.

### 4.2 Installer VS Code (ton éditeur de code)

Tu l'as déjà (`code` est disponible). Sinon : https://code.visualstudio.com/

Depuis ce dossier, ouvre VS Code :

```bash
code .
```

### 4.3 Créer un environnement virtuel (virtual environment)

**Pourquoi ?** Isoler les bibliothèques d'un projet pour ne pas tout casser à l'échelle
de ta machine. **C'est LA bonne pratique** que BeCode attend.

```bash
cd 00-introduction
python3 -m venv .venv
```

Cela crée un dossier `.venv/`. Pour l'**activer** (macOS/Linux) :

```bash
source .venv/bin/activate
```

Tu verras `(.venv)` apparaître au début de ton invitation de terminal. Bravo, tu es
dans l'environnement. Pour **désactiver** :

```bash
deactivate
```

> **Vocabulaire** : *virtual environment* = environnement virtuel. *Activate* = activer.

### 4.4 Installer les premières bibliothèques

Dans l'environnement activé :

```bash
pip install jupyterlab numpy pandas matplotlib
pip list
```

- `pip` = l'installateur de paquets Python.
- `jupyterlab` = l'outil pour les notebooks interactifs (très utilisés en data).
- `numpy`, `pandas`, `matplotlib` = les 3 piliers de la data en Python.

### 4.5 Fichier `requirements.txt`

Au lieu de se souvenir des paquets, on les liste dans un fichier pour les réinstaller :

```bash
pip freeze > requirements.txt
```

Pour réinstaller plus tard : `pip install -r requirements.txt`.

---

## 5. Ton premier programme

Crée un fichier `hello.py` (avec VS Code ou en ligne de commande) :

```python
# hello.py
nom = input("Comment tu t'appelles ? ")
print(f"Bonjour {nom}, prêt·e à devenir data scientist ?")
```

Lance-le :

```bash
python3 hello.py
```

Ce que tu viens de voir :
- `input(...)` : demande une info à l'utilisateur.
- `print(...)` : affiche du texte.
- `f"..."` : une **f-string**, pour insérer une variable dans du texte.
- `#` : un **commentaire** (ignoré par Python). En production, on commente peu mais bien.

---

## 6. Exercices

Fais-les dans un fichier `exercices.py`. Les solutions sont tout en bas — **regarde-les
seulement après avoir essayé**.

1. **Présentation** : demande le prénom et l'âge de l'utilisateur, puis affiche
   `Bonjour {prénom}, tu as {âge} ans.`
2. **Calcul** : demande deux nombres, affiche leur somme, leur produit et leur division.
   (Indice : `float(input(...))` convertit le texte en nombre décimal.)
3. **Vocabulaire** : écris en commentaire, avec tes mots, la différence entre
   *supervised* et *unsupervised learning*.
4. **Environnement** : crée un nouvel environnement virtuel dans `01-terminal/`,
   active-le, installe `numpy`, puis génère un `requirements.txt`. Désactive-le.

---

## 7. Solutions

<details>
<summary>Cliquer pour révéler</summary>

```python
# Exercice 1
prenom = input("Ton prénom ? ")
age = input("Ton âge ? ")
print(f"Bonjour {prenom}, tu as {age} ans.")

# Exercice 2
a = float(input("Premier nombre : "))
b = float(input("Deuxième nombre : "))
print(f"Somme = {a + b}")
print(f"Produit = {a * b}")
print(f"Division = {a / b}")

# Exercice 3 : (exemple de réponse)
# Supervised = on connaît les réponses (labels) et le modèle apprend à les prédire.
# Unsupervised = pas de réponses ; on cherche des structures cachées (groupes).
```

Exercice 4 (commandes) :

```bash
cd 01-terminal
python3 -m venv .venv
source .venv/bin/activate
pip install numpy
pip freeze > requirements.txt
deactivate
```

</details>

---

## 8. Récapitulatif & auto-évaluation

Tu peux passer au Module 01 si tu sais :
- [ ] Expliquer la différence IA / ML / DL / GenAI.
- [ ] Citer les 4 métiers et ce qu'ils font.
- [ ] Créer et activer un environnement virtuel.
- [ ] Installer un paquet avec `pip` et générer un `requirements.txt`.
- [ ] Écrire et lancer un petit script Python avec `input` et `print`.

---

## Ressources recommandées

- Python officiel : https://www.python.org/
- VS Code : https://code.visualstudio.com/docs/getstarted
- Google's Machine Learning Crash Course (EN) : https://developers.google.com/machine-learning/crash-course
- BeCode : https://becode.org/en/job-seekers/trainings/ai-data-science

**Prochaine étape → Module 01 : le Terminal.** Dis-moi quand tu as terminé les
exercices (ou si tu bloques) et on continue.

# Vocabulaire 
roadmap = feuille de route
mindset =  état d'esprit
deep = profonde
features = caractééristiques 
feedbacks = commentaires