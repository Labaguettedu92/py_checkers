from tkinter import *

# -- Evènements --

def showDamier(): #Fonction qui trace un damier
    x = -50
    y = -50
    line = 0
    while line <= 10: #On boucle tant que toutes les lignes n'ont pas été tracées
        y = 0
        if line % 2 == 0: #Si le numéro de ligne est impaire on les places normalement
            while y < 500: #On boucle tant que l'on a pas fait chacune des lignes
                while x < 450: #On boucle tant que l'on a pas fini chaque carré d'une ligne
                    can.create_rectangle(x+50, y, x+100, y + 50, fill='black')
                    x += 100       
                x = -50
                y += 100
        else: #Sinon on les décales
            while y < 500: #On boucle tant que l'on a pas fait chacune des lignes
                while x < 500: #On boucle tant que l'on a pas fini chaque carré d'une ligne
                    can.create_rectangle(x+100, y+50, x+150, y + 100, fill='black')
                    x += 100
                x = -50
                y += 100
        line += 1
    initPion()

def initPion():
    
    #Initialisation des variables
    nombreLignes = 1
    coteActuel = 0
    couleur = "grey"
    
    #Coordonnées de bases
    xB = -25
    yB = -75
    xW = 75
    yW = 75   
        
    while nombreLignes <= 10: #On boucle tant que l'on a pas atteint la fin du damier
        if nombreLignes <= 4 or nombreLignes > 6: #Cela permet d'avoir la coupure de deux lignes au milieu du damier
            if nombreLignes == 7: #Si le nombre de ligne est égal à 7 cela veut dire que l'on a changé de coté
                couleur = "white"
                yB = 225
            if nombreLignes % 2 == 0: #Si le nombre de lignes est impaire
                while xB < 470: #On boucle sur une ligne entière
                    rond(xB + 50, yB + 100, 25, couleur)
                    xB += 100
                xB = -25
                yB += 100
            else: #Sinon on les affiche décalés
                if nombreLignes == 7: #Si le nombre de ligne est égal à 7 on modifie la hauteur
                    yW = 375
                while xW < 480: #Tant que l'on a pas fini une ligne on affiche les pions
                    rond(xW, yW, 25, couleur)
                    xW += 100
                xW = 75
                yW += 100
        nombreLignes += 1 


def rond(x, y, r, coul): #Fonction permettant de tracer un rond plein
    "tracé d ' un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, fill=coul)

# -- Programme Principal --

#Initialisation de la fenêtre et du canvas
fen = Tk()
can = Canvas(fen, width = 500, height = 500, bg = 'ivory' )
can.pack(side =TOP, padx =0, pady =0)

#Initialisation des boutons
bou1 = Button(fen, text='Afficher damier', command = showDamier)
bou1.pack(side = LEFT, padx =3, pady =3)

#Boucle principale
fen.mainloop()
