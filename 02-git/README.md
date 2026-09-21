# Module 02 — Git & GitHub

> **Objectif** : versionner ton code avec Git, utiliser GitHub (cloud) pour sauvegarder,
> partager et collaborer. À la fin tu sauras créer un repo, faire des commits, des
> branches, push/pull, et gérer un `.gitignore` (adieu les `.DS_Store` !).

Durée conseillée : ~2h30. Encore une fois : **tape tout toi-même**.

---

## 1. Pourquoi Git ?

Imagine que tu travailles sur ton code. Tu veux : sauvegarder l'historique, revenir en
arrière si tu casses tout, tester une idée sans casser le code existant, et collaborer
à plusieurs sans s'écraser.

**Git** = un outil de *versioning* (gestion de versions) qui enregistre **l'historique
de tes fichiers**. **GitHub** = un site (cloud) qui héberge tes repos, permet le backup
et la collaboration (beaucoup d'entreprises recrutent directement via ton GitHub).

### Vocabulaire bilingue

| English | Français | Idée |
|---------|----------|------|
| Version control | Gestion de versions | L'historique du code |
| Repository (repo) | Dépôt | Le dossier versionné (+ son historique) |
| Commit | Validation / snapshot | Une "photo" de ton code à un instant T |
| Tracked / Untracked | Suivi / non suivi | Fichiers connus ou pas de Git |
| Stage (index) | Zone de préparation | Fichiers prêts à être commités |
| Working directory | Répertoire de travail | Tes fichiers sur le disque |
| Branch | Branche | Une ligne de développement parallèle |
| Merge | Fusion | Réunir deux branches |
| Remote | Dépôt distant | Le repo sur GitHub |
| Clone | Cloner | Copier un repo distant en local |
| Pull / Push | Tirer / Pousser | Récupérer / envoyer les changements |
| Pull request (PR) | Demande de fusion | Proposer l'ajout de son code |

---

## 2. Configuration initiale

Un fois par machine :

```bash
git config --global user.name "TonPrenom"
git config --global user.email "ton.email@exemple.com"
git config --global init.defaultBranch main
```

- Un commit est signé par ce nom/email.
- `--global` = pour tous tes projets. Vérifie : `git config --list`.

> BeCode exige typiquement `main` comme branche par défaut (et non `master`).

---

## 3. Le cycle de vie d'un fichier

```
Working directory  ──git add──►  Stage (index)  ──git commit──►  Historique
     (modifié)                       (préparé)                     (sauvegardé)
```

1. Tu modifies un fichier → il devient **modified** (modifié).
2. `git add fichier` → il passe dans le **stage** (préparé / *staged*).
3. `git commit -m "message"` → il est **commité** (*committed*) : une photo est enregistrée.

### Vos 4 premières commandes

```bash
git init                     # transforme le dossier courant en repo
git status                   # l'état de ton repo (À NE PAS QUITTER !)
git add fichier.py           # préparer un fichier
git add .                    # préparer tous les fichiers
git commit -m "Mon premier commit"   # enregistrer la photo
git log --oneline            # historique des commits
```

> **Réflexe n°1** : `git status` AVANT et APRÈS chaque action. Tu verras l'état exact.

---

## 4. Créons ton premier repo : ta formation !

Installons Git directement sur ton dossier de formation. Le dossier contient des
`.venv` (énormes, à ne PAS versionner) et des `.DS_Store` (fichiers système macOS).

### 4.1 Le fichier `.gitignore`

Il liste les choses à **ignorer**. Crée-le à la racine :

```gitignore
# .gitignore
# Environnements virtuels
.venv/
venv/

# macOS
.DS_Store

# Python
__pycache__/
*.py[cod]
.ipynb_checkpoints/

# IDE
.vscode/
.idea/
```

- `dossier/` = ignorer un dossier entier.
- Le nom de fichier exact `.gitignore` (rien avant le point).

### 4.2 Initialisation + premier commit

```bash
cd ~/Desktop/devIA/formations/beCode
git init
git status              # -> .venv et .DS_Store doivent être ignorés (grisés)
git add .
git commit -m "Début de la formation : modules 00 à 02"
git log --oneline
```

> ⚠️ Si `.venv` apparaît, booste `.gitignore`. Un `.venv` commité = repo pollué.

---

## 5. Différer, corriger, revenir en arrière

```bash
git diff                     # voir les changements NON stagés (avant add)
git diff --staged            # voir les changements stagés (après add)
git restore fichier.py       # annuler les modifs non commitées (le fichier revient en arrière)
git restore --staged f.py    # "dé-stager" (enlever du stage sans annuler)
git reset --hard HEAD        # ⚠️ tout casser ? revient au dernier commit (danger !)
```

Règle de sécurité : toujours `git status` avant un commande destructrice.

---

## 6. Les branches : tester sans casser

**Pourquoi ?** Tu veux expérimenter sans toucher au code stable `main`.

```bash
git branch                # liste les branches (l'étoile * = courante)
git branch test-tuto      # crée une branche nommée test-tuto
git switch test-tuto      # bascule dessus (ou : git checkout test-tuto)
git switch main           # revient sur main
git switch -c nouvelle    # crée + bascule directement (-c)
```

Tu travailles sur `test-tuto`, ça marche → tu **fusionnes** sur `main` :

```bash
git switch main           # retourne sur la branche principale
git merge test-tuto       # fusionne test-tuto dans main
git branch -d test-tuto   # supprime la branche (déjà fusionnée)
```

```
main      : A --- B ---*M---        (*M = commit de merge)
test-tuto :      \--- C ---/
```

> **Bonnes pratiques** : `main` = toujours quelque chose qui fonctionne ; chaque nouvelle
> fonctionnalité/variante → une branche dédiée ; merge une fois testé.

---

## 7. GitHub : sauvegarder dans le cloud

### 7.1 Créer le repo sur GitHub

1. Va sur https://github.com et crée un compte (gratuit).
2. Clique **New repository** → nomme-le `beCode-formation` → **Public ou Private** →
   **ne coche rien** (pas de README) → Create.
3. GitHub te donne des commandes à coller. Connecte le repo local :

```bash
git remote add origin https://github.com/TON_USER/beCode-formation.git
git branch -M main              # renomme ta branche en main
git push -u origin main         # premier envoi (-u : mémorise origin/main)
```

- `remote` = l'URL du repo distant. `push` = envoyer. `pull` = récupérer.

### 7.2 Le cycle quotidien

```bash
git add .
git commit -m "description claire du changement"
git push            # envoie vers GitHub
git pull            # récupère les changements des autres (avant de coder)
```

### 7.3 Récupérer un projet existant

```bash
git clone https://github.com/utilisateur/projet.git
cd projet
```

### 7.4 Collaboration via Pull Request (PR)

1. **Fork** (copie du repo chez toi) OU branche sur le même repo.
2. Tu fais tes commits sur ta branche, tu `push`.
3. GitHub → **Compare & pull request** → tu décris ton changement.
4. Les autres **reviewnt**, discutent, puis **merge**.

> C'est le workflow standard en entreprise ("GitHub flow"). On le reverra.

### 7.5 SSH ou HTTPS ?

- **HTTPS** : facile, mais demande login/mot de passe (ou token) à chaque push.
- **SSH** : une fois configuré (`ssh-keygen`, copie de la clé publique dans GitHub), plus
  de mot de passe. Pourquoi pas plus tard : on reste simple maintenant.

---

## 8. Aperçu : commit propre en data science

En data science, messages de commit **clairs** et **sémantiques** (convention BeCode) :

```text
feat: add train/test split
fix: correct missing value imputation
docs: update README with setup instructions
chore: add requirements.txt
```

- `feat`: nouvelle fonctionnalité · `fix`: correction · `docs`: doc · `chore`: maintenance.

---

## 9. Exercices

1. **Init** : dans `beCode/`, crée un `.gitignore` (masque `.venv`, `.DS_Store`,
   `__pycache__/`) puis `git init`, `git add .`, commit, et vérifie `git log --oneline`.
2. **Ignore** : crée un fichier test `echo "x" > test_temporaire.txt`, `git status`.
   Ajoute-le au `.gitignore`, vérifie qu'il disparaît de `git status`.
3. **Branche** : crée et bascule sur une branche `experiments`. Crée `experiments/`
   avec un fichier `note.md`. Commite. Reviens sur `main`. Observe : `git branch`,
   `git status`, `ls` (le dossier ne doit pas exister sur main !).
4. **Merge** : fusionne `experiments` dans `main`, supprime la branche.
5. **GitHub** : crée un repo sur GitHub, ajoute le remote, push. (Si pas de compte,
   note la commande et poursuis, on le fera ensemble.)
6. **Cycle** : fais une modif, `add`, `commit` avec un message de type `feat:`/`fix:`, push.

---

## 10. Solutions

<details>
<summary>Cliquer pour révéler</summary>

```bash
# Exercice 1
cd ~/Desktop/devIA/formations/beCode
# crée .gitignore (contenu : .venv/, __pycache__/, .DS_Store, etc.)
git init
git add .
git commit -m "Début de la formation : modules 00 à 02"
git log --oneline

# Exercice 2
echo "x" > test_temporaire.txt
git status                      # test_temporaire.txt apparaît (untracked)
echo "test_temporaire.txt" >> .gitignore
git status                      # il n'apparaît plus
git add .gitignore && git commit -m "chore: ignore temporaires"

# Exercice 3
git switch -c experiments
mkdir experiments && echo "mes idées" > experiments/note.md
git add experiments && git commit -m "feat: branche experiments avec note"
git switch main
ls          # experiments n'existe pas ici ; il reviendra au merge

# Exercice 4
git merge experiments
git branch -d experiments
git log --oneline

# Exercice 5
git remote add origin https://github.com/TOI/beCode-formation.git
git push -u origin main

# Exercice 6
echo "# BeCode formation" > README.md
git add .
git commit -m "docs: ajout README"
git push
```

</details>

---

## 11. Récapitulatif & auto-évaluation

Tu peux passer au Module 03 si tu sais :
- [ ] Expliquer working directory / stage / commit.
- [ ] Créer un repo (`init`), `add`, `commit`, lire `git status` et `git log`.
- [ ] Rédiger un `.gitignore` efficace.
- [ ] Créer / basculer / fusionner / supprimer des branches.
- [ ] `push` et `pull` vers GitHub.
- [ ] Écrire des messages de commit clairs.

### Aide-mémoire (cheat sheet)

| Commande | Rôle |
|----------|------|
| `git init` | Créer un repo |
| `git status` | État du repo |
| `git add .` | Préparer tout |
| `git commit -m "msg"` | Valider une photo |
| `git log --oneline` | Historique |
| `git diff` | Changements non stagés |
| `git restore <f>` | Annuler des modifs |
| `git switch -c <b>` | Créer + basculer de branche |
| `git merge <b>` | Fusionner |
| `git push` / `git pull` | Envoyer / récupérer |
| `git clone <url>` | Copier un repo |

**Prochaine étape → Module 03 : Python, les bases.** Dis-moi quand c'est fait et
n'oublie pas de me montrer ton `git log` 😉.