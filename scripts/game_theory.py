import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
# %%
# 3 == Y,Y == 3
# 0 == Y,K == 5
# 1 == K,K == 1

class Oyuncu:
    def __init__(self, ad):
        self.ad = ad

class Can(Oyuncu):
    ad = "Can"
    tanım = "çift sayılar Y, tek sayılar K"

    def hamle_yap(arena, hamle_sayısı, oyuncu_no, son_hamle):
        hamleler = []
        for i in range(hamle_sayısı):
            if i % 2 == 0:
                hamleler.append("Y")
            else: 
                hamleler.append("K")
        return(hamleler)

class Cem(Oyuncu):
    ad = "Cem"
    tanım = "hep Y"

    def hamle_yap(arena, hamle_sayısı, oyuncu_no, son_hamle):
        hamleler = []
        for i in range(hamle_sayısı):
            hamleler.append("Y")
        return(hamleler)

class Emre(Oyuncu):
    ad = "Emre"
    tanım = "Y ile başla. Rakibi taklit et"

    def hamle_yap(arena, hamle_sayısı, oyuncu_no, son_hamle):
        hamleler = []
        rakip_no = oyuncu_no # oyuncu_no olarak gönderilen rakip (0,1)
        for i in range(hamle_sayısı):
            if son_hamle == 0:
                hamleler.append("Y")
            else: 
                    hamleler.append(arena[rakip_no][son_hamle-1])


        return(hamleler) # "K" ve "Y"lerden oluşan bir dizi



def oyna(oyuncu_1, oyuncu_2, hamle_sayısı=10, çiz = False):
    sayman = pd.DataFrame({
    "Y":[[3,3], [0,5]],
    "K":[[5,0], [1,1]]
    })
    sayman.index = ["Y", "K"]
    arena = np.empty((2,0), dtype=int)

    M_sayı = 0
    L_sayı = 0
    Toplam_sayı = 0

    # Oynat
    for i in range(hamle_sayısı):
        M_hamle = oyuncu_1.hamle_yap(arena, hamle_sayısı, 1, i)[i]
        L_hamle = oyuncu_2.hamle_yap(arena, hamle_sayısı, 0, i)[i]
        arena = np.hstack((arena, np.array([[M_hamle],[L_hamle]])))

    
    # Hesapla
    for i in range(hamle_sayısı):
        M_hamle = arena[0,i]
        L_hamle = arena[1,i]
        
        M_sayı = M_sayı + sayman[M_hamle][L_hamle][0]
        L_sayı = L_sayı + sayman[M_hamle][L_hamle][1]
        Toplam_sayı = M_sayı + L_sayı

    sonuclar = pd.DataFrame({
        oyuncu_1.ad: M_sayı,
        oyuncu_2.ad: L_sayı,
        "Toplam": Toplam_sayı,
        "Oyun_sayısı": hamle_sayısı  
    }, index= [""])

    if çiz == True:
        string_to_int = {"Y": 0, "K": 1}
        int_arena = np.vectorize(string_to_int.get)(arena)
        cmap = ListedColormap(["Green", "Red"])

        plt.imshow(int_arena, cmap=cmap)
        print(type(int_arena))

    
    df_arena = pd.DataFrame(arena, index=[oyuncu_1.ad, oyuncu_2.ad])
    return(sonuclar, df_arena)



oyna(Can,Emre, 10)[0]



