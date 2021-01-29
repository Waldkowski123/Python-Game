import pygame
import os
import random

pygame.init()
pygame.font.init()
mainclock = pygame.time.Clock()
import time
WIDTH, HEIGHT = 900, 900
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stec skacze w windzie")
STEC = pygame.image.load(os.path.join("assets", "STEC1.png"))
MEGASTEC = pygame.image.load(os.path.join("assets", "MEGASTEC.png"))
STECSLEEP = [pygame.image.load(os.path.join("assets", "STEC1.png")), pygame.image.load(os.path.join("assets", "STEC2.png")), pygame.image.load(os.path.join("assets", "STEC3.png")), pygame.image.load(os.path.join("assets", "STEC2.png")), pygame.image.load(os.path.join("assets", "STEC1.png"))]
ULEPSZONAWINDA = pygame.image.load(os.path.join("assets", "Ulepszona winda.png"))
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "main_menu_bg 2.png")), (WIDTH, HEIGHT))
options_bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "controls.png")), (WIDTH, HEIGHT))
richstec = pygame.image.load(os.path.join("assets", "richstec.png"))

hop = pygame.mixer.Sound(os.path.join("assets", "hop.wav"))
hajsiezdadza = pygame.mixer.Sound(os.path.join("assets", "hajs sie zgadza.wav"))
atencjo = pygame.mixer.Sound(os.path.join("assets", "atencja.wav"))
upgrade = pygame.mixer.Sound(os.path.join("assets", "Upgrade.wav"))
buty = pygame.mixer.Sound(os.path.join("assets", "buty.wav"))
stecthegame = pygame.mixer.Sound(os.path.join("assets", "game.wav"))
stecthegame.play()
BG = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "smallwinda.png")), (WIDTH, HEIGHT)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "Ulepszona winda 2.png")), (WIDTH, HEIGHT)),
      pygame.transform.scale(pygame.image.load(os.path.join("assets", "Ulepszona winda 3.png")), (WIDTH, HEIGHT)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "Ulepszona winda 4.png")), (WIDTH, HEIGHT)),
      pygame.transform.scale(pygame.image.load(os.path.join("assets", "Ulepszona winda 5.png")), (WIDTH, HEIGHT)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "Ulepszona winda 6.png")), (WIDTH, HEIGHT))]

