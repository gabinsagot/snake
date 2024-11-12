from random import randint
import pygame as pg

WIDTH = 20 # largeur du rectangle en pixels
HEIGHT = 20 # hauteur du rectangle en pixels
BLACK = (0, 0, 0) # couleur noire
GREEN = (0, 255, 0) #couleur verte
RED = (255, 0, 0)
SCREEN_SIZE = (600, 600)

screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()
count = 0


def draw_snake(snake):
    for pos_i, pos_j in snake:
        rect_snake = pg.Rect(WIDTH*pos_i, HEIGHT*pos_j, WIDTH, HEIGHT)
        pg.draw.rect(screen, GREEN, rect_snake)
    
def draw_fruit(fruit):
    xf, yf = WIDTH*fruit[0], HEIGHT*fruit[1]
    rect_fruit = pg.Rect(xf, yf, WIDTH, HEIGHT)
    pg.draw.rect(screen, RED, rect_fruit)

def eat_snake(snake, count, queue):
    count += 1
    snake.insert(0, queue)


if __name__ == "__main__":

    pg.init()

    # on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
    snake = [(10, 15),
            (11, 15),
            (12, 15)]
    direction = (1, 0)
    fruit = (10, 10)
    running = True

    while running:
        
        screen_color = (255, 255, 255)
        screen.fill(screen_color)
        clock.tick(6)

        # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
        # ici donc tous les évènements survenus durant la seconde précédente
        for event in pg.event.get():
            # chaque évênement à un type qui décrit la nature de l'évênement
            # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre


            #handle_events(event, running, direction) en créant une fonction auxiliaire ne fonctionne pas

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

        #Création du damier
        
        for i in range(15):
            for j in range(15):
                x = (2*i+1)*WIDTH
                y = 2*j*HEIGHT

                rect = pg.Rect(x, y, WIDTH, HEIGHT)
                pg.draw.rect(screen, BLACK, rect)

        for i in range(15):
            for j in range(15):
                x = 2*i*WIDTH
                y = (2*j+1)*HEIGHT

                rect = pg.Rect(x, y, WIDTH, HEIGHT)
                pg.draw.rect(screen, BLACK, rect)

        snake.append(tuple(a + b for a,b in zip(snake[-1], direction)))
        queue = snake.pop(0)
            
        draw_fruit(fruit)

        if snake[-1]==fruit:
            eat_snake(snake, count, queue)
            fruit = (randint(0, 29), randint(0, 29))

        if snake[-1] in snake[:-1] or -1 in snake[-1] or 30 in snake[-1]:
            print(count)
            running = False

        draw_snake(snake)

        pg.display.update()


    # Enfin on rajoute un appel à pg.quit()
    # Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
    pg.quit()