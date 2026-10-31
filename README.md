# Séance Python — Création et manipulation d'une pile

## 1. Présentation du projet

**Nom du projet :** `2026_seance_stack`

Ce projet pédagogique a pour objectif de mettre en œuvre les listes Python afin de créer et de manipuler une structure de données appelée **pile**.

Une pile fonctionne selon le principe LIFO (*Last In, First Out*), ce qui signifie que le dernier élément ajouté est le premier élément retiré.

Les stagiaires devront concevoir eux-mêmes les fonctions permettant de gérer cette structure, sans utiliser directement les méthodes `append()` et `pop()` de Python pour manipuler les éléments de la pile.

## 2. Objectifs pédagogiques

À l'issue de cette séance, vous serez capable de :

- comprendre le fonctionnement d'une pile ;
- utiliser une liste Python pour représenter une structure de données ;
- manipuler les indices d'une liste ;
- concevoir une fonction constructeur ;
- développer des fonctions spécialisées ;
- utiliser des conditions pour contrôler les opérations ;
- gérer les erreurs à l'aide de codes numériques ;
- tester et documenter un module Python.

## 3. Prérequis

Cette séance nécessite de connaître les notions suivantes :

- les variables et les types de données ;
- les listes Python et leurs indices ;
- les conditions ;
- les fonctions, leurs paramètres et leurs valeurs de retour ;
- les instructions d'affichage et de saisie ;
- les tests d'un programme Python.

## 4. Représentation de la pile

La pile sera représentée par une liste Python.

Les trois premières cellules seront réservées à la gestion de la structure.

| Indice | Rôle | Exemple |
|---:|---|---|
| `0` | Capacité maximale | `5` |
| `1` | Code de la dernière erreur | `0` |
| `2` | Taille actuelle | `3` |
| `3` et suivants | Éléments empilés | `"A"`, `"B"`, `"C"` |

Pour une capacité maximale de `5`, la liste contiendra `8` cellules : trois cellules de gestion et cinq emplacements pour les éléments.

La longueur de la liste restera constante pendant les opérations. Seule la taille actuelle évoluera en fonction des ajouts et des retraits.

### Codes d'erreur

| Code | Signification |
|---:|---|
| `0` | Aucune erreur |
| `1` | Capacité maximale invalide |
| `2` | Pile pleine |
| `3` | Pile vide |
| `4` | Structure de pile invalide |

Ces codes devront être utilisés conformément aux règles de gestion définies pendant la séance.

## 5. Fonctions à développer

Le module `stack.py` devra contenir les sept fonctions suivantes.

### 5.1. `create_stack(max_size)`

Crée et initialise une pile.

La fonction devra :

- vérifier que la capacité maximale est un entier strictement positif ;
- initialiser le code d'erreur à `0` ;
- initialiser la taille actuelle à `0` ;
- réserver les emplacements destinés aux éléments.

### 5.2. `push(stack, element)`

Ajoute un élément au sommet de la pile.

La fonction devra vérifier que la pile n'est pas pleine avant d'effectuer l'ajout.

### 5.3. `pop(stack)`

Retire et retourne l'élément situé au sommet de la pile.

La fonction devra vérifier que la pile n'est pas vide, mettre à jour sa taille et libérer l'emplacement utilisé.

### 5.4. `peek(stack)`

Retourne l'élément situé au sommet sans le retirer.

La taille et le contenu de la pile devront rester inchangés.

### 5.5. `size(stack)`

Retourne le nombre d'éléments actuellement présents dans la pile.

### 5.6. `is_empty(stack)`

Retourne `True` si la pile est vide et `False` dans le cas contraire.

### 5.7. `is_full(stack)`

Retourne `True` si la pile a atteint sa capacité maximale et `False` dans le cas contraire.

## 6. Mini-projet : UndoStack

Les fonctions développées seront réutilisées dans une application en mode console permettant de gérer un historique d'actions.

L'application devra proposer les fonctionnalités suivantes :

1. Enregistrer une action dans l'historique.
2. Annuler la dernière action enregistrée.
3. Consulter la dernière action.
4. Afficher le nombre d'actions enregistrées.
5. Vérifier si l'historique est vide.
6. Vérifier si l'historique est plein.
7. Afficher les actions enregistrées.
8. Quitter l'application.

La capacité maximale de l'historique sera définie lors de sa création.

**Règle de gestion :** la dernière action enregistrée sera la première à être annulée.

Cette première version simulera l'annulation des actions. Elle ne nécessitera pas la modification réelle d'un document.

## 7. Organisation du projet

Le projet pourra être organisé de la manière suivante :

```text
2026_seance_stack/
│
├── stack.py
├── main.py
├── test_stack.py
└── README.md
```

- `stack.py` : contient les sept fonctions de gestion de la pile.
- `main.py` : contient le programme principal et le menu console.
- `test_stack.py` : regroupe les tests des fonctions.
- `README.md` : présente le projet et sa documentation.

## 8. Plan de tests

Les tests devront notamment couvrir les situations suivantes :

| Test | Situation | Résultat attendu |
|---|---|---|
| T01 | Création d'une pile valide | Pile initialisée, taille égale à `0` |
| T02 | Création avec une capacité invalide | Erreur `1` |
| T03 | Ajout d'un élément | Taille incrémentée |
| T04 | Consultation du sommet | Élément retourné, pile inchangée |
| T05 | Retrait d'un élément | Élément retourné, taille décrémentée |
| T06 | Retrait d'une pile vide | Erreur `3` |
| T07 | Ajout dans une pile pleine | Erreur `2` |
| T08 | Vérification d'une pile vide | Résultat booléen correct |
| T09 | Vérification d'une pile pleine | Résultat booléen correct |
| T10 | Réutilisation d'un emplacement libéré | Ajout effectué au bon indice |

Les tests devront également vérifier que la taille ne devient jamais négative et ne dépasse jamais la capacité maximale.

## 9. Contraintes techniques

- Langage : Python 3.
- Environnement de développement : PyCharm ou environnement équivalent.
- Structure de données : liste Python.
- Interface : mode console.
- Documentation : docstrings pour les fonctions.
- Gestion des erreurs : codes numériques stockés dans la cellule d'indice `1`.

Pour cette séance, les éléments seront manipulés directement par leurs indices dans la liste. L'utilisation de `append()` et de `pop()` pour gérer les éléments de la pile n'est pas autorisée.

Les fonctions devront avoir des responsabilités clairement définies et respecter les règles de gestion de la pile.

## 10. Critères de validation

Le projet sera considéré comme terminé lorsque :

- les sept fonctions seront réalisées ;
- les opérations respecteront le principe LIFO ;
- les cas de pile vide et de pile pleine seront gérés ;
- la taille sera correctement mise à jour ;
- les codes d'erreur seront cohérents ;
- les tests auront été exécutés ;
- l'application console permettra de gérer un historique d'actions ;
- le code sera documenté et le README complété.

## 11. Pour aller plus loin

Une évolution possible consistera à ajouter une seconde pile permettant de rétablir une action précédemment annulée.

Cette amélioration permettra de découvrir le mécanisme `Undo/Redo`, présent dans de nombreux éditeurs de texte et logiciels de création.

---

**Projet pédagogique — CodeEnJava**

*Apprendre à concevoir une structure de données en Python en mobilisant les notions déjà étudiées.*
