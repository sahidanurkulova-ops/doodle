import pygame


class Platform:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

        self.width_green = 115
        self.height_green = 30

        self.width_blue = 115
        self.height_blue = 30

        self.width_breaking = 64
        self.height_breaking = 20
        self.double_width_breaking = self.width_breaking * 2

        self.assets = pygame.image.load("assets/images/assets.png").convert_alpha()
        self.assets_2 = pygame.image.load("assets/images/game_tile_doodlejump.png")

        self.platform_green = self.assets.subsurface(6, 405, self.width_green, self.height_green)

        self.platform_blue = self.assets.subsurface(260, 405, self.width_blue, self.height_blue)

        self.platform_breaking_1 = self.assets_2.subsurface(0, 70, self.width_breaking, self.height_breaking)
        self.platform_breaking_1 = pygame.transform.scale(self.platform_breaking_1, (self.width_breaking * 2, self.height_breaking * 2))
        self.platform_breaking_2 = self.assets_2.subsurface(0, 90, self.width_breaking, self.height_breaking)
        self.platform_breaking_2 = pygame.transform.scale(self.platform_breaking_2,
                                                          (self.width_breaking * 2, self.height_breaking * 2))
        self.platform_breaking_3 = self.assets_2.subsurface(0, 120, self.width_breaking, self.height_breaking)
        self.platform_breaking_3 = pygame.transform.scale(self.platform_breaking_3,
                                                          (self.width_breaking * 2, self.height_breaking * 2))
        self.platform_breaking_4 = self.assets_2.subsurface(0, 150, self.width_breaking, self.height_breaking)
        self.platform_breaking_4 = pygame.transform.scale(self.platform_breaking_4,
                                                          (self.width_breaking * 2, self.height_breaking * 2))

        self.platform_breaking_costumes = [self.platform_breaking_1, self.platform_breaking_2, self.platform_breaking_3,
                                           self.platform_breaking_4]

        self.counter = 0
        self.image = self.platform_breaking_costumes[self.counter]

        self.broken = False

        if self.color == "green":
            self.image = self.platform_green
            self.width = self.width_green
            self.height = self.height_green
        if self.color == "breaking":
            self.image = self.image
        else:
            self.image = self.platform_blue
            self.width = self.width_blue
            self.height = self.height_blue

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hitbox = self.rect.copy()

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.hitbox.x = self.x
        self.hitbox.y = self.y

        if self.broken:
            self.counter += 0.1
        self.image = self.platform_breaking_costumes[int(self.counter) % 4]

    def draw(self, screen):
        self.update()
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)