# Pendu

# Import de random pour choisir un mot au hasard
import random

# definir la liste de mots
liste_mots = ["arbre", "maison", "voiture", "oiseau", "vent", "gourde", "python"]


# Function pour choisir un mot aléatoirement
def choisir_mot():
    return random.choice(liste_mots).lower()


# Function pour afficher les lettres trouvees et remplace les lettres manquantes par des underscores
def afficher_mot(mot_a_trouver, lettres_trouvees):
    return " ".join(
        lettre if lettre in lettres_trouvees else "_" for lettre in mot_a_trouver
    )


# Fonction principale du jeu
def jeu():
    mot_a_trouver = choisir_mot()  # choisir un mot aléatoirement
    lettres_trouvees = set()  # set pour stocker les lettres trouvées
    tentatives_restantes = 6  # nombre de tentatives restantes

    # Boucle principale du jeu
    while (
        tentatives_restantes > 0
    ):  # tant que les tentatives restantes sont plus grandes que 0

        mot_actuel = afficher_mot(mot_a_trouver, lettres_trouvees)
        print(f"\nMot :", {mot_actuel})
        print(f"Tentatives restantes : {tentatives_restantes}")

        # Demander une lettre au joueur
        lettre = input("Entrez une lettre : ").lower()

        # Verifier si la lettre est dans le mot
        if lettre in mot_a_trouver and len(lettre) == 1:
            lettres_trouvees.add(lettre)
            print(f"Bravo, la lettre {lettre} est dans le mot.")
        else:
            tentatives_restantes -= 1
            print(f"La lettre {lettre} n'est pas dans le mot.")

        # Verifier si le joueur a trouvé le mot
        if lettres_trouvees == set(mot_a_trouver):
            print(f"\nBravo, vous avez trouve le mot : {mot_a_trouver}.")
            return  # sortir de la fonction jeu() si trouvé

    # si le joueur a utilisé toutes ses tentatives
    print(f"Le mot a trouver etait : {mot_a_trouver}. Vous avez perdu.")


jeu()  # lancer le jeu
