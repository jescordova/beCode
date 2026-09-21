# 11 EXERCICES
## COMMANDES
- touch memo_terminal.md

## 1, NAVIGATION
```bash
cd 01-terminal
mkdir exercices
cd exercices
pwd
cd ..
```

## 2. CRÉATION
```bash
cd exercices
touch a.txt b.txt c.txt
mkdir data
mv *.txt data
ls -la data/
```

## 3. ÉCRITURE
```bash
echo "Bonjour" > data/a.txt
echo "le monde" >> data/a.txt
cat data/a.txt
```

## 4. PIPE & GREP
```bash
cat data/a.txt | grep "Bonjour"
```

## 5. NETTOYAGE
```bash
cd ..
rm -r exercices
```

## 6. SCRIPT
```zsh
touch stats.sh 
#!/bin/zsh
date
pwd
ls -la
zsh stats.sh 
# ou
chmod +x stats.sh
./stats.sh
```