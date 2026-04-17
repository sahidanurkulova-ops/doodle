import pygame
pygame.mixer.init()


class Monster:
    def __init__(self):
        self.x = 10
        self.y = 100
        self.width = 75
        self.height = 44

        self.projectile_x = 10
        self.projectile_y = 110
        self.projectile_width = 45
        self.projectile_height = 34

        self.type_monster = "flying_1"

        self.direction = "right"

        self.shooting = False

        self.assets = pygame.image.load("assets/images/game_tile_doodlejump.png")

        self.projectile = self.assets.subsurface(149, 266, self.projectile_width, self.projectile_height)

        self.flying_monster_1 = self.assets.subsurface(149, 0, self.width, self.height)
        self.flying_monster_2 = self.assets.subsurface(228, 0, self.width, self.height)
        self.flying_monster_3 = self.assets.subsurface(309, 0, self.width, self.height)
        self.flying_monster_4 = self.assets.subsurface(391, 0, self.width, self.height)
        self.flying_monster_5 = self.assets.subsurface(149, 47, self.width, self.height)

        self.costumes = [self.flying_monster_1, self.flying_monster_2, self.flying_monster_3,
                         self.flying_monster_4, self.flying_monster_5]

        self.counter = 0
        self.image = self.costumes[self.counter]

        if self.type_monster == "flying_1":
            self.image = self.flying_monster_2

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.hitbox = self.rect.copy()

        self.projectile_hitbox = pygame.Rect(self.projectile_x, self.projectile_y, self.projectile_width, self.projectile_height)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hitbox = self.rect.copy()
        self.projectile_hitbox = pygame.Rect(self.projectile_x, self.projectile_y, self.projectile_width, self.projectile_height)
        if self.x < 532 - self.width and self.direction == "right":
            self.x += 1
            if self.x > 510 - self.width:
                self.direction = "left"
        if self.x > 10 and self.direction == "left":
            self.x -= 1
            if self.x < 30:
                self.direction = "right"

        self.counter += 0.1
        self.image = self.costumes[int(self.counter) % 5]

        if self.shooting == False:
            self.projectile_x = self.x + 17

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.projectile, (self.projectile_x, self.projectile_y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(screen, (255, 0, 0), self.projectile_hitbox, 2)

    def shoot(self, player):
        if self.projectile_x > player.hitbox.x - 10 and self.projectile_x < player.hitbox.x + 10:
            self.shooting = True
        if self.shooting:
            self.projectile_y += 3
        if self.projectile_y > 850 or self.projectile_y == 850:
            self.shooting = False
            self.projectile_y = self.y + 18