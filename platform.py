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

        self.assets = pygame.image.load("assets/images/assets.png").convert_alpha()

        self.platform_green = self.assets.subsurface(6, 405, self.width_green, self.height_green)
        self.platform_blue = self.assets.subsurface(260, 405, self.width_blue, self.height_blue)

        if self.color == "green":
            self.image = self.platform_green
            self.width = self.width_green
            self.height = self.height_green
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

    def draw(self, screen):
        self.update()
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)