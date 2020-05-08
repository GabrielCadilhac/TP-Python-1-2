#!/usr/bin/env python
# coding: utf-8

# In[1]:
from random import sample
#Renvoie une liste qui contient toutes les coordonnées des mines
#En fonction d'une probabilité et d'une taille
def random_mines(p,g):
    size = len(g)
    nmines = int(size*p)
    mines = sample(g, nmines)
    return mines

#Renvoie une liste contenant les coordonnées des 8 cases atour de la case (i,j) et de taille n
def voisins(n, i, j):
    "Dans une grille n x n, indices (ligne, colonne) des voisins dans la grille d'un sommet (i,j) de la grille"
    return [(a,b) for (a, b) in [(i, j+1),(i, j-1), (i-1, j), (i+1,j), (i+1,j-1),(i+1,j+1),(i-1,j+1),(i-1,j-1)] if a in range(n) and b in range(n)]

#Renvoie une liste avec les coordonnées d'un "anneau" de taille n
#genere calcule les coordonnées qui sont tout autour d'une case de distance n
def genere(n,cx,cy,i):
    L = []
    for x in range(0,2*i+1):
        for y in range(0,2*i+1):
            if x==0 or x==2*i or y==0 or y==2*i:
                L.append((x+cx-i,y+cy-i))
    return L

#Retourne une liste qui est la matrice du plateau avec toutes les cases nombres et mines
#Elle prend en paramètre la liste de coordonnées des mines, la parcours et ajoute +1 tout autour de la case mine
def nombre(mines,n,click):
    compteurMines = 0
    grid = [[0]*n for _ in range(n)]
    for (i,j) in mines:
        v = voisins(n,i,j)
        for (a,b) in v:
            if not((a,b) in mines):
                grid[a][b] += 1
                
    for (x,y) in mines:
        grid[x][y] = "X"
        compteurMines += 1
    
    return grid,compteurMines

#Regroupe deux cartes pour en faire une seule
def createMap(n,click,p,lst_mines):
    #Générer la première carte en fonction du clic
    grid1,p,lst_mines = update(n,p,click,lst_mines)

    #On génère une grille normalement avec toutes les mines de taille n
    grid = [(line,col) for col in range(0,n) for line in range(0,n)]
    mines = random_mines(p,grid)
    grid2 =[[0]*n for _ in range(n)]
    for (a,b) in mines:
        grid2[a][b] = "X"
        
    #On supperpose les deux grilles states, en faisant attention que grid1 soit prioritaire sur grid2
    map=[]
    for x in range(n):
        map.append([])
        for y in range(n):
            if (x>=click[0]-4 and x<=click[0]+4) and (y>=click[1]-4 and y<=click[1]+4):
                map[x].append(grid1[x][y])
            else:
                map[x].append(grid2[x][y])
                if grid2[x][y]=="X":
                    lst_mines.append((x,y))
    N, compteurMines = nombre(lst_mines,n,click)
    afficher(N)
    return N, compteurMines, lst_mines

#update permet de créer un grille de 4x4 au début pour créer une zones avec peu de mines en fonction du click du joueur
def update(n,p,click,lst_mines):
    for i in range(1,4):
        if click[0]+i or click[0]-i or click[1]+i or click[1]-i:
            #genere permet de créer une liste qui contient 
            #les coordonnées des cases autour du click en fonction de i
            g = genere(n, click[0], click[1],i)
            mines = random_mines(p, g)
            p += 0.05
            for (a,b) in mines:
                lst_mines.append((a,b))
    
    grid=[[0]*n for _ in range(n)]
    for (a,b) in lst_mines:
        grid[a][b] = "X"
    return grid,p,lst_mines

#Prend une liste en paramère et l'affiche dans la console
def afficher(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = " ")
        print()
# In[ ]:




