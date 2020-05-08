#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from tkinter import Canvas

#Créé un canvas et le return
def createCanvas(w,h,root):
    cnv=Canvas(root, width=w, height=h, bg="gray")
    cnv.pack()
    return cnv

#Dessine les 7 segments de l'afficheur en fonction de coordonnée (x,y) et dun nombre que l'on veut afficher
def afficheur(x,y,t,nb,cnv):
    if nb == 0 or nb == 2 or nb == 3 or nb == 5 or nb == 7 or nb == 8 or nb == 9:
        cnv.create_polygon((x*t,y*t),((x+5)*t,y*t),((x+4)*t,(y+1)*t),((x+1)*t,(y+1)*t),fill="red",outline='black')
    
    if nb == 0 or nb == 4 or nb == 5 or nb == 6 or nb == 8 or nb == 9:
        cnv.create_polygon((x*t,y*t),(x*t,(y+5)*t),((x+1)*t,(y+4.5)*t),((x+1)*t,(y+1)*t),fill="red",outline='black')
    
    if nb == 0 or nb == 1 or nb == 2 or nb == 3 or nb == 4 or nb == 7 or nb == 8 or nb == 9:
        cnv.create_polygon(((x+5)*t,y*t),((x+5)*t,(y+5)*t),((x+4)*t,(y+4.5)*t),((x+4)*t,(y+1)*t),fill="red",outline='black')
    
    if nb == 2 or nb == 3 or nb == 4 or nb == 5 or nb == 6 or nb == 8 or nb == 9:
        cnv.create_polygon((x*t,(y+5)*t),((x+1)*t,(y+5.5)*t),((x+4)*t,(y+5.5)*t),((x+5)*t,(y+5)*t),((x+4)*t,(y+4.5)*t),((x+1)*t,(y+4.5)*t),fill="red",outline='black')
    
    if nb == 0 or nb == 2 or nb == 6 or nb == 8:
        cnv.create_polygon((x*t,(y+5)*t),(x*t,(y+10)*t),((x+1)*t,(y+9)*t),((x+1)*t,(y+5.5)*t),fill="red",outline='black')
    
    if nb == 0 or nb == 1 or nb == 3 or nb == 4 or nb == 5 or nb == 6 or nb == 7 or nb == 8 or nb == 9:
        cnv.create_polygon(((x+5)*t,(y+5)*t),((x+5)*t,(y+10)*t),((x+4)*t,(y+9)*t),((x+4)*t,(y+5.5)*t),fill="red",outline='black')
    
    if nb == 0 or nb == 2 or nb == 3 or nb == 5 or nb == 6 or nb == 8:
        cnv.create_polygon((x*t,(y+10)*t),((x+5)*t,(y+10)*t),((x+4)*t,(y+9)*t),((x+1)*t,(y+9)*t),fill="red",outline='black')

#Prend un nombre en paramètre et le découpe
#Retourne la liste de chiffres
def splitNumber(nb):
    L = []
    L.append(nb%10)
    nb = nb//10
    L.append(nb%10)
    nb = nb//10
    L.append(nb)
    return L

#Créé une map vide et appelle afficher pour afficher cette map
def grille(n,cnv,img,cellsize):
    cnv.delete("all")
    map = []
    for i in range(n):
        map.append([])
        for j in range(n):
            map[i].append(9)
    draw(map,cnv, "", img,cellsize)

#Affiche une map vide, si perdu : affiche les mines et "PERDU!" ou si gagné : affihce "GAGNE!"
def draw(map, cnv, fin, img, cellsize):
    MAX_X = len(map)*cellsize
    MAX_Y = len(map[0])*cellsize    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]=="X" and fin == "perdu":
                cnv.create_image(cellsize*(j+0.5),cellsize*(i+0.5),image=img[7])
            elif map[i][j] == 9 and fin == "":
                cnv.create_image(cellsize*(j+0.5),cellsize*(i+0.5),image=img[len(img)-1])
    
    if fin == "perdu":
        cnv.create_text(MAX_X/2, MAX_Y/2, text="PERDU!", font=('courier', 80, 'bold'), fill="red")
    elif fin == "gagné":
        cnv.create_text(MAX_X/2, MAX_Y/2, text="GAGNE!", font=('courier', 80, 'bold'), fill="red")
