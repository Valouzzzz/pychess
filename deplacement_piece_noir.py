from piece_valide import cavalier_valide, tour_valide, fou_valide, dame_valide, roi_valide, sur_le_plateau, piece_blanc, piece_noir, plateau

def pion_valide(avant, apres):
    if str(avant) in "[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]" :
        for i in range(0, 6):
            if apres not in piece_blanc[i]:
                return apres[1] == avant[1] - 1 or apres[1] == avant[1] - 2 or apres == [avant[0] + 1, avant[1] - 1] or apres == [avant[0] - 1, avant[1] - 1]
    else :
        for i in range(0, 6):
            if apres not in piece_blanc[i]:
                return apres[1] == avant[1] - 1 or apres == [avant[0] + 1, avant[1] - 1] or apres == [avant[0] - 1, avant[1] - 1]

def changement_position_noir(avant, apres): 
    """
    Exemple(s) :
    $$$ changement_position_noir([1, 7], [2, 5]) #Pour Cavalier
    [2, 5]
    $$$ changement_position_noir([6, 7], [5, 5]) #Pour Cavalier
    [[2, 5],[5, 5]]
    $$$ changement_position_noir([3, 7], [3, 6]) #Pour Dame
    [3, 6]
    """
    Pion = piece_noir[0]
    Tour = piece_noir[1]
    Cavalier = piece_noir[2]
    Fou = piece_noir[3]
    Dame = piece_noir[4]
    Roi = piece_noir[5]
    if sur_le_plateau(apres):
        if avant in Tour:
            tour = []
            nb = 0
            for t in Tour :
                if avant == t:
                    if tour_valide(avant, apres) and verification_piece_noir(avant, apres, 't'):
                        if nb > 0:
                            piece_noir[1][nb] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[1]
                        if nb == 0:
                            piece_noir[1][0] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[1][0]
                else :
                    nb += 1
                    tour += [t]
        if avant in Cavalier:
            cavalier = []
            nb = 0
            for c in Cavalier :
                if avant == c:
                    if cavalier_valide(avant, apres) and verification_piece_noir(avant, apres, 'c'):
                        if nb > 0:
                            piece_noir[2][nb] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[2]
                        if nb == 0:
                            piece_noir[2][0] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[2][0]
                else :
                    nb += 1
                    cavalier += [c]
        if avant in Fou:
            fou = []
            nb = 0
            for f in Fou :
                if avant == f:
                    if fou_valide(avant, apres) and verification_piece_noir(avant, apres, 'f'):
                        if nb > 0:
                            piece_noir[3][nb] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[3]
                        if nb == 0:
                            piece_noir[3][0] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[3][0]
                else :
                    nb += 1
                    fou += [f]
        if avant in Dame:
            dame = []
            nb = 0
            for d in Dame :
                if avant == d:
                    if dame_valide(avant, apres) and verification_piece_noir(avant, apres, 'd'):
                        if nb > 0:
                            piece_noir[4][nb] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[4]
                        if nb == 0:
                            piece_noir[4][0] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[4][0]
                else :
                    nb += 1
                    dame += [d]
        if avant == Roi:
            if roi_valide(avant, apres) and verification_piece_noir(avant, apres, 'r'):
                piece_noir[5] = apres
                plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                plateau[avant[1]][avant[0]] = ['  ']
                return plateau[avant[1]][avant[0]], piece_noir[5]
        if avant in Pion:
            pion = []
            nb = 0
            for p in Pion :
                if avant == p:
                    if pion_valide(avant, apres) and verification_piece_noir(avant, apres, 'p'):
                        if nb > 0:
                            piece_noir[0][nb] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[0]
                        if nb == 0:
                            piece_noir[0][0] = apres
                            plateau[apres[1]][apres[0]] = plateau[avant[1]][avant[0]]
                            plateau[avant[1]][avant[0]] = ['  ']
                            return plateau[avant[1]][avant[0]], piece_noir[0][0]
                else :
                    nb += 1
                    pion += [p]
        
    
def verification_piece_noir(avant, apres, TYPE):
    """ renvoie True si placement valide !

    Précondition : 
    Exemple(s) :
    $$$ verification_piece_noir([5, 5], [4, 4], 'f')
    True
    $$$ verification_piece_noir([5, 5], [5, 4], 't')
    True
    $$$ verification_piece_noir([5, 5], [5, 4], 'r')
    True
    $$$ verification_piece_noir([5, 5], [6, 7], 'c')
    True
    $$$ verification_piece_noir([5, 5], [6, 7], 'd')
    True
    """
    if TYPE == 't':
        if TYPE_T(avant, apres) == None:
            return True
        else :
            return TYPE_T(avant, apres)
    if TYPE == 'c':
        if TYPE_C(avant, apres) == None:
            return True
        else :
            return TYPE_C(avant, apres)
    if TYPE == 'f':
        if TYPE_F(avant, apres) == None:
            return True
        else :
            return TYPE_F(avant, apres)
    if TYPE == 'r':
        if TYPE_R(avant, apres) == None:
            return True
        else :
            return TYPE_R(avant, apres)
    if TYPE == 'p':
        if TYPE_P(avant, apres) == None:
            return True
        else :
            return TYPE_P(avant, apres)
    if TYPE == 'd':
        return verification_piece_noir(avant, apres, 't') or verification_piece_noir(avant, apres, 'c') or TYPE_F(avant, apres) or verification_piece_noir(avant, apres, 'r')
    
