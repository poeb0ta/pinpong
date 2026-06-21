import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode((1000, 800))
screen.fill([9, 7, 133])
pygame.display.flip()
pygame.display.set_caption("Пинг понг!!!")

m = pygame.mixer.music
m.load('music/fon.mp3')
m.set_volume(0.04)
m.play(loops=-1)

no_win = 'GAME OVER'
win = 'YOU ARE WIN'

# Настройка анимации/смены кадров
img = pygame.image.load('images/fon.jpg')

clock = pygame.time.Clock()
FPS = 30

shrift = 50
# Настройка положения и движения
speed1 = 20
speed2 = 10
speed3 = 10
x1 = 400
y1 = 750

x2 = 350
y2 = 400
red2 = 0
green2 = 255

x3 = 400
y3 = 20

x4 = 20

schet = '0'
schet1 = '0'

right = False
left = False
running = True

font = pygame.font.SysFont(None, 70)
txt = font.render(no_win, False, (255, 0, 0))

font1 = pygame.font.SysFont(None, 70)
txt1 = font1.render(win, False, (0, 255, 0))
while running:
    # Обработка событий
    clock.tick(FPS)
    screen.fill([9, 7, 133])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Изменение параметров

        # Отрисовка

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False

    my_font = pygame.font.SysFont(None, shrift)
    text1 = my_font.render(schet1, False, (255, 0, 0))
    my_font1 = pygame.font.SysFont(None, shrift)
    text2 = my_font1.render(schet, False, (0, 255, 0))
    if right == True and x1 < 800:
        x1 = x1 + speed1
    if left == True and x1 > 0:
        x1 = x1 - speed1
    if x2 >= 950:
        speed3 = -speed3
        speed3 -= 1
    if x2 <= 50:
        speed3 = speed3 * -2 + speed3
        speed3 += 1

    if y2 <= 50:
        speed2 = 10
    if y2 >= 705 and x2 + 50 <= x1 + 265.5 and x2 + 50 > x1 - 8:
        green2 = 255
        red2 = 0
        schet = int(schet)
        schet = schet + 1
        speed1 = speed1 + 0.4
        speed2 = -speed2
        speed2 -= 0.5
        schet = str(schet)

    if y2 <= 100 and x2 + 50 <= x3 + 110 and x2 + 50 > x3 - 5:
        red2 = 255
        green2 = 0
        schet1 = int(schet1)
        schet1 = schet1 + 1
        speed2 = speed2 * -2 + speed2
        speed2 += 0.5
        schet1 = str(schet1)
    if x2 != 950:
        x4 = x4
    if x2 >= 950:
        x4 = x4 * -1
    if x2 != 50:
        x4 = x4
    if x2 <= 50:
        x4 = x4 * -1
    x3 = x2 - x4
    print(x2, x3, speed2)
    screen.blit(img, (0, 0))
    pygame.draw.circle(screen, [red2, green2, 13], [x2, y2], 50)
    pygame.draw.rect(screen, [0, 255, 0], [x1, y1, 200, 30])
    pygame.draw.rect(screen, [255, 0, 0], [x3 - 50, y3, 100, 30])
    screen.blit(text1, (30, 370))
    screen.blit(text2, (940, 370))

    if y2 + 50 >= 800:
        m.stop()
        m.load('music/no_win.mp3')
        m.set_volume(0.1)
        m.play(loops=1)
        screen.blit(txt, (350, 400))
        pygame.display.flip()
        time.sleep(2.5)
        pygame.quit()
    if y2 - 50 <= 0:
        m.load('music/win.mp3')
        m.set_volume(0.1)
        m.stop()
        m.play(loops=1)
        screen.blit(txt1, (350, 400))
        pygame.display.flip()
        time.sleep(2.5)
        pygame.quit()

    x2 = x2 + speed3
    y2 = y2 + speed2

    pygame.display.flip()

pygame.quit()