# MyXhibit

![Status](https://img.shields.io/badge/status-active-green.svg)
![Statut](https://img.shields.io/badge/statut-phase%20de%20conception%20et%20de%20d%C3%A9veloppement-yellow.svg)
![License](https://img.shields.io/badge/license-CC--BY--NC--ND--4.0-blue.svg)

**MyXhibit** est une application Web permettant de gérer, organiser et partager des œuvres d'art et des expositions. Elle offre une interface intuitive pour explorer, enrichir et partager des collections d'art tout en respectant les droits d'auteur des œuvres.

⚠️ Statut du projet : Ce projet est actuellement en phase de conception et de développement. Des fonctionnalités peuvent évoluer au fil du temps.

---

## Table des matières
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Auteurs](#auteurs)

---

## Fonctionnalités principales

### 1. Gestion des œuvres d'art
- Ajouter et gérer des informations détaillées sur les œuvres d'art.
- Informations : image, titre, artiste(s), technique(s), description, date, etc.

### 2. Gestion des expositions numériques
- Créer et organiser des expositions publiques ou privées.
- Œuvres d'art sélectionnées en fonction de thèmes et d'artistes.

### 3. Recherche dynamique
- Rechercher des œuvres, des artistes et des expositions par différents critères.

### 4. Interaction entre utilisateurs
- Suivre, aimer, commenter et échanger des messages avec d'autres utilisateurs.

---

## Technologies utilisées

MyXhibit est développé avec une architecture MVC (Modèle-Vue-Contrôleur), permettant une séparation claire entre la logique métier, l'affichage et la gestion des données.

### Backend
- **Python** avec **Flask** : Framework léger pour le développement web.
- **SQLAlchemy** : ORM pour la gestion de la base de données
- **Flask-Login** : Gestion de l'authentification des utilisateurs.

### Base de données
- MySQL : Gestion des données des œuvres, utilisateurs et expositions.

### Frontend
- **HTML5** : Structure des pages web.
- **CSS3** : Mise en forme et animations.
- **JavaScript (ES6+)** : Interactions dynamiques côté client.
- **Jinja2** : Moteur de templates pour l'intégration dynamique du contenu.

---

## Installation

1. Clonez ce repository :
   ```bash
   git clone https://github.com/votre-utilisateur/myxhibit.git
   ```

2. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

3. Configurez la base de données MySQL et mettez à jour les paramètres dans le fichier `.env`.

4. Lancez l'application :
   ```bash
   python app.py
   ```

5. L'application sera disponible à l'adresse [http://localhost:5000](http://localhost:5000).

---

## Utilisation

Une fois l'application lancée, vous pouvez :
- Créer un profil utilisateur.
- Ajouter des œuvres d'art et créer des expositions numériques.
- Explorer et interagir avec des œuvres et des expositions publiques.
- Suivre d'autres utilisateurs et participer à des discussions.

---

## Contribuer

Les contributions sont les bienvenues ! Pour proposer une amélioration, veuillez suivre ces étapes :

1. Fork ce repository.
2. Créez une nouvelle branche pour votre fonctionnalité (`git checkout -b nouvelle-fonctionnalité`).
3. Effectuez vos modifications.
4. Soumettez un pull request.

---

## Licence

Ce projet est sous la licence **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.

### Conditions :
- **Attribution** : Vous devez donner crédit à l'auteur de manière appropriée.
- **NonCommercial** : Vous ne pouvez pas utiliser ce projet à des fins commerciales.
- **Pas de modifications** : Vous ne pouvez pas modifier ou redistribuer ce code sous une forme modifiée.

Pour consulter la licence complète, veuillez visiter le fichier [LICENSE](./LICENSE) ou suivre ce lien vers la [licence complète CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).

---

## Auteurs

- **Clémence LOSA** (Clem-V507) - Développeuse principale