def TYPE_T(avant, apres):
    dif_x = avant[0] - apres[0]
    dif_y = avant[1] - apres[1]
    if avant[1] >= apres[1] or avant[0] >= apres[0]:
        if dif_x != 0:
            for i in range(apres[0]+1, avant[0]+1, 1):
                position = [i, avant[1]]
                for y in range(0, 6):
                    if position in piece_noir[y] and position != avant:
                        return False
            for i in range(apres[0]+1, avant[0], 1):
                position = [i, avant[1]]
                for y in range(0, 6):
                    if position in piece_blanc[y] and position != avant:
                        return False
        elif dif_y != 0:
            for i in range(apres[1], avant[1]+1, 1):
                position = [avant[0], i]
                for y in range(0, 6):
                    if position in piece_noir[y] and position != avant:
                        return False
            for i in range(apres[1], avant[1], 1):
                position = [avant[0], i]
                for y in range(0, 6):
                    if position in piece_blanc[y] and position != avant:
                        return False
    if avant[1] < apres[1] or avant[0] < apres[0]:
        if dif_x != 0:
            for i in range(avant[0]+1, apres[0]+1, 1):
                position = [i, avant[1]]
                for y in range(0, 6):
                    if position in piece_noir[y] and position != avant:
                        return False
            for i in range(avant[0]+1, apres[0], 1):
                position = [i, avant[1]]
                for y in range(0, 6):
                    if position in piece_blanc[y] and position != avant:
                        return False
        elif dif_y != 0:
            for i in range(avant[1]+1, apres[1]+1, 1):
                position = [avant[0], i]
                for y in range(0, 6):
                    if position in piece_noir[y] and position != avant:
                        return False
            for i in range(avant[1], apres[1]+1, 1):
                position = [avant[0], i]
                for y in range(0, 6):
                    if position in piece_blanc[y] and position != avant:
                        return False
                
def TYPE_C(avant, apres):
    if cavalier_valide(avant, apres):
        for y in range(0, 6):
            if apres in piece_noir[y]:
                return False
            
def TYPE_F(avant, apres):
    deplacement_x = apres[0] - avant[0]
    deplacement_y = apres[1] - avant[1]
    if deplacement_x > 0 and deplacement_y > 0:
        for i in range(1, int(deplacement_x)+1, 1):
            position = [avant[0]+i, avant[1]+i]
            for y in range(0, 6):
                if position in piece_noir[y] and position != avant:
                    return False
        for i in range(1, int(deplacement_x), 1):
            position = [avant[0]+i, avant[1]+i]
            for y in range(0, 6):
                if position in piece_blanc[y] and position != avant:
                    return False
    if deplacement_x < 0 and deplacement_y < 0:
        for i in range(-1, int(deplacement_x)-1, -1):
            position = [avant[0]+i, avant[1]+i]
            for y in range(0, 6):
                if position in piece_noir[y] and position != avant:
                    return False
        for i in range(-1, int(deplacement_x), -1):
            position = [avant[0]+i, avant[1]+i]
            for y in range(0, 6):
                if position in piece_blanc[y] and position != avant:
                    return False
    if deplacement_x > 0 and deplacement_y < 0:
        for i in range(1, int(deplacement_x)+1, 1):
            position = [avant[0]+i, avant[1]+(i*-1)]
            for y in range(0, 6):
                if position in piece_noir[y] and position != avant:
                    return False
        for i in range(1, int(deplacement_x), 1):
            position = [avant[0]+i, avant[1]+(i*-1)]
            for y in range(0, 6):
                if position in piece_blanc[y] and position != avant:
                    return False
    if deplacement_x < 0 and deplacement_y > 0:
        for i in range(-1, int(deplacement_x)-1, -1):
            position = [avant[0]+i, avant[1]+(i*-1)]
            for y in range(0, 6):
                if position in piece_noir[y] and position != avant:
                    return False
        for i in range(-1, int(deplacement_x), -1):
            position = [avant[0]+i, avant[1]+(i*-1)]
            for y in range(0, 6):
                if position in piece_blanc[y] and position != avant:
                    return False
                
def TYPE_R(avant, apres):
    for y in range(0, 6):
        if apres in piece_noir[y] and position != avant:
            return False
        
        
def TYPE_P(avant, apres):
    for y in range(0, 6):
        if apres in piece_noir[y] and position != avant:
            return False