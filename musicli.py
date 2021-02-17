import pygame
import random
from pygame import mixer
import sys
import os

global highscore
global gamelife
gamelife = True
global gamer
gamer = False

x = 1000
y = 800

f = open("musicli/highscore.txt", "r")
highscore = int(f.read())
startscore = highscore
f.close()

mixer.init()
mixer.music.load('musicli/love.mp3')
mixer.music.play()


def load_image(name, colorkey=None):
    fullname = os.path.join("musicli/", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

pygame.init()
clock = pygame.time.Clock()

FPS = 50
WIDTH = 750
HEIGHT = 422
screen = pygame.display.set_mode((WIDTH, HEIGHT))

kursorim = load_image("pixelcursor.png").convert()
kursorim = pygame.transform.scale(kursorim, (100, 100))
kursorim.set_colorkey(kursorim.get_at((0, 0)))

kursor_sprites = pygame.sprite.Group()
kursor = pygame.sprite.Sprite()
kursor.image = kursorim
kursor.rect = kursor.image.get_rect()
kursor_sprites.add(kursor)
pygame.mouse.set_visible(False)

global excep
excep = True


def terminate():
    global excep
    excep = False
    pygame.quit()
    exit


def start_screen():
    global excep, gamer
    fon = pygame.transform.scale(load_image('startscreen.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50

    while excep == True:
        screen.fill((0, 0, 0))
        fon = pygame.transform.scale(load_image('startscreen.png'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                excep = False
                gamer = True
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] > 210 and pos[0] < 310 and pos[1] > 170 and pos[1] < 260:
                    return 1
                if pos[0] > 340 and pos[0] < 430 and pos[1] > 170 and pos[1] < 260:
                    return 2
                if pos[0] > 470 and pos[0] < 550 and pos[1] > 170 and pos[1] < 260:
                    return 3
        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            kursor.rect.x = pos[0] - 42
            kursor.rect.y = pos[1] - 40
        try:
            kursor_sprites.draw(screen)
            pygame.display.flip()
        except Exception as e:
            pass
        clock.tick(FPS)

levelnumber = start_screen()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Musicli")

all_sprites = pygame.sprite.Group()

mist = 0
score = 0


def level(number):
    if number == 1:
        create()


def playmusic(lvl):
    msc = 0
    if lvl == 1:
        msc = 1
    return 1


def create():
    bomb = pygame.sprite.Sprite(all_sprites)
    bomb.image = load_image(random.choice(["pinkrect.png", "redrect.png",
                                                  "bluerect.png", "greenrect.png",
                                                  "miraclerect.png", "orangerect.png",
                                                  "purplerect.png"]))
    bomb.rect = bomb.image.get_rect()
    bomb.rect.x = 250 + 65
    bomb.rect.y = 20

    n = random.randrange(1, 4)

    if n == 1:
        bomb.rect.x = 250 + 65
        bomb.rect.y = 20

    if n == 2:
        bomb.rect.x = 250 + 65 + 125
        bomb.rect.y = 20

    if n == 3:
        bomb.rect.x = 250 + 65 + 125 + 125
        bomb.rect.y = 20


def move():
    for enemy in all_sprites:
        enemy.rect.y += 2    

kursorim = load_image("pixelcursor.png").convert()
kursorim = pygame.transform.scale(kursorim, (100, 100))
kursorim.set_colorkey(kursorim.get_at((0, 0)))

kursor_sprites = pygame.sprite.Group()
kursor = pygame.sprite.Sprite()
kursor.image = kursorim
kursor.rect = kursor.image.get_rect()
kursor_sprites.add(kursor)
pygame.mouse.set_visible(False)

star_sprites = pygame.sprite.Group()

GRAVITY = 0.1 

heartim = load_image("heart.png")
heart_sprites = pygame.sprite.Group()
heart = pygame.sprite.Sprite()
heart.image = heartim
heart.rect = heart.image.get_rect()
heart_sprites.add(heart)

for i in heart_sprites:
    a = i
    heart_sprites.add(a)
    a.rect.x = 760
    a.rect.y = 150
class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]

    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(star_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()


        self.velocity = [dx, dy]

        self.rect.x, self.rect.y = pos


        self.gravity = GRAVITY
 
    def update(self):

        self.velocity[1] += self.gravity

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.y > 799:
            self.kill()


def create_particles(position):
    particle_count = 30
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


def play(name):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()

sound1 = pygame.mixer.Sound('musicli/drum1.wav')
sound2 = pygame.mixer.Sound('musicli/drum2.wav')
sound3 = pygame.mixer.Sound('musicli/drum3.wav')


def pole():
    pygame.draw.line(screen, (255, 0, 0), (375, 20), (375, 780), 4)
    pygame.draw.line(screen, (0, 0, 255), (500, 20), (500, 780), 4)
    pygame.draw.line(screen, (255, 0, 255), (625, 20), (625, 780), 4)
    pygame.draw.line(screen, (255, 255, 255), (250, 730), (750, 730), 4)
    pygame.draw.rect(screen, (0, 255, 0), (250, 20, 500, 760), 5)


def mistakes():
    global mist
    mist += 1
    return mist


def wrong():
    for enemy in all_sprites:
        if enemy.rect.y > 780:
            enemy.kill()
            mistakes()

animates_sprites = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(animates_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x + 10, y + 200)
 
    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
 
    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


dragon = AnimatedSprite(load_image("mario5.png"), 12, 8, 0, 0)

glob = 0



def draw():
    f1 = pygame.font.Font(None, 50)
    f2 = pygame.font.Font(None, 40)
    text1 = f1.render('SCORE: {}'.format(score), 1, (0, 255, 0))
    screen.blit(text1, (760, 100))
    text2 = f2.render('HIGHSCORE: {}'.format(highscore), 1, (0, 255, 0))
    screen.blit(text2, (760, 50))    

def playing(high):
    global score
    really = 0
    if high == 1:
        for enemy in all_sprites:
            if enemy.rect.y > 669 and enemy.rect.y < 779 and enemy.rect.x == 250 + 65:        
                really = 1
                enemy.kill()
                score += 1
                create_particles([375, 730])
    if high == 3:
        for enemy in all_sprites:
            if enemy.rect.y > 669 and enemy.rect.y < 779 and enemy.rect.x == 250 + 65 + 125:
                really = 1
                enemy.kill()
                score += 1
                create_particles([500, 730])

    if high == 2:
        for enemy in all_sprites:
            if enemy.rect.y > 669 and enemy.rect.y < 779 and enemy.rect.x > 250 + 65 + 125:
                really = 1
                enemy.kill()
                score += 1
                create_particles([625, 730])

    if really == 0:
        mistakes()


def timertime(time):
    n = 40 - time / 10
    if n >=  10:
        intro_text = ["TIME:",
                      "00:{}".format(int(n))]
    else:
        intro_text = ["TIME:",
                      "00:0{}".format(int(n))]
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('green'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

level(1)
second = 0
startion = 0
hard = playmusic(levelnumber)
milisec = 0
kolvosec = 0

while gamer == False:
    glob += 1
    milisec += 100
    if levelnumber == 1:
        mixer.init()
        mixer.music.load('musicli/mario1.mp3')
        mixer.music.play()
        levelnumber = 100
    if levelnumber == 2:
        mixer.init()
        mixer.music.load('musicli/8bit.mp3')
        mixer.music.play()
        levelnumber = 200
    if levelnumber == 3:
        mixer.init()
        mixer.music.load('musicli/tetris.mp3')
        mixer.music.play()
        levelnumber = 300
    if startion == 0:
        startion = 1
    screen.fill((0, 0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            gamer = True
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                sound1.play()
                playing(1)
            elif i.key == pygame.K_DOWN:
                sound2.play()
                playing(3)
            elif i.key == pygame.K_RIGHT:
                sound3.play()
                playing(2)
    if glob % 10 == 0:
        dragon.update()
    animates_sprites.draw(screen)
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        kursor.rect.x = pos[0] - 42
        kursor.rect.y = pos[1] - 40
    wrong()
    pole()
    if levelnumber == 100:
        second += 30
        if second == 120000:
            mixer.music.pause()
            gamer = True
    if levelnumber == 200:
        second += 20
        if second == 80000:
            mixer.music.pause()
            gamer = True
    if levelnumber == 300:
        second += 25
        if second == 100000:
            mixer.music.pause()
            gamer = True
    if second % 1000 == 0:
        level(1)
    heart_sprites.draw(screen)
    if mist >= 3:
        gamer = True
    if mist >= 1:
        pygame.draw.rect(screen, (0, 0, 0), (760, 450, 180, 150))
    if mist >= 2:
        pygame.draw.rect(screen, (0, 0, 0), (760, 300, 180, 150))
    if milisec % 10000 == 0:
        kolvosec = int(milisec / 1000)
    if highscore < score:
        highscore = score
    star_sprites.update()
    star_sprites.draw(screen)
    timertime(kolvosec)
    move()
    all_sprites.draw(screen)
    kursor_sprites.draw(screen)
    draw()
    pygame.display.flip()
    clock.tick(100)

mixer.music.pause()
FPS = 50
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

mixer.init()
mixer.music.load('musicli/love.mp3')
mixer.music.play()


def terminate():
        global gamelife
        gamelife = False
        pygame.quit()
        exit


def start_screen(score):
    global gamelife
    intro_text = ["SCORE:"]
    intro_text1 = ["HIGHSCORE:"]

    fon = pygame.transform.scale(load_image('coin.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    text_coord = 50
    for line in intro_text:
        line = '{}{} {}'.format(' '*40, line, score)
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    text_coord1 = 100
    for line in intro_text1:
        line = '{}{} {}'.format(' '*35, line, highscore)
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord1 += 10
        intro_rect.top = text_coord1
        intro_rect.x = 10
        text_coord1 += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while gamelife == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        try:
            pygame.display.flip()
        except Exception as e:
            pass
        clock.tick(FPS)

start_screen(score)

pygame.quit()

if startscore < score:
    highscore = score

    f = open("musicli/highscore.txt", "w")
    f.write(str(highscore))
    f.close()
