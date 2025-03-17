
# Pendu

"Pendu" est une implémentation simple du jeu du pendu en Python. Ce projet propose une version console où le joueur doit deviner un mot choisi aléatoirement parmi une liste prédéfinie. Avec un nombre limité de tentatives, le joueur doit proposer des lettres pour révéler progressivement le mot.

## Fonctionnalités
- **Choix aléatoire du mot :** Utilisation du module `random` pour sélectionner un mot dans une liste.
- **Affichage dynamique :** Le mot à deviner est affiché avec des underscores pour les lettres non encore trouvées.
- **Gestion des tentatives :** Le joueur dispose de 6 essais pour trouver le mot.
- **Feedback interactif :** Le jeu indique si la lettre proposée est présente ou non dans le mot.
- **Fin de partie :** Le jeu se termine lorsque le mot est entièrement découvert ou que les tentatives sont épuisées.

## Prérequis
- **Python 3.x** doit être installé sur votre machine. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/downloads/).

## Installation
1. **Cloner le dépôt ou télécharger le code source :**

   ```bash
   git clone 
   cd pendu
   ```

2. **(Optionnel) Créer un environnement virtuel :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Pas de dépendances externes :**  
   Le projet n'utilise que les bibliothèques standard de Python.

## Lancement du Jeu
Pour lancer le jeu, exécutez simplement le fichier principal :

```bash
python3 pendu.py
```

Suivez ensuite les instructions affichées dans le terminal pour jouer.

## Comment Jouer
1. **Déroulement :**  
   Le jeu affiche un mot dont certaines lettres sont masquées par des underscores.
   
2. **Entrée utilisateur :**  
   Vous devez entrer une lettre pour tenter de révéler une partie du mot.
   
3. **Vérification :**  
   - Si la lettre est présente, elle sera affichée aux emplacements correspondants.
   - Sinon, une tentative est perdue.
   
4. **Objectif :**  
   Deviner l'intégralité du mot avant d'épuiser les 6 tentatives.

## Structure du Code
- **Import et sélection du mot :**  
  Le module `random` est utilisé pour choisir aléatoirement un mot depuis la liste `liste_mots`.

- **Affichage du mot à deviner :**  
  La fonction `afficher_mot` affiche le mot en masquant les lettres non trouvées avec des underscores.

- **Logique principale :**  
  La fonction `jeu` gère la boucle principale du jeu, interroge le joueur et vérifie ses propositions de lettres.

- **Gestion de la fin de partie :**  
  Le jeu se termine lorsque toutes les lettres du mot sont découvertes ou lorsque le nombre de tentatives restantes atteint zéro.

## Améliorations Futures
- **Interface Graphique :**  
  Ajouter une interface utilisateur graphique (GUI) avec Tkinter ou Pygame.
  
- **Niveaux de difficulté :**  
  Varier le nombre de tentatives ou la complexité des mots selon le niveau choisi.
  
- **Extension de la liste de mots :**  
  Charger la liste de mots depuis un fichier externe (texte, CSV, JSON) ou une API.

## Licence
Ce projet est distribué sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

