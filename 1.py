import numpy as np
import cv2


def zmniejszanie(obraz):
    wysokosc, szerokosc,  _ = obraz.shape
    maska = np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]])

    obraz2 = np.zeros(((wysokosc)//3, (szerokosc)//3, 3), dtype=np.uint8)

    for k in range(1, (wysokosc)//3 - 1):
        for l in range(1, (szerokosc)//3 - 1):
            i = 3 * k
            j = 3 * l

            tr = np.sum(maska * obraz[i - 1:i + 2, j - 1:j + 2, 0]) // 16
            tg = np.sum(maska * obraz[i - 1:i + 2, j - 1:j + 2, 1]) // 16
            tb = np.sum(maska * obraz[i - 1:i + 2, j - 1:j + 2, 2]) // 16

            obraz2[k][l][0] = tr
            obraz2[k][l][1] = tg
            obraz2[k][l][2] = tb

    return obraz2

def zmniejszanie_alfa(obraz):
    wysokosc, szerokosc,  _ = obraz.shape
    maska = np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]])

    obraz2 = np.zeros(((wysokosc)//3, (szerokosc)//3, 4), dtype=np.uint8)

    for k in range(1, (wysokosc)//3 - 1):
        for l in range(1, (szerokosc)//3 - 1):
            i = 3 * k
            j = 3 * l

            tr = np.sum(maska * obraz[i - 1:i + 2, j - 1:j + 2, 0]) // 16
            tg = np.sum(maska * obraz[i - 1:i + 2, j - 1:j + 2, 1]) // 16
            tb = np.sum(maska * obraz[i - 1:i + 2, j - 1:j + 2, 2]) // 16

            obraz2[k][l][0] = tr
            obraz2[k][l][1] = tg
            obraz2[k][l][2] = tb
            obraz2[k][l][3] = obraz[i, j, 3] 

    return obraz2

def zwiekszanie(obraz, wysokosc2, szerokosc2):
    wysokosc, szerokosc,  _ = obraz.shape
    maska = np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]])
    obraz2 = np.zeros((wysokosc2, szerokosc2, 3), dtype=np.uint8)
    obraz3 = np.zeros((wysokosc2, szerokosc2, 3), dtype=np.uint8)


    wsp_wys = wysokosc2 / wysokosc
    wsp_szer = szerokosc2 / szerokosc

    for i in range(wysokosc2):
        for j in range(szerokosc2):
            obraz2[i][j] = obraz[int(i/wsp_wys)][int(j/wsp_szer)]

    for i in range(1, wysokosc2 - 1):
        for j in range(1, szerokosc2 - 1):
            tr = np.sum(maska * obraz2[i - 1:i + 2, j - 1:j + 2, 0]) // 16
            tg = np.sum(maska * obraz2[i - 1:i + 2, j - 1:j + 2, 1]) // 16
            tb = np.sum(maska * obraz2[i - 1:i + 2, j - 1:j + 2, 2]) // 16

            obraz3[i][j][0] = tr
            obraz3[i][j][1] = tg
            obraz3[i][j][2] = tb

    return obraz3

def laczenie(obraz, obraz2):
    wysokosc, szerokosc,  _ = obraz.shape
    obraz3 = np.zeros((wysokosc, szerokosc, 3), dtype=np.uint8)


    for i in range(wysokosc):
        for j in range(szerokosc):
            obraz3[i][j][0] = (int(obraz[i][j][0]) + int(obraz2[i][j][0]))//2
            obraz3[i][j][1] = (int(obraz[i][j][1]) + int(obraz2[i][j][1]))//2
            obraz3[i][j][2] = (int(obraz[i][j][2]) + int(obraz2[i][j][2]))//2

    return obraz3


def laczenie_alfa(obraz, obraz2):
    wysokosc, szerokosc,  _ = obraz.shape
    wysokosc2, szerokosc2,  _ = obraz2.shape
    obraz3 = np.zeros((wysokosc, szerokosc, 3), dtype=np.uint8)

    y = (wysokosc - wysokosc2)//2
    x = (szerokosc - szerokosc2)//2
    yk = y + wysokosc2
    xk = x + szerokosc2
    for i in range(wysokosc):
        for j in range(szerokosc):
            if j < x or j > xk-1 or i < y or i > yk-1:
                obraz3[i][j] = obraz[i][j][:]
            else:
                obraz3[i][j][0] = (int(obraz[i][j][0]) + int(obraz[i][j][0]) * int(1-obraz2[i-y][j-x][3]/255) +  int(obraz2[i-y][j-x][0]) * int(obraz2[i-y][j-x][3]/255))//2
                obraz3[i][j][1] = (int(obraz[i][j][1]) + int(obraz[i][j][1]) * int(1-obraz2[i-y][j-x][3]/255) +  int(obraz2[i-y][j-x][1]) * int(obraz2[i-y][j-x][3]/255))//2
                obraz3[i][j][2] = (int(obraz[i][j][2]) + int(obraz[i][j][2]) * int(1-obraz2[i-y][j-x][3]/255) +  int(obraz2[i-y][j-x][2]) * int(obraz2[i-y][j-x][3]/255))//2

    return obraz3



obraz_org = cv2.imread('pg.jpg')
obraz_zmniejszony = zmniejszanie(obraz_org)
obraz_zmniejszony2 = zmniejszanie(obraz_zmniejszony)

pomarancza_org = cv2.imread('Orange.png', cv2.IMREAD_UNCHANGED)
pomarancza_zmniejszona = zmniejszanie_alfa(pomarancza_org)
pomarancza_zmniejszona2 = zmniejszanie_alfa(pomarancza_zmniejszona)

blend = laczenie_alfa(obraz_org, pomarancza_org)
blend_zmniejszony = laczenie_alfa(obraz_zmniejszony, pomarancza_zmniejszona)
blend_zmniejszony2 = laczenie_alfa(obraz_zmniejszony2, pomarancza_zmniejszona2)

powiekszony2_1 = zwiekszanie(blend_zmniejszony2, blend_zmniejszony.shape[0], blend_zmniejszony.shape[1])
powiekszony1_0 = zwiekszanie(blend_zmniejszony, blend.shape[0], blend.shape[1])

wynik1 = laczenie(blend_zmniejszony, powiekszony2_1)
wynik = laczenie(blend, powiekszony1_0)


cv2.imwrite('wynik2.jpg', blend_zmniejszony2)
cv2.imwrite('wynik1.jpg', wynik1)
cv2.imwrite('wynik.jpg', wynik)
