import pygame
pygame.mixer.init()


class Player:
    def __init__(self):
        self.start_x = 235
        self.start_y = 607

        self.width_idle = 63
        self.width_shooting = 63
        self.width = self.width_idle
        self.height = 63

        self.assets = pygame.image.load("assets/images/assets.png")
        self.image_idle = self.assets.subsurface(323, 10, 127, 127)
        self.image_idle = pygame.transform.scale(self.image_idle, (self.width_idle, self.height))

        self.bunny_idle = pygame.image.load("assets/images/doodle_jump_bunny_idle.png")
        self.bunny_shooting = pygame.image.load("assets/images/doodle_jump_bunny_shooting.png")
        self.bunny_idle = pygame.transform.scale(self.bunny_idle, (self.width_idle, self.height))
        self.bunny_shooting = pygame.transform.scale(self.bunny_shooting, (self.width_shooting, self.height))

        self.blue_idle = pygame.image.load("assets/images/doodle_jump_blue_idle.png")
        self.blue_shooting = pygame.image.load("assets/images/doodle_jump_blue_shooting.png")
        self.blue_idle = pygame.transform.scale(self.blue_idle, (self.width_idle, self.height))
        self.blue_shooting = pygame.transform.scale(self.blue_shooting, (self.width_shooting, self.height))

        self.fisher_idle = pygame.image.load("assets/images/doodle_jump_fisher_idle.png")
        self.fisher_shooting = pygame.image.load("assets/images/doodle_jump_fisher_shooting.png")
        self.fisher_idle = pygame.transform.scale(self.fisher_idle, (self.width_idle, self.height))
        self.fisher_shooting = pygame.transform.scale(self.fisher_shooting, (self.width_shooting, self.height))

        self.doodlestein_idle = pygame.image.load("assets/images/doodle_jump_doodlestein_idle.png")
        self.doodlestein_shooting = pygame.image.load("assets/images/doodle_jump_doodlestein_shooting.png")
        self.doodlestein_idle = pygame.transform.scale(self.doodlestein_idle, (self.width_idle, self.height))
        self.doodlestein_shooting = pygame.transform.scale(self.doodlestein_shooting, (self.width_shooting, self.height))

        self.ghost_idle = pygame.image.load("assets/images/doodle_jump_ghost_idle.png")
        self.ghost_shooting = pygame.image.load("assets/images/doodle_jump_ghost_shooting.png")
        self.ghost_idle = pygame.transform.scale(self.ghost_idle, (self.width_idle, self.height))
        self.ghost_shooting = pygame.transform.scale(self.ghost_shooting, (self.width_shooting, self.height))

        self.green_idle = pygame.image.load("assets/images/doodle_jump_green_idle.png")
        self.green_shooting = pygame.image.load("assets/images/doodle_jump_green_shooting.png")
        self.green_idle = pygame.transform.scale(self.green_idle, (self.width_idle, self.height))
        self.green_shooting = pygame.transform.scale(self.green_shooting, (self.width_shooting, self.height))

        self.ice_idle = pygame.image.load("assets/images/doodle_jump_ice_idle.png")
        self.ice_shooting = pygame.image.load("assets/images/doodle_jump_ice_shooting.png")
        self.ice_idle = pygame.transform.scale(self.ice_idle, (self.width_idle, self.height))
        self.ice_shooting = pygame.transform.scale(self.ice_shooting, (self.width_shooting, self.height))

        self.soccer_idle = pygame.image.load("assets/images/doodle_jump_soccer_idle.png")
        self.soccer_shooting = pygame.image.load("assets/images/doodle_jump_soccer_shooting.png")
        self.soccer_idle = pygame.transform.scale(self.soccer_idle, (self.width_idle, self.height))
        self.soccer_shooting = pygame.transform.scale(self.soccer_shooting, (self.width_shooting, self.height))

        self.space_idle = pygame.image.load("assets/images/doodle_jump_space_idle.png")
        self.space_shooting = pygame.image.load("assets/images/doodle_jump_space_shooting.png")
        self.space_idle = pygame.transform.scale(self.space_idle, (self.width_idle, self.height))
        self.space_shooting = pygame.transform.scale(self.space_shooting, (self.width_shooting, self.height))

        self.underwater_idle = pygame.image.load("assets/images/doodle_jump_underwater_idle.png")
        self.underwater_shooting = pygame.image.load("assets/images/doodle_jump_underwater_shooting.png")
        self.underwater_idle = pygame.transform.scale(self.underwater_idle, (self.width_idle, self.height))
        self.underwater_shooting = pygame.transform.scale(self.underwater_shooting, (self.width_shooting, self.height))

        self.image_shooting = pygame.image.load("assets/images/doodle_jump_green_shooting.png")
        self.image_shooting = pygame.transform.scale(self.image_shooting, (self.width_shooting, self.height))

        self.nose_width = 14
        self.nose_height = 60
        self.nose = pygame.image.load("assets/images/doodle_jump_nose_yellow.png")
        self.ghost_nose = pygame.image.load("assets/images/doodle_jump_nose_ghost.png")
        self.doodlestein_nose = pygame.image.load("assets/images/doodle_jump_nose_doodlestein.png")
        self.nose = pygame.transform.scale(self.nose, (self.nose_width, self.nose_height))
        self.ghost_nose = pygame.transform.scale(self.ghost_nose, (self.nose_width, self.nose_height))
        self.doodlestein_nose = pygame.transform.scale(self.doodlestein_nose, (self.nose_width, self.nose_height))

        self.bullet_x = 0
        self.bullet_y = 0
        self.bullet_width = 15
        self.bullet_height = 12
        self.bullet = pygame.image.load("assets/images/doodle_jump_bullet.png")
        self.bullet_hitbox = pygame.Rect(self.bullet_x, self.bullet_y, self.bullet_width, self.bullet_height)

        self.jump_sound = pygame.mixer.Sound("assets/sounds/jump.wav")
        self.jetpack_sound = pygame.mixer.Sound("assets/sounds/jetpack3.mp3")
        self.shoot_sound = pygame.mixer.Sound("assets/sounds/pistol_shoot.mp3")

        self.state = "default"
        self.shoot = False

        self.image_player = self.image_idle

        self.rect = pygame.Rect(self.start_x, self.start_y, self.width_idle - 20, self.height)
        self.hitbox = self.rect.copy()

        self.vel_y = 0
        self.gravity = 0.35
        self.jump_strength = -12
        self.player_speed = 5

    def update_hitbox(self):
        if not self.shoot:
            self.hitbox.x = self.rect.x + 20
            self.hitbox.y = self.rect.y
            self.hitbox.width = self.rect.width
            self.hitbox.height = self.rect.height
            self.bullet_x = self.rect.x
            self.bullet_y = self.rect.y
        if self.shoot:
            self.hitbox.x = self.rect.x + 15
            self.hitbox.y = self.rect.y
            self.hitbox.width = self.width_shooting - 30
            self.hitbox.height = self.rect.height
            self.bullet_y += 1

    def draw(self, screen):
        screen.blit(self.image_player, (self.rect.x, self.rect.y))
        screen.blit(self.bullet, (self.bullet_x, self.bullet_y))

        if self.shoot:
            if self.state != "ghost" or self.state != "doodlestein":
                screen.blit(self.nose, (self.rect.x + 25, self.rect.y + 5))
            if self.state == "ghost":
                screen.blit(self.ghost_nose, (self.rect.x + 25, self.rect.y + 5))
            if self.state == "doodlestein":
                screen.blit(self.doodlestein_nose, (self.rect.x + 25, self.rect.y + 5))

        self.update_hitbox()
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.player_speed

        if self.rect.right < 0:
            self.rect.left = screen_width
        elif self.rect.left > screen_width:
            self.rect.right = 0

    def apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

    def do_jump(self):
        self.vel_y = self.jump_strength
        try:
            self.jump_sound.play()
        except:
            pass

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.vel_y = 0
        self.shoot = False
        self.image_player = self.image_idle
        self.update_hitbox()

    def switch_to_shooting(self, keys):
        if keys[pygame.K_SPACE]:
            self.shoot = True
            self.shooting()
            self.shoot_sound.play()
            self.hitbox = pygame.Rect(self.start_x + 50, self.start_y, self.width_shooting, self.height)
        else:
            self.image_player = self.image_idle
            self.shoot = False
            self.hitbox = pygame.Rect(self.start_x, self.start_y, self.width_idle, self.height)

    def set_new_costume(self, skins):
        skins.transform_to_playable()
        self.image_idle = skins.skin
        self.image_player = self.image_idle

    def set_idle_image_by_state(self):
        if self.state == "bunny":
            self.image_player = self.bunny_idle
        elif self.state == "blue":
            self.image_player = self.blue_idle
        elif self.state == "fisher":
            self.image_player = self.fisher_idle
        elif self.state == "doodlestein":
            self.image_player = self.doodlestein_idle
        elif self.state == "ghost":
            self.image_player = self.ghost_idle
        elif self.state == "green":
            self.image_player = self.green_idle
        elif self.state == "ice":
            self.image_player = self.ice_idle
        elif self.state == "soccer":
            self.image_player = self.soccer_idle
        elif self.state == "space":
            self.image_player = self.space_idle
        elif self.state == "underwater":
            self.image_player = self.underwater_idle
        else:
            self.image_player = self.image_idle

    def shooting(self):
        if self.state == "bunny":
            self.image_player = self.bunny_shooting
        elif self.state == "blue":
            self.image_player = self.blue_shooting
        elif self.state == "fisher":
            self.image_player = self.fisher_shooting
        elif self.state == "doodlestein":
            self.image_player = self.doodlestein_shooting
        elif self.state == "ghost":
            self.image_player = self.ghost_shooting
        elif self.state == "green":
            self.image_player = self.green_shooting
        elif self.state == "ice":
            self.image_player = self.ice_shooting
        elif self.state == "soccer":
            self.image_player = self.soccer_shooting
        elif self.state == "space":
            self.image_player = self.space_shooting
        elif self.state == "underwater":
            self.image_player = self.underwater_shooting
        else:
            self.image_player = self.image_shooting