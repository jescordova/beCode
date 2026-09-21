# Module 01 — Terminal & ligne de commande

> **Objectif** : être à l'aise dans le terminal pour naviguer, créer/déplacer/supprimer
> des fichiers, enchaîner des commandes et écrire de petits scripts. Le terminal est
> l'outil n°1 du développeur et du data scientist.

Durée conseillée : ~2 h. **Tape chaque commande toi-même**, c'est le seul moyen.

---

## 1. C'est quoi un terminal ?

Le **terminal** (ou *console*, *shell*) est une fenêtre où tu **écris des commandes**
au lieu de cliquer. La commande est interprétée par un **shell** — sur ton macOS,
c'est **zsh** par défaut.

Pourquoi c'est essentiel en IA / Data Science :
- Lancer des scripts, des notebooks, des entraînements de modèles.
- Installer des bibliothèques (`pip`, `conda`).
- Utiliser Git, Docker, le cloud (AWS, Azure, GCP) — tout se fait en ligne de commande.
- Automatiser des tâches répétitives.

### Vocabulaire bilingue

| English | Français | Idée |
|---------|----------|------|
| Terminal / Console | Terminal / console | La fenêtre |
| Shell | Interpréteur de commandes | Le programme qui lit tes commandes (zsh, bash) |
| Command | Commande | Une instruction tapée |
| Directory / Folder | Répertoire / dossier | Un dossier |
| Path | Chemin | L'adresse d'un fichier/dossier |
| Flag / Option | Option | Un réglage passé à une commande (`-l`, `--help`) |
| Argument | Argument | Ce sur quoi agit la commande |
| Pipe | Tube | Envoyer la sortie d'une commande vers une autre (`|`) |
| Redirect | Redirection | Écrire la sortie dans un fichier (`>`, `>>`) |
| Working directory | Répertoire courant | Là où tu te trouves |

### Anatomie d'une commande

```
   ls      -l       -a       Documents
   │       │        │        │
commande  option  option   argument
```

- Les **options** commencent souvent par `-` (court) ou `--` (long).
- Les **arguments** sont les cibles (fichiers, dossiers).
- Les éléments sont séparés par des **espaces**.

> **Astuce** : la touche `Tab` **complète automatiquement** les noms de fichiers/dossiers.
> Utilise-la tout le temps ! `↑` / `↓` rappellent les commandes précédentes.

---

## 2. Se repérer : où suis-je ?

```bash
pwd            # Print Working Directory : affiche le dossier courant
```

- `pwd` = *print working directory*.

```bash
ls             # liste le contenu du dossier courant
ls -l          # format long (droits, taille, date)
ls -a          # affiche aussi les fichiers cachés (qui commencent par .)
ls -la         # combine les deux
```

- `ls` = *list*.

---

## 3. Se déplacer : `cd`

```bash
cd Documents        # entre dans le dossier Documents (chemin relatif)
cd ..               # remonte d'un niveau (dossier parent)
cd .                # reste ici (le dossier courant)
cd ~                # va dans ton dossier personnel (home)
cd /                # va à la racine du disque
cd -                # retourne au dossier précédent
cd                  # sans argument : retourne au home
```

- `cd` = *change directory*.

### Chemins absolus vs relatifs

| Type | Exemple | Sens |
|------|---------|------|
| **Absolu** | `/Users/petros/Desktop` | Commence par `/` (racine). Marche depuis n'importe où. |
| **Relatif** | `Desktop/devIA` | Part du dossier courant. |
| `~` | `~/Desktop` | Ton dossier personnel (`/Users/petros`). |
| `.` | `.` | Dossier courant. |
| `..` | `..` | Dossier parent. |

> **Retiens** : `.` = ici, `..` = au-dessus, `~` = chez moi.

---

## 4. Créer, copier, déplacer, supprimer

```bash
mkdir mon_dossier           # créer un dossier (make directory)
mkdir -p a/b/c              # créer une arborescence complète (-p = parents)
touch notes.txt             # créer un fichier vide
```

