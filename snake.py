"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
count = 0


# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
snake = [
        (10, 15),
        (11, 15),
        (12, 15),]
direction = (1, 0)
fruit = (10, 10)
running = True

while running:
    #Création du serpent


    screen_color = (255, 255, 255)
    screen.fill(screen_color)
    clock.tick(6)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        """

        """
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_UP:
                direction = (0, -1)
            if event.key == pg.K_DOWN:
                direction = (0, 1)
            if event.key == pg.K_LEFT:
                direction = (-1, 0)
            if event.key == pg.K_RIGHT:
                direction = (1, 0)
            if event.key == pg.K_q:
                running = False

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...

    width = 20 # largeur du rectangle en pixels
    height = 20 # hauteur du rectangle en pixels
    black = (0, 0, 0) # couleur noire
    green = (0, 255, 0) #couleur verte
    red = (255, 0, 0)

    #Création du damier
    
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
    """   
    for event in pg.event.get():
        if event.key == pg.K_w:
            direction = (0, 1)
        if event.key == pg.K_s:
            direction = (0, -1)
        if event.key == pg.K_a:
            direction = (-1, 0)
        if event.key == pg.K_d:
            direction = (1, 0)
"""
    snake.append(tuple(a + b for a,b in zip(snake[-1], direction)))
    queue = snake.pop(0)
        

    xf, yf = width*fruit[0], height*fruit[1]
    rect_fruit = pg.Rect(xf, yf, width, height)
    pg.draw.rect(screen, red, rect_fruit)

    if snake[-1]==fruit:
        count += 1
        snake.insert(0, queue)
        fruit = randint(0, 29), randint(0, 29)

    if snake[-1] in snake[:-1]:
        print(count)
        running = False

    for point in snake:
        x, y = width*point[0], height*point[1]
        rect_snake = pg.Rect(x, y, width, height)
        pg.draw.rect(screen, green, rect_snake)


    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()