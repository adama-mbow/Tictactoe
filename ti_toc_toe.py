import random


tableau_jeu = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"] #créer le tableau de jeu
joueur_actuel = "X" # vriable joueur actuel est l'utilisateur
gangant = None
game = True

# Table de jeu
def printTable(tableau_jeu): #créer une fonction tableau_jeu qui permet à son appel d'avoir le tableau de jeu
    print(tableau_jeu[0] + " | " + tableau_jeu[1] + " | " + tableau_jeu[2])
    print("---------")
    print(tableau_jeu[3] + " | " + tableau_jeu[4] + " | " + tableau_jeu[5])
    print("---------")
    print(tableau_jeu[6] + " | " + tableau_jeu[7] + " | " + tableau_jeu[8])


# creer une fonction qui demande au jour actuelle de meettre une valeur entre 1 et 9
def joueurInput(tableau_jeu):
    entre_chiffre = int(input("choisissez une place 1-9: "))
    if tableau_jeu[entre_chiffre-1] == "-": # si la valeur entrer par le jour actuel est different des valeur 1 à 9, on reste sur le meme joueur
        tableau_jeu[entre_chiffre-1] = joueur_actuel
    else:
        print("Oops c'est à votre tour.")


# verifier si le joueur actuel a gagné ou perdu
def Horizontle(tableau_jeu): #verifier l'égalité horizontal 
    global gangant
    if tableau_jeu[0] == tableau_jeu[1] == tableau_jeu[2] and tableau_jeu[0] != "-":
        gangant = tableau_jeu[0]
        return True
    elif tableau_jeu[3] == tableau_jeu[4] == tableau_jeu[5] and tableau_jeu[3] != "-":
        gangant = tableau_jeu[3]
        return True
    elif tableau_jeu[6] == tableau_jeu[7] == tableau_jeu[8] and tableau_jeu[6] != "-":
        gangant = tableau_jeu[6]
        return True

def vertical(tableau_jeu): #verifier l'égalité verticale
    global gangant
    if tableau_jeu[0] == tableau_jeu[3] == tableau_jeu[6] and tableau_jeu[0] != "-":
        gangant = tableau_jeu[0]
        return True
    elif tableau_jeu[1] == tableau_jeu[4] == tableau_jeu[7] and tableau_jeu[1] != "-":
        gangant = tableau_jeu[1]
        return True
    elif tableau_jeu[2] == tableau_jeu[5] == tableau_jeu[8] and tableau_jeu[2] != "-":
        gangant = tableau_jeu[3]
        return True


def Diagonal(tableau_jeu): # vérifier le diagonal
    global winner
    if tableau_jeu[0] == tableau_jeu[4] == tableau_jeu[8] and tableau_jeu[0] != "-":
        gangant = tableau_jeu[0]
        return True
    elif tableau_jeu[2] == tableau_jeu[4] == tableau_jeu[6] and tableau_jeu[4] != "-":
        gangant = tableau_jeu[2]
        return True


def checkIfWin(tableau_jeu):
    global game
    if Horizontle(tableau_jeu):
        printTable(tableau_jeu)
        print(f"le gagnant est {gangant}!")
        game = False

    elif vertical(tableau_jeu):
        printTable(tableau_jeu)
        print(f"Le gagnat est {gangant}!")
        game = False

    elif Diagonal(tableau_jeu):
        printTable(tableau_jeu)
        print(f"Le gagnant est {gangant}!")
        game = False


def checkIfTie(tableau_jeu):
    global game
    if "-" not in tableau_jeu:
        printTable(tableau_jeu)
        print("Egalité!")
        game = False


# tour de jeu
def switchjoueur():
    global joueur_actuel
    if joueur_actuel == "X":
        joueur_actuel = "O"
    else:
        joueur_actuel = "X"


def computer(tableau_jeu):
    while joueur_actuel == "O":
        position = random.randint(0, 8)
        if tableau_jeu[position] == "-":
            tableau_jeu[position] = "O"
            switchjoueur()


while game:
    printTable(tableau_jeu)
    joueurInput(tableau_jeu)
    checkIfWin(tableau_jeu)
    checkIfTie(tableau_jeu)
    switchjoueur()
    computer(tableau_jeu)
    checkIfWin(tableau_jeu)
    checkIfTie(tableau_jeu)