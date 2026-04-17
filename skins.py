import pygame


class Skins:
    def __init__(self):
        self.width, self.height = 200, 200
        self.width_player, self.height_player = 63, 63
        self.x, self.y = 161, 325
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        self.bunny_idle = pygame.image.load("assets/images/doodle_jump_bunny_idle.png")
        self.bunny_shooting = pygame.image.load("assets/images/doodle_jump_bunny_shooting.png")
        self.bunny_idle = pygame.transform.scale(self.bunny_idle, (self.width, self.height))
        self.bunny_shooting = pygame.transform.scale(self.bunny_shooting, (self.width, self.height))

        self.blue_idle = pygame.image.load("assets/images/doodle_jump_blue_idle.png")
        self.blue_shooting = pygame.image.load("assets/images/doodle_jump_blue_shooting.png")
        self.blue_idle = pygame.transform.scale(self.blue_idle, (self.width, self.height))
        self.blue_shooting = pygame.transform.scale(self.blue_shooting, (self.width, self.height))

        self.fisher_idle = pygame.image.load("assets/images/doodle_jump_fisher_idle.png")
        self.fisher_shooting = pygame.image.load("assets/images/doodle_jump_fisher_shooting.png")
        self.fisher_idle = pygame.transform.scale(self.fisher_idle, (self.width, self.height))
        self.fisher_shooting = pygame.transform.scale(self.fisher_shooting, (self.width, self.height))

        self.doodlestein_idle = pygame.image.load("assets/images/doodle_jump_doodlestein_idle.png")
        self.doodlestein_shooting = pygame.image.load("assets/images/doodle_jump_doodlestein_shooting.png")
        self.doodlestein_idle = pygame.transform.scale(self.doodlestein_idle, (self.width, self.height))
        self.doodlestein_shooting = pygame.transform.scale(self.doodlestein_shooting, (self.width, self.height))

        self.ghost_idle = pygame.image.load("assets/images/doodle_jump_ghost_idle.png")
        self.ghost_shooting = pygame.image.load("assets/images/doodle_jump_ghost_shooting.png")
        self.ghost_idle = pygame.transform.scale(self.ghost_idle, (self.width, self.height))
        self.ghost_shooting = pygame.transform.scale(self.ghost_shooting, (self.width, self.height))

        self.green_idle = pygame.image.load("assets/images/doodle_jump_green_idle.png")
        self.green_shooting = pygame.image.load("assets/images/doodle_jump_green_shooting.png")
        self.green_idle = pygame.transform.scale(self.green_idle, (self.width, self.height))
        self.green_shooting = pygame.transform.scale(self.green_shooting, (self.width, self.height))

        self.ice_idle = pygame.image.load("assets/images/doodle_jump_ice_idle.png")
        self.ice_shooting = pygame.image.load("assets/images/doodle_jump_ice_shooting.png")
        self.ice_idle = pygame.transform.scale(self.ice_idle, (self.width, self.height))
        self.ice_shooting = pygame.transform.scale(self.ice_shooting, (self.width, self.height))

        self.soccer_idle = pygame.image.load("assets/images/doodle_jump_soccer_idle.png")
        self.soccer_shooting = pygame.image.load("assets/images/doodle_jump_soccer_shooting.png")
        self.soccer_idle = pygame.transform.scale(self.soccer_idle, (self.width, self.height))
        self.soccer_shooting = pygame.transform.scale(self.soccer_shooting, (self.width, self.height))

        self.space_idle = pygame.image.load("assets/images/doodle_jump_space_idle.png")
        self.space_shooting = pygame.image.load("assets/images/doodle_jump_space_shooting.png")
        self.space_idle = pygame.transform.scale(self.space_idle, (self.width, self.height))
        self.space_shooting = pygame.transform.scale(self.space_shooting, (self.width, self.height))

        self.underwater_idle = pygame.image.load("assets/images/doodle_jump_underwater_idle.png")
        self.underwater_shooting = pygame.image.load("assets/images/doodle_jump_underwater_shooting.png")
        self.underwater_idle = pygame.transform.scale(self.underwater_idle, (self.width, self.height))
        self.underwater_shooting = pygame.transform.scale(self.underwater_shooting, (self.width, self.height))

        self.skin = self.bunny_idle
        self.counter = 0
        self.skins = {self.bunny_idle: False,
                      self.blue_idle: False,
                      self.fisher_idle: False,
                      self.doodlestein_idle: False,
                      self.ghost_idle: False,
                      self.green_idle: False,
                      self.ice_idle: False,
                      self.soccer_idle: False,
                      self.space_idle: False,
                      self.underwater_idle: False}

        self.last_skin_change = 0
        self.skin_delay = 200

    def switch(self, player):
        keyboard = pygame.key.get_pressed()

        current_time = pygame.time.get_ticks()

        if current_time - self.last_skin_change >= self.skin_delay:
            if keyboard[pygame.K_a]:
                self.counter -= 1
                self.last_skin_change = current_time
                self.get_skin()

            elif keyboard[pygame.K_d]:
                self.counter += 1
                self.last_skin_change = current_time
                self.get_skin()

        self.counter %= 10

        if self.counter == 0:
            self.skins[self.bunny_idle] = True
            player.state = "bunny"
        if self.counter != 0:
            self.skins[self.bunny_idle] = False
        if self.counter == 1:
            self.skins[self.blue_idle] = True
            player.state = "blue"
        if self.counter != 1:
            self.skins[self.blue_idle] = False
        if self.counter == 2:
            self.skins[self.fisher_idle] = True
            player.state = "fisher"
        if self.counter != 2:
            self.skins[self.fisher_idle] = False
        if self.counter == 3:
            self.skins[self.doodlestein_idle] = True
            player.state = "doodlestein"
        if self.counter != 3:
            self.skins[self.doodlestein_idle] = False
        if self.counter == 4:
            self.skins[self.ghost_idle] = True
            player.state = "ghost"
        if self.counter != 4:
            self.skins[self.ghost_idle] = False
        if self.counter == 5:
            self.skins[self.green_idle] = True
            player.state = "green"
        if self.counter != 5:
            self.skins[self.green_idle] = False
        if self.counter == 6:
            self.skins[self.ice_idle] = True
            player.state = "ice"
        if self.counter != 6:
            self.skins[self.ice_idle] = False
        if self.counter == 7:
            self.skins[self.soccer_idle] = True
            player.state = "soccer"
        if self.counter != 7:
            self.skins[self.soccer_idle] = False
        if self.counter == 8:
            self.skins[self.space_idle] = True
            player.state = "space"
        if self.counter != 8:
            self.skins[self.space_idle] = False
        if self.counter == 9:
            self.skins[self.underwater_idle] = True
            player.state = "underwater"
        if self.counter != 9:
            self.skins[self.underwater_idle] = False

    def draw(self, screen):
        for costume, status in self.skins.items():
            if status:
                screen.blit(costume, (self.x, self.y))
                # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def transform_to_playable(self):
        self.skin = pygame.transform.scale(self.skin, (self.width_player, self.height_player))

    def transform_to_carousel(self):
        self.skin = pygame.transform.scale(self.skin, (self.width, self.height))

    def get_skin(self):
        if self.skins[self.bunny_idle]:
            self.skin = self.bunny_idle
        if self.skins[self.blue_idle]:
            self.skin = self.blue_idle
        if self.skins[self.fisher_idle]:
            self.skin = self.fisher_idle
        if self.skins[self.doodlestein_idle]:
            self.skin = self.doodlestein_idle
        if self.skins[self.ghost_idle]:
            self.skin = self.ghost_idle
        if self.skins[self.green_idle]:
            self.skin = self.green_idle
        if self.skins[self.ice_idle]:
            self.skin = self.ice_idle
        if self.skins[self.soccer_idle]:
            self.skin = self.soccer_idle
        if self.skins[self.space_idle]:
            self.skin = self.space_idle
        if self.skins[self.underwater_idle]:
            self.skin = self.underwater_idle





