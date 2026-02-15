 # classicmodels-analysis

Ce projet analyse la base de données ClassicModels à l’aide de SQL et Python.  
L’objectif est de réaliser des analyses, de documenter les requêtes SQL et de créer des visualisations afin de présenter des statistiques métiers.

---

 Prérequis

Les logiciels suivants doivent être installés :

- MySQL Server
- MySQL Workbench
- Python 3.11 ou version ultérieure avec `pip`
- Git

---

# Étape 1 — Installation de MySQL

1. Télécharger MySQL Server et MySQL Workbench depuis :
   https://dev.mysql.com/downloads/

2. Installer MySQL Server et définir un mot de passe pour l’utilisateur root.

3. Installer MySQL Workbench.

4. Ouvrir MySQL Workbench et se connecter au serveur MySQL local.

---

## Étape 2 — Importation de la base ClassicModels

1. Télécharger le fichier `classicmodels.sql`.

2. Dans MySQL Workbench :
   - Ouvrir MySQL Workbench
   - Aller dans **Server → Data Import**
   - Sélectionner **Import from Self-Contained File**
   - Choisir le fichier `classicmodels.sql`
   - Définir le **Target Schema** sur `classicmodels`
   - Cliquer sur **Start Import**

3. Vérifier l’import avec la requête suivante :
```sql
USE classicmodels;
SHOW TABLES;
```
--- 
## Étape 3 — Clonage du dépôt GitHub

1. Cloner le dépôt avec les commandes suivantes :

```bash
git clone https://github.com/YOUR_USERNAME/classicmodels-analysis.git

cd classicmodels-analysis
```
---

## Étape 4 — Installation des dépendances Python

Installer les dépendances Python avec :
```bash
pip install -r requirements.txt
```
Ou manuellement :

```bash
pip install pandas matplotlib mysql-connector-python
```
---

## Étape 5 — Structure du projet

Le projet est organisé de la manière suivante :

database/
  schema/
  queries/
  classicmodels.mwb

src/
  database/
  analysis/
  exports/

notebooks/
visualizations/
docs/
reports/
config/

--- 

## Étape 6 — Exécution des scripts SQL

Toutes les requêtes SQL d’analyse sont stockées dans :

database/queries/

Ouvrir chaque fichier .sql dans MySQL Workbench et exécuter les requêtes.

---

## Étape 7 — Exécution des scripts Python

Les scripts Python d’analyse sont stockés dans :

src/analysis/

Pour exécuter un script :
```bash
python src/analysis/nom_du_script.py

Ces scripts se connectent à MySQL, exécutent les requêtes SQL et génèrent des visualisations.
```
---

## Étape 8 — Visualisations

Les graphiques générés sont sauvegardés dans :

visualizations/

Ces graphiques sont utilisés
pour présenter les résultats.

Auteur : ALAOUI MRANI Salma — Étudiante en M1 BIDABI