```bash
cp notes.txt copie.txt      # copier un fichier (copy)
cp -r dossier1 dossier2     # copier un dossier (-r = récursif)
mv notes.txt archives/      # déplacer un fichier
mv ancien.txt nouveau.txt   # renommer (mv sert aussi à renommer)
```

```bash
rm fichier.txt              # supprimer un fichier (remove) ⚠️
rm -r mon_dossier           # supprimer un dossier et son contenu ⚠️
rm -i fichier.txt           # demande confirmation avant suppression
```

> ⚠️ **Danger** : `rm` ne met pas à la corbeille, c'est **définitif**.
> N'utilise **jamais** `rm -rf /` (cela détruirait ton système). Prends l'habitude
> de relire ta commande avant d'appuyer sur Entrée.

---

## 5. Lire le contenu d'un fichier

```bash
cat notes.txt        # affiche tout le fichier
less notes.txt       # affiche page par page (q pour quitter) — mieux pour les gros fichiers
head notes.txt       # 10 premières lignes
head -n 3 notes.txt  # 3 premières lignes
tail notes.txt       # 10 dernières lignes
wc -l notes.txt      # compte les lignes (word count)
```

```bash
echo "Bonjour"       # affiche du texte
echo $HOME           # affiche le contenu d'une variable d'environnement
```

---

## 6. Les jokers (wildcards)

```bash
ls *.py              # tous les fichiers .py
ls data_*.csv        # tous les fichiers commençant par data_ et finissant par .csv
ls image?.png        # un seul caractère quelconque (?)
```

- `*` = n'importe quelle suite de caractères.
- `?` = exactement un caractère.

---

## 7. Redirections et pipes (le super-pouvoir)

### Rediriger la sortie vers un fichier

```bash
echo "ligne 1" > fichier.txt     # > écrase le fichier avec la sortie
echo "ligne 2" >> fichier.txt    # >> ajoute à la fin (sans écraser)
ls -la > liste.txt               # enregistre la liste dans un fichier
```

- `>` = *write* (écrase). `>>` = *append* (ajoute).

### Enchaîner avec des pipes

```bash
ls -la | less                    # envoie la sortie de ls vers less
ls | grep ".py"                  # garde seulement les lignes contenant ".py"
cat notes.txt | wc -l            # compte les lignes du fichier
history | tail -n 20             # les 20 dernières commandes tapées
```

- `|` = *pipe* : la sortie de gauche devient l'entrée de droite.
- `grep "motif"` = filtre les lignes contenant le motif.

---

## 8. Aide, historique et nettoyage

```bash
man ls               # manuel de la commande ls (q pour quitter)
ls --help            # aide rapide (souvent plus lisible que man)
history              # historique de tes commandes
clear                # nettoie l'écran (raccourci : Ctrl + L)
```

### Raccourcis clavier indispensables

| Raccourci | Effet |
|-----------|-------|
| `Tab` | Complète automatiquement |
| `↑` / `↓` | Commande précédente / suivante |
| `Ctrl + C` | **Interrompt** la commande en cours (très utilisé !) |
| `Ctrl + L` | Efface l'écran |
| `Ctrl + A` / `Ctrl + E` | Début / fin de la ligne |
| `Ctrl + R` | Recherche dans l'historique |

---

## 9. Écrire un petit script shell

Un **script** = un fichier de commandes que l'on peut relancer.

Crée `bonjour.sh` :

```bash
#!/bin/zsh
# Ceci est un commentaire
echo "Bonjour depuis un script !"
date
pwd
```

- La 1re ligne `#!/bin/zsh` s'appelle le **shebang** : indique quel shell utiliser.

Rends-le exécutable puis lance-le :

```bash
chmod +x bonjour.sh    # ajoute le droit d'exécution
./bonjour.sh           # ./ = "le fichier dans le dossier courant"
```

> Sur macOS, sans `chmod +x`, tu peux toujours lancer avec `zsh bonjour.sh`.

---

## 10. Permissions (aperçu)