class Button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    def draw(self, DISPLAY, outline=None):
        if outline:
            pygame.draw.rect(DISPLAY, outline, (self.x-2, self.y-2, self.width+4, self.height + 4), 0)
        pygame.draw.rect(DISPLAY, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != "":
            font = pygame.font.SysFont("comicsans", 25)
            text = font.render(self.text, True, (0, 0, 0))
            DISPLAY.blit(text, (self.x + (self.width/2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
class Player():

    def __init__(self, x, y):
        self.Player_img = STEC
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.Player_img)


    def draw(self, window):
        window.blit(self.Player_img, (self.x, self.y))

    def get_width(self):
        return self.Player_img.get_width()

    def get_height(self):
        return self.Player_img.get_height()

def main_menu():
    while True:

        DISPLAY.blit(menu_bg, (0, 0))
        pos = pygame.mouse.get_pos()
        button_1 = Button((0, 0, 255), 270, 287, 335, 47, "PLAY")
        button_2 = Button((0, 0, 255), 270, 410, 335, 47, "MORE INFO")
        button_1.draw(DISPLAY, (0, 0, 0))
        button_2.draw(DISPLAY, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if button_1.isOver(pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        atencjo.play()
                        time.sleep(2)
                        main()
            if button_2.isOver(pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        options()
        pygame.display.update()

def options():
    while True:
        DISPLAY.blit(options_bg, (0, 0))
        pos = pygame.mouse.get_pos()
        info_button1 = Button((0, 0, 255), 280, 612, 305, 63, "BACK")
        info_button1.draw(DISPLAY, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if info_button1.isOver(pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main_menu()
        pygame.display.update()

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    player = Player(100, 355)
    player_vel = 5
    jump = False
    player_vel_y = 10
    main_font = pygame.font.SysFont(" 8-Bit-Madness", 30)
    number_of_points = 0
    shop1price = 10
    shop2price = 10
    shop3price = 10
    pointsdouble = 2

    normalSkok = 4
    shop1 = Button((0, 255, 0), 0, 0, 220, 50, f"Ulepsz skok: {shop1price}")
    shop2 = Button((0, 255, 0), 230, 0, 220, 50, f"Ulepsz punkty: {shop2price}")
    shop3 = Button((0, 255, 0), 460, 0, 220, 50, (f"Ulepsz winde:{shop3price}"))
    win = Button((0, 255, 0), 0, 100, 200, 50, "Win: 10000 + AllMaxed")
    levelshop1 = 0
    levelshop2 = 0
    levelshop3 = 0
    background_image = 0

    def redraw_window():
        DISPLAY.blit(BG[background_image], (0, 0))
        player.draw(DISPLAY)
        points = main_font.render(f"Punkty: {round(number_of_points)}", True, (255, 255, 255))
        DISPLAY.blit(points, (WIDTH - points.get_width() - 50, 10))
        shop1.draw(DISPLAY, (0, 0, 0))
        shop2.draw(DISPLAY, (0, 0, 0))
        shop3.draw(DISPLAY, (0, 0, 0))
        win.draw(DISPLAY, (0, 0, 0))
        pygame.display.update()


    while run:
        redraw_window()
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if shop1.isOver(pos):
                        if number_of_points >= shop1price:
                            if levelshop1 + 1 <= 5:
                                if player.y == 355:
                                   number_of_points -= shop1price
                                   shop1price *= 4
                                   buty.play()
                                   levelshop1 += 1
                                   normalSkok += 2
                                   shop1.text = f"Ulepsz skok  lvl {levelshop1 + 1}: {shop1price} p "
                            if levelshop1 == 5:
                                player.Player_img = MEGASTEC
                                shop1.text = "Skok wymaxowany"
                                shop1.color = (255, 0 ,0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shop2.isOver(pos):
                    if levelshop2 + 1 <= 5:
                        if number_of_points >= shop2price:
                            number_of_points -= shop2price
                            pointsdouble *= 2
                            shop2price *= 4
                            hajsiezdadza.play()
                            levelshop2 += 1
                            shop2.text = f"Punkty x2 lvl {levelshop2 + 1}: {shop2price}"
                    if levelshop2 == 5:
                        shop2.text = "Punkty wymaxowane"
                        shop2.color = (255, 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shop3.isOver(pos):
                    if background_image + 1 <= 5:
                        if number_of_points >= shop3price:
                            number_of_points -= shop3price
                            shop3price *= 4
                            levelshop3 += 1
                            upgrade.play()
                            background_image += 1
                            shop3.text = f"Ulepsz windę na  lvl {levelshop3 + 1}: {shop3price} p "

                    if background_image == 5:
                        shop3.text = "Winda wymaxowana"
                        shop3.color = (255, 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if win.isOver(pos):
                    if number_of_points >= 10000:
                        if levelshop2 == 5 and levelshop1 == 5 and levelshop3 == 5:
                            player.Player_img = richstec
                            hajsiezdadza.play()
                            win.color = (255, 0, 0)
                            win.text = "Wygrałeś!"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
        if keys[pygame.K_d] and player.x + player_vel + 440 < WIDTH:  # Right
            player.x += player_vel

        if keys[pygame.K_a] and player.x - player_vel > - 120:  # Left
            player.x -= player_vel
        if  jump is False and keys[pygame.K_SPACE] and player.y == 355:
            jump = True
            hop.play()

        if jump is True:
            player.y -= player_vel_y*normalSkok
            player_vel_y -= 1
            number_of_points += pointsdouble
            if player_vel_y < -10:
                jump = False
                player_vel_y = 10

main_menu()