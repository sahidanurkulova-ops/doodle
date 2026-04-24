import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Volume Slider")


class VolumeControl:
    def __init__(self, x, y, width, level=0.5):
        self.x = x
        self.y = y
        self.width = width
        self.height = 6
        self.radius = 12
        self.level = level
        self.dragging = False

        pygame.mixer.music.set_volume(self.level)

    def set_level(self, level):
        self.level = max(0, min(1, level))
        pygame.mixer.music.set_volume(self.level)

    def get_level(self):
        return self.level

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            handle_x = self.x + self.level * self.width

            if abs(mx - handle_x) <= self.radius and abs(my - self.y) <= self.radius:
                self.dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        if event.type == pygame.MOUSEMOTION and self.dragging:
            mx, my = event.pos
            self.set_level((mx - self.x) / self.width)

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100),
                         (self.x, self.y, self.width, self.height))

        filled = int(self.level * self.width)

        pygame.draw.rect(screen, (0, 200, 100),
                         (self.x, self.y, filled, self.height))

        handle_x = int(self.x + self.level * self.width)

        pygame.draw.circle(screen, (255, 255, 255),
                           (handle_x, self.y + self.height // 2),
                           self.radius)


slider = VolumeControl(100, 150, 300)


running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        slider.handle_event(event)



    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Volume: {int(slider.get_level()*100)}%", True, (255, 255, 255))
    screen.blit(text, (170, 80))

    pygame.display.update()

pygame.quit()