import os
import pygame
import time
pygame.init()
pygame.font.init()

def bouncing_rect():
    global x_speed, y_speed, other_rect_y_speed
    rect.x += x_speed
    rect.y += y_speed
    other_rect.y += y_speed
    pygame.draw.rect(DISPLAY, (255, 255, 255), rect)
    pygame.draw.rect(DISPLAY, (255, 0, 0), other_rect)
    if rect.right >= WIDTH or rect.left <= 0:
        x_speed *= -1
    if rect.bottom >= WIDTH or rect.top <= 0:
        y_speed *= -1
    if other_rect.bottom >= HEIGHT or other_rect.top <= 0:
        other_rect_y_speed *= -1



    if rect.colliderect(other_rect):
        if abs(other_rect.top - rect.bottom) < 10:
            y_speed *= -1
        if abs(other_rect.bottom - rect.top) < 10:
            y_speed *= -1
        if abs(other_rect.right - rect.left) < 10:
            x_speed *= -1
        if abs(other_rect.left - rect.right) < 10:
            x_speed *= -1

clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kondzior idzie po piwo")
KONDZIOR = pygame.image.load(os.path.join("assets", "STEC1.png"))
rect = pygame.Rect(350, 350, 100, 100)
x_speed, y_speed = 5,4
other_rect_y_speed = 4
other_rect = pygame.Rect(300, 600, 200, 100)
def main():
    run = True
    while run is True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        DISPLAY.fill((30, 30, 30))
        bouncing_rect()
        pygame.display.flip()
        clock.tick(60)



main()









