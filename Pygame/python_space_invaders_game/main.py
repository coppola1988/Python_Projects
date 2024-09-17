import pygame
import random
import math


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width  # breite x achse
        self.height = height  # höhe y achse
        self.screen = pygame.display.set_mode((self.width, self.height))  # auflösung des spiels
        pygame.display.set_caption("SpaceInvaders")  # benennt die Anwendung
        self.clock = pygame.time.Clock()  # Framerate
        self.running = True  # solange true, wird das fenster nicht geschlossen
        self.spaceship = Spaceship(self, 370, 515)  # platzierung des raumschiffs anhand koordinaten
        self.score = 0

        self.enemies = []
        for i in range(12):
            self.enemies.append(Enemy(self, random.randint(0, 736), random.randint(30, 130)))
            # gegner werden zufällig gespawnt
        self.background_img = pygame.image.load("stars.png")  # laden des hintergrund bildes

        while self.running:
            self.clock.tick(60)  # framerate
            self.screen.fill((0, 0, 255))  # farbe des hintergrunds
            self.screen.blit(self.background_img, (0, 0))  # platzierung des Hintergrunds

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # damit das Fenster sich nicht von alleine schließt
                    self.running = False  # wenn man auf das x zum schliessen klickt, wird das Fenster geschloßen

                if event.type == pygame.KEYDOWN:  # prüft, ob eine Taste gedrückt wurde
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-10)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(10)
                    if event.key == pygame.K_SPACE:
                        self.spaceship.fire_bullet()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(10)

                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(-10)

            self.spaceship.update()  # aufruf für das spaceship damit es angezeigt wird

            if len(self.spaceship.bullets) > 0:
                # wenn in der liste bullets mehr als 0 elemente drin sin, wird die Liste durchlaufen
                for bullet in self.spaceship.bullets:
                    if bullet.is_fired:
                        # in jedem durchlauf, wird geprüft ob is fired auf true ist. Wenn ja wird, update ausgeführt
                        bullet.update()
                    else:
                        self.spaceship.bullets.remove(bullet)
                        # hier wird das geschoß wieder aus der Liste entfernt,
                        # wenn das geschoß aus dem Bildschirm heraus fliegt

            for enemy in self.enemies:
                enemy.update()
                enemy.check_collision()
                if enemy.y > 460:
                    for i in self.enemies:
                        i.y = 1000
                    self.print_game_over()
                    break

            self.print_score()
            pygame.display.update()  # damit das display immer aktualisiert wird

    def print_game_over(self):
        go_font = pygame.font.Font("freesansbold.ttf", 64)
        go_text = go_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(go_text, (200, 250))

    def print_score(self):
        score_font = pygame.font.Font("freesansbold.ttf", 24)
        score_text = score_font.render("Punkte: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (8, 8))


class Spaceship:
    def __init__(self, game, x, y):  # hier wurde game geladen, um zugriff auf den screen zu bekommen
        self.x = x  # x koordinate für das spaceship
        self.y = y  # y koordinate für das spaceship
        self.change_x = 0
        self.game = game  # hier wird, game aufgefangen um damit arbeiten zu können und
        # zugriff auf den screen zu bekommen
        self.spaceship_img = pygame.image.load("spaceship.png")  # hier wird das spaceship ins programm geladen
        self.bullets = []  # speichert die geschosse

    def fire_bullet(self):  # methode für die patrone
        self.bullets.append(Bullet(self.game, self.x, self.y))  # bekommt die koordinaten des spaceships
        # und diese werden der liste bullets hinzugefügt
        self.bullets[len(self.bullets) - 1].fire()  # es wird auf die liste referenziert,
        # mit der len funktion können wir uns die anzahl der elemente ausgeben lassen.
        # um das letzte element anzusprechen, nehmen wir -1. von dort aus wird fire() aufgerufen (True)

    def move(self, speed):
        self.change_x += speed

    def update(self):  # neue funktion um das spaceship zu zeichnen
        self.x += self.change_x
        if self.x < 0:  # begrenzung, damit das schiff nicht aus dem Bildschirm fliegen kann
            self.x = 0
        elif self.x > 736:  # 800 - 64, weil das Fenster größer als 800 ist (864)
            self.x = 736

        self.game.screen.blit(self.spaceship_img, (self.x, self.y))  # hier wird das spaceship"gezeichnet"


class Bullet:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.is_fired = False
        self.bullet_speed = 10
        self.bullet_img = pygame.image.load("bullet.png")

    def fire(self):
        self.is_fired = True

    def update(self):
        self.y -= self.bullet_speed  # dadurch bewegt sich das geschoss nach oben
        # weil bullet_speed den wert 10 beinhalten und somit von der y achse immer 10 abgezogen wird

        if self.y <= 0:  # dadurch wird geprüft, ob das geschoss den wert 0 erreicht hat (außerhalb vom Spielfeld)
            self.is_fired = False  # da wir oben bei update immer prüfen ob is fired true ist,
            # können wir durch is_fired = false eine else anweisung setzen und
            # somit das geschoss am Ende einfach löschen
        self.game.screen.blit(self.bullet_img, (self.x, self.y))  # dadurch wird das objekt auf
        # dem spielfeld gezeichnet


class Enemy:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.change_x = 5
        self.change_y = 60
        self.game = game
        self.enemy_img = pygame.image.load("enemy.png")

    def check_collision(self):
        for bullet in self.game.spaceship.bullets:
            distance = math.sqrt(math.pow(self.x - bullet.x, 2) + math.pow(self.y - bullet.y, 2))
            if distance < 35:
                bullet.is_fired = False
                self.game.score += 1
                self.x = random.randint(0, 736)
                self.y = random.randint(50, 150)

    def update(self):
        self.x += self.change_x  # dadurch bewegen sich die gegner

        if self.x >= 736:
            self.y += self.change_y
            self.change_x = -5
        elif self.x <= 0:
            self.y += self.change_y
            self.change_x = 5

        self.game.screen.blit(self.enemy_img, (self.x, self.y))


if __name__ == "__main__":
    game = Game(800, 600)
