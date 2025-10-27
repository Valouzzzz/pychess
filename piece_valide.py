def cavalier_valide(avant, apres):
    return (apres[0] == avant[0]+1 and (apres[1] == avant[1]+2 or apres[1] == avant[1]-2)) or (apres[0] == avant[0]+2 and (apres[1] == avant[1]+1 or apres[1] == avant[1]-1)) or (apres[0] == avant[0]-1 and (apres[1] == avant[1]+2 or apres[1] == avant[1]-2)) or (apres[0] == avant[0]-2 and (apres[1] == avant[1]+1 or apres[1] == avant[1]-1))

def tour_valide(avant, apres):
    deplacement_x = apres[0] - avant[0]
    deplacement_y = apres[1] - avant[1]
    return (apres[0] == avant[0] and apres[1] == avant[1]+deplacement_y) or (apres[1] == avant[1] and apres[0] == avant[0]+deplacement_x)

def fou_valide(avant, apres):
    deplacement_x = apres[0] - avant[0]
    deplacement_y = apres[1] - avant[1]
    return abs(deplacement_x) == abs(deplacement_y)
    
def dame_valide(avant, apres):
    return fou_valide(avant, apres) or tour_valide(avant, apres) or cavalier_valide(avant, apres)

def roi_valide(avant, apres):
    return (apres[0] == avant[0]+1 or apres[0] == avant[0]-1) or (apres[1] == avant[1]+1 or apres[1] == avant[1]-1) or (apres[0] == avant[0]+1 and apres[1] == avant[1]+1 or apres[1] == avant[1]-1) or (apres[0] == avant[0]-1 and apres[1] == avant[1]+1 or apres[1] == avant[1]-1)
    
    
"""
print(cavalier_valide([3, 5], [4, 7]))
print(tour_valide([3, 5], [6, 5]))
print(fou_valide([3, 5], [5, 7]))
print(roi_valide([3, 5], [4, 6]))
"""

def sur_le_plateau(apres):
    return apres[0] < 8 and apres[1] < 8
    

piece_blanc = [[[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]], #Pion
              [[0, 0], [7, 0]], #Tour
              [[1, 0], [6, 0]], #Cavalier
              [[2, 0], [5, 0]], #Fou
              [[3, 0]], #Dame
              [4, 0]] #Roi
#piece_blanc = [[[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]], [[0, 0], [7, 0], [1, 7]], [[1, 0], [6, 0]], [[2, 0], [5, 0]], [[3, 0]], [4, 0]]

piece_noir = [[[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]], #Pion
              [[0, 7], [7, 7]], #Tour
              [[1, 7], [6, 7]], #Cavalier
              [[2, 7], [5, 7]], #Fou
              [[3, 7]], #Dame
              [4, 7]] #Roi
#piece_noir = [[[2, 4], [3, 4], [4, 4], [5, 6], [6, 6], [7, 6]], [[0, 7], [7, 7]], [[6, 7]], [[2, 7], [5, 7]], [[3, 7]], [4, 7]]    
plateau = [[['Tb'], ['Cb'], ['Fb'], ['Db'], ['Rb'], ['Fb'], ['Cb'], ['Tb']], #plateau[0]
           [['Pb'], ['Pb'], ['Pb'], ['Pb'], ['Pb'], ['Pb'], ['Pb'], ['Pb']], #plateau[1]
           [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']], #plateau[2]
           [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']], #plateau[3]
           [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']], #plateau[4]
           [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']], #plateau[5]
           [['Pr'], ['Pr'], ['Pr'], ['Pr'], ['Pr'], ['Pr'], ['Pr'], ['Pr']], #plateau[6]
           [['Tr'], ['Cr'], ['Fr'], ['Dr'], ['Rr'], ['Fr'], ['Cr'], ['Tr']]] #plateau[7]

#plateau = [[['Tb'], ['Cb'], ['Fb'], ['Db'], ['Rb'], ['Fb'], ['Cb'], ['Tb']], [['  '], ['Pb'], ['Pb'], ['Pb'], ['Pb'], ['Pb'], ['Pb'], ['Pb']], [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']], [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']], [['  '], ['  '], ['Pr'], ['Pr'], ['Pr'], ['  '], ['  '], ['  ']], [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']], [['  '], ['  '], ['  '], ['  '], ['  '], ['Pr'], ['Pr'], ['Pr']], [['Tr'], ['Tb'], ['Fr'], ['Dr'], ['Rr'], ['Fr'], ['Cr'], ['Tr']]]