Quand tu fais `ls -l`, tu vois par exemple :

```
-rw-r--r--  1 petros  staff  9033 Sep 21 16:12 README.md
```

- `-` = fichier (un `d` = dossier).
- Les 9 caractères = droits pour **User / Group / Others** : `rwx` = *read / write / execute*.

```bash
chmod +x script.sh     # ajouter exécution
chmod 644 fichier.txt  # rw- r-- r-- (droits classiques d'un fichier)
```

Tu n'as pas besoin de tout retenir maintenant : retiens juste `chmod +x`.

---

## 11. Exercices

Travaille dans le dossier `01-terminal/`. Crée un fichier `memo_terminal.md` pour noter
les commandes que tu retiens.

1. **Navigation** : va dans `01-terminal/`, crée un dossier `exercices`, entre dedans,
   affiche `pwd`, puis remonte d'un niveau.
2. **Création** : dans `exercices/`, crée 3 fichiers `a.txt`, `b.txt`, `c.txt` et un
   dossier `data/`. Déplace les 3 fichiers dans `data/`. Liste le résultat.
3. **Écriture** : écris `Bonjour` dans `data/a.txt` (en écrasant), ajoute `le monde`
   sur une 2e ligne, puis affiche le fichier avec `cat`.
4. **Pipe & grep** : affiche le contenu de `data/a.txt` filtré pour ne garder que les
   lignes contenant `Bonjour`.
5. **Nettoyage** : supprime le dossier `exercices` et **tout** son contenu.
6. **Script** : crée `stats.sh` qui affiche la date, le dossier courant et la liste des
   fichiers, puis rends-le exécutable et lance-le.

---

## 12. Solutions

<details>
<summary>Cliquer pour révéler</summary>

```bash
# Exercice 1
cd 01-terminal
mkdir exercices
cd exercices
pwd
cd ..

# Exercice 2
cd exercices
touch a.txt b.txt c.txt
mkdir data
mv a.txt b.txt c.txt data/
ls -la data

# Exercice 3
echo "Bonjour" > data/a.txt
echo "le monde" >> data/a.txt
cat data/a.txt

# Exercice 4
cat data/a.txt | grep "Bonjour"

# Exercice 5
cd ..
rm -r exercices

# Exercice 6
# stats.sh :
#   #!/bin/zsh
#   date
#   pwd
#   ls -la
chmod +x stats.sh
./stats.sh
```

</details>

---

## 13. Récapitulatif & auto-évaluation

Tu peux passer au Module 02 si tu sais :
- [ ] Te repérer avec `pwd`, `ls`, `cd` (relatif, absolu, `~`, `..`).
- [ ] Créer/copier/déplacer/renommer/supprimer fichiers et dossiers.
- [ ] Lire un fichier (`cat`, `less`, `head`, `tail`).
- [ ] Rediriger (`>`, `>>`) et enchaîner avec un pipe (`|`) + `grep`.
- [ ] Interrompre une commande avec `Ctrl + C`.
- [ ] Créer et exécuter un script shell.

### Aide-mémoire (cheat sheet)

| Commande | Rôle |
|----------|------|
| `pwd` | Dossier courant |
| `ls -la` | Lister (tout, format long) |
| `cd chemin` | Se déplacer |
| `mkdir -p a/b` | Créer des dossiers |
| `touch f` | Créer un fichier vide |
| `cp -r src dst` | Copier |
| `mv src dst` | Déplacer / renommer |
| `rm -r dossier` | Supprimer (⚠️ définitif) |
| `cat` / `less` | Lire |
| `head` / `tail` | Début / fin |
| `grep motif` | Filtrer des lignes |
| `\|` | Pipe |
| `>` / `>>` | Écrire / ajouter dans un fichier |
| `chmod +x` | Rendre exécutable |
| `man cmd` | Manuel |

**Prochaine étape → Module 02 : Git & GitHub.** Dis-moi quand les exercices sont
faits (ou envoie-moi tes réponses/`stats.sh`) et on continue.
