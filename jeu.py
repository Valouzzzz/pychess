from deplacement_piece_blanc import changement_position_blanc, piece_blanc
from deplacement_piece_noir import changement_position_noir, piece_noir
from piece_valide import plateau 


def promotion_blanc(avant, apres):
    if (apres in piece_blanc[0]) and (apres[1] == 7):
        promotion = input("en quoi ? T, C, F ou D ")
        if promotion == 'T':
            for element in piece_blanc:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
                    piece_blanc[1] += [apres]
                    plateau[apres[1]][apres[0]] = ['Tb']
        if promotion == 'C':
            for element in piece_blanc:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
                    piece_blanc[2] += [apres]
                    plateau[apres[1]][apres[0]] = ['Cb']
        if promotion == 'F':
            for element in piece_blanc:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
                    piece_blanc[3] += [apres]
                    plateau[apres[1]][apres[0]] = ['Fb']
        if promotion == 'D':
            for element in piece_blanc:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
                    piece_blanc[4] += [apres]
                    plateau[apres[1]][apres[0]] = ['Db']

def promotion_noir(avant, apres):
    if (apres in piece_noir[0]) and (apres[1] == 0):
        promotion = input("en quoi ? T, C, F ou D ")
        if promotion == 'T':
            for element in piece_noir:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
                    piece_noir[1] += [apres]
                    plateau[apres[1]][apres[0]] = ['Tr']
        if promotion == 'C':
            for element in piece_noir:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
                    piece_noir[2] += [apres]
                    plateau[apres[1]][apres[0]] = ['Cr']
        if promotion == 'F':
            for element in piece_noir:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
                    piece_noir[3] += [apres]
                    plateau[apres[1]][apres[0]] = ['Fr']
        if promotion == 'D':
            for element in piece_noir:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
                    piece_noir[4] += [apres]
                    plateau[apres[1]][apres[0]] = ['Dr']
                    

def reponce(a):
    liste = []
    conv = []
    for i in a :
        liste += i
    if liste[0] == "A":
        conv = [0] + [int(liste[1])-1]
        return conv
    if liste[0] == "B":
        conv = [1] + [int(liste[1])-1]
        return conv
    if liste[0] == "C":
        conv = [2] + [int(liste[1])-1]
        return conv
    if liste[0] == "D":
        conv = [3] + [int(liste[1])-1]
        return conv
    if liste[0] == "E":
        conv = [4] + [int(liste[1])-1]
        return conv
    if liste[0] == "F":
        conv = [5] + [int(liste[1])-1]
        return conv
    if liste[0] == "G":
        conv = [6] + [int(liste[1])-1]
        return conv
    if liste[0] == "H":
        conv = [7] + [int(liste[1])-1]
        return conv


def main():
    print("*********\nDebut du jeu :")
    print(f"{plateau[7]}8\n{plateau[6]}7\n{plateau[5]}6\n{plateau[4]}5\n{plateau[3]}4\n{plateau[2]}3\n{plateau[1]}2\n{plateau[0]}1\n[[ A ],  [ B ],  [ C ],  [ D ],  [ E ],  [ F ],  [ G ],  [ H ]]")
    for i in range(0, 100):
        piece = str(input("Piece que J1 veux bouger : "))
        ou = str(input("ou : "))
        avant = reponce(piece)
        #print(avant)
        apres = reponce(ou)
        #print(apres)
        if changement_position_blanc(avant, apres) == None :
            return f"pas possible"
        else :
            changement_position_blanc(avant, apres)
            for element in piece_noir:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
            promotion_blanc(avant, apres)
        print(f"{plateau[7]}8\n{plateau[6]}7\n{plateau[5]}6\n{plateau[4]}5\n{plateau[3]}4\n{plateau[2]}3\n{plateau[1]}2\n{plateau[0]}1\n[[ A ],  [ B ],  [ C ],  [ D ],  [ E ],  [ F ],  [ G ],  [ H ]]")
        print("*********")
        piece = str(input("Piece que J2 veux bouger : "))
        ou = str(input("ou : "))
        avant = reponce(piece)
        #print(avant)
        apres = reponce(ou)
        #print(apres)
        if changement_position_noir(avant, apres) == None :
            return f"pas possible"
        else :
            changement_position_noir(avant, apres)
            for element in piece_blanc:
                if isinstance(element, list) and apres in element:
                    element.remove(apres)
            promotion_noir(avant, apres)
        print(f"{plateau[7]}8\n{plateau[6]}7\n{plateau[5]}6\n{plateau[4]}5\n{plateau[3]}4\n{plateau[2]}3\n{plateau[1]}2\n{plateau[0]}1\n[[ A ],  [ B ],  [ C ],  [ D ],  [ E ],  [ F ],  [ G ],  [ H ]]")
        print("*********")

    
    

if __name__ == '__main__':
    main()