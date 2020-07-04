from copy import deepcopy


def init(n):
    return [list(range(n, 0, -1)), [], []]


def nombre_disques(plateau, numtour):
    return len(plateau[numtour])


def disque_superieur(plateau, numtour):
    if not plateau[numtour]:
        return -1
    else:
        return min(plateau[numtour])

    
def position_disque(plateau, numtour):
    for tour in plateau:
        if numtour in tour:
            return plateau.index(tour)

        
def verifier_deplacement(plateau, pi, pf):
    if plateau[pi] and (not plateau[pf] or position_disque(plateau, pf) > position_disque(plateau, pi)):
        return True
    else:
        return False


def verifier_victoire(plateau, n):
    if plateau == [[], [], list(range(n, 0, -1))]:
        return True
    else:
        return False


def lire_coords(plateau):

    while True:
        try:
            tour_depart = int(input("Donnez la tour de depart: "))
            if tour_depart > 2 or tour_depart < 0:
                print('Veuillez saisir la bonne tour de depart! Entre 0 et 2')
            elif not plateau[tour_depart]:
                print('Veuillez saisir la bonne tour de depart! Celle-la est vide!')
            else:
                break
        except ValueError:
            print('Be carefull of pressing wrong buttons.')
    while True:
        try:
            tour_arrivee = int(input("Donnez la tour d'arrivee: "))
            if tour_arrivee > 2 or tour_arrivee < 0:
                print("Veuillez saisir la bonne tour d'arrivee! Entre 0 et 2")
            elif plateau[tour_arrivee] and (min(plateau[tour_depart]) > min(plateau[tour_arrivee])):
                print(
                    "Veuillez saisir la bonne tour d'arrivee! Celle-la contient un disque plus petit!")
            else:
                break
        except ValueError:
            print('Be carefull of pressing wrong buttons.')
    return tour_depart, tour_arrivee


def jouer_un_coup(plateau, n):
    pi, pf = lire_coords(plateau)
    plateau[pf].append(plateau[pi][-1])
    del plateau[pi][-1]
    return plateau


def boucle_jeu(plateau, n):
    compteur = 0
    gagne = False
    coups = dict()
    coups[compteur] = deepcopy(plateau)
    print(f'{coups}')
    while True:
        compteur += 1
        plateau_copied = jouer_un_coup(deepcopy(coups[compteur-1]), n)
        coups[compteur] = deepcopy(plateau_copied)
        print(f'{coups}')
        annul = input('Voulez vous annulez votre coup (y/n)?  ')
        if annul.lower() == 'y':
            del coups[compteur]
            compteur -= 1
            print(f'{coups}')
        else:
            pass
        if compteur == (n ^ 2 + 1):
            print(f'Partie jouée en {compteur} coups. Trop de coup! {gagne}')
            return coups
        if verifier_victoire(coups[compteur], n):
            gagne = True
            print(f'Gagné en {compteur} coups, {gagne}')
            return coups


nombre = int(input("Donnez le nombre de disques: "))
coups = boucle_jeu(init(nombre), nombre)
print(coups)
