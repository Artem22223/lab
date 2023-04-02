from pygame import *
from random import randint

FPS = 60

wn_x,wn_y = 570,570
start_x,start_y = 15,120
wn = display.set_mode((wn_x,wn_y))
display.set_caption("Лабиринт")

clock = time.Clock()

class GameSprite(sprite.Sprite):
#конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed,keys,size,colide):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 
        self.keys = keys
        self.colide = colide
        self.move = True

    def show_(self):
        key_pressed = key.get_pressed()

        if key_pressed[self.keys[0]]:
            self.rect.y -= self.speed
        if key_pressed[self.keys[1]]:
            self.rect.y += self.speed
        if key_pressed[self.keys[2]]:
            self.rect.x -= self.speed
        if key_pressed[self.keys[3]]:
            self.rect.x += self.speed
        
        if self.colide:
            if self.rect.y < 15:
                self.rect.y = start_y
                self.rect.x = start_x
            if self.rect.y > 510:
                self.rect.y = start_y
                self.rect.x = start_x
            if self.rect.x < 15:
                self.rect.y = start_y
                self.rect.x = start_x
            if self.rect.x > 510:
                self.rect.y = start_y
                self.rect.x = start_x
        wn.blit(self.image, (self.rect.x, self.rect.y))
    
    def hide(self):
        self.rect.x = 1000
        self.rect.y = 1000

class Wall_(sprite.Sprite):
    def __init__(self, x, y,size,color):
        super().__init__()
        self.image = Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show_(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))

    def hide(self):
        self.rect.x = 800
        self.rect.y = 800

#создание стен 1 уровня
walls = []

walls_cord = [[15,93,(95,15)],[185,93,(15,100)],[15,186,(280,15)],[280,15,(15,95)],[15,278,(360,15)],
[370,90,(15,203)],[463,90,(15,280)],[92,370,(500,15)],[93,462,(200,15)],[278,476,(15,100)],[370,385,(15,95)],
[463,465,(150,15)]
]

for i in range(len(walls_cord)):
    wall1 = Wall_(walls_cord[i][0],walls_cord[i][1],walls_cord[i][2],(40, 40, 40))
    walls.append(wall1)

wall_key_treasure = Wall_(463,90,(94,15),(255,0,0))

wall_key_key = Wall_(385,465,(100,15),(34,177,76))





background = transform.scale(image.load("Labirint.jpg"),(wn_x,wn_y))

cyborg = GameSprite("hero.png",start_x,start_y,5,[K_w,K_s,K_a,K_d],(50,50),True)
cyborg1 = GameSprite("monster_.png",start_x,start_y,5,[K_UP,K_DOWN,K_LEFT,K_RIGHT],(50,50),True)

treasure = GameSprite("treasure.png",490,315,5,[K_3,K_4,K_5,K_6],(50,50),True)

key_treasure = GameSprite("Key_red.png",500,400,5,[K_3,K_4,K_5,K_6],(50,50),False)
key_key = GameSprite("Key_green.png",210,490,5,[K_3,K_4,K_5,K_6],(50,50),False)

monster1 = GameSprite("cyborg.png",25,500,5,[K_3,K_4,K_5,K_6],(50,50),False)
monster2 = GameSprite("cyborg.png",300,30,5,[K_3,K_4,K_5,K_6],(50,50),False)

GAME = True

while GAME:
    wn.blit(background,(0,0))

    cyborg.show_()
    cyborg1.show_()
    treasure.show_()

    wall_key_treasure.show_()
    #wall_key_treasure.hide()
    wall_key_key.show_()

    key_treasure.show_()
    key_key.show_()

    monster1.show_()
    monster2.show_()

    for wall in walls:
        wall.show_()


    #Монстры
    if sprite.collide_rect(cyborg, monster1):
        print("Ещё закрыто")
        cyborg.rect.x = start_x
        cyborg.rect.y = start_y

    if sprite.collide_rect(cyborg, monster2):
        print("Ещё закрыто")
        cyborg.rect.x = start_x
        cyborg.rect.y = start_y

    #Стены, которые меняются
    if sprite.collide_rect(cyborg, wall_key_treasure):
        print("Ещё закрыто")
        cyborg.rect.x = start_x
        cyborg.rect.y = start_y

    if sprite.collide_rect(cyborg, wall_key_key):
        print("Ещё закрыто")
        cyborg.rect.x = start_x
        cyborg.rect.y = start_y

    #Сокровище
    if sprite.collide_rect(cyborg, treasure):
        print("Киборг победил")

    #Ключи
    if sprite.collide_rect(cyborg, key_treasure):
        wall_key_treasure.hide()
        key_treasure.hide()

    if sprite.collide_rect(cyborg, key_key):
        wall_key_key.hide()
        key_key.hide()


    if sprite.spritecollideany(cyborg, walls):
        print("Столкновение со стеной")
        cyborg.rect.x = start_x
        cyborg.rect.y = start_y


    ###
    #Монстры
    if sprite.collide_rect(cyborg1, monster1):
        print("Ещё закрыто")
        cyborg1.rect.x = start_x
        cyborg1.rect.y = start_y

    if sprite.collide_rect(cyborg1, monster2):
        print("Ещё закрыто")
        cyborg1.rect.x = start_x
        cyborg1.rect.y = start_y

    #Стены, которые меняются
    if sprite.collide_rect(cyborg1, wall_key_treasure):
        print("Ещё закрыто")
        cyborg1.rect.x = start_x
        cyborg1.rect.y = start_y

    if sprite.collide_rect(cyborg1, wall_key_key):
        print("Ещё закрыто")
        cyborg1.rect.x = start_x
        cyborg1.rect.y = start_y

    #Сокровище
    if sprite.collide_rect(cyborg1, treasure):
        print("Киборг победил")

    #Ключи
    if sprite.collide_rect(cyborg1, key_treasure):
        wall_key_treasure.hide()
        key_treasure.hide()

    if sprite.collide_rect(cyborg1, key_key):
        wall_key_key.hide()
        key_key.hide()


    if sprite.spritecollideany(cyborg1, walls):
        print("Столкновение со стеной")
        cyborg1.rect.x = start_x
        cyborg1.rect.y = start_y





    #print(cyborg.rect.x,cyborg.rect.y)

    if monster2.rect.x < 295:
        monster2.move = True
    if monster2.rect.x > 500:
        monster2.move = False

    if monster2.move:
        monster2.rect.x += 1
    else:
        monster2.rect.x -= 1 
    
    #
    if monster1.rect.y < 295:
        monster1.move = True
    if monster1.rect.y > 500:
        monster1.move = False

    if monster1.move:
        monster1.rect.y += 1
    else:
        monster1.rect.y -= 1



    for events in event.get():
        if events.type == QUIT:
            GAME = False


    clock.tick(FPS)
    display.update()
