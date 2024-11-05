"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    screen_color = (255, 255, 255)
    screen.fill(screen_color)
    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...

    # les coordonnées de rectangle que l'on dessine
    width = 20 # largeur du rectangle en pixels
    height = 20 # hauteur du rectangle en pixels
    black = (0, 0, 0) # couleur noire
    green = (0, 255, 0) #couleur verte

    for i in range(15):
        for j in range(15):
            x = (2*i+1)*width
            y = 2*j*height

            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, black, rect)

    for i in range(15):
        for j in range(15):
            x = 2*i*width
            y = (2*j+1)*height

            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, black, rect)


    # appel à la méthode draw.rect()
    snake = [
    (10, 15),
    (11, 15),
    (12, 15),]

    for point in snake:
        x, y = width*point[0], height*point[1]
        rect_snake = pg.Rect(x, y, width, height)
        pg.draw.rect(screen, green, rect_snake)

    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()