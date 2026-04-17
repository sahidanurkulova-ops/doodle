import pygame


class Buttons:
    def __init__(self):
        self.button_coordinates = {"play_button": {"x": 76, "y": 262},
                                   "toys_button": {"x": 129, "y": 390},
                                   "store_button": {"x": 240, "y": 747},
                                   "options_button": {"x": 428, "y": 750},
                                   "score_button": {"x": 335, "y": 748},
                                   "menu_button": {"x": 20, "y": 5},
                                   "right_button": {"x": 422, "y": 375},
                                   "left_button": {"x": 10, "y": 375},
                                   "choose_button": {"x": 216, "y": 600},
                                   }
        self.main_width, self.main_height = 195, 72
        self.side_width, self.side_height = 90, 104
        self.button_width, self.button_height = 100, 100

        self.play_button_image = pygame.image.load("assets/images/button_play.png")
        self.play_button_image = pygame.transform.scale(self.play_button_image, (self.main_width, self.main_height))
        self.toys_button_image = pygame.image.load("assets/images/button_toys.png")
        self.toys_button_image = pygame.transform.scale(self.toys_button_image, (self.main_width, self.main_height))
        self.menu_button_image = pygame.image.load("assets/images/button_menu.png")
        self.menu_button_image = pygame.transform.scale(self.menu_button_image, (self.main_width, self.main_height))

        self.store_button_image = pygame.image.load("assets/images/button_store.png")
        self.store_button_image = pygame.transform.scale(self.store_button_image, (self.side_width, self.side_height))
        self.options_button_image = pygame.image.load("assets/images/button_options.png")
        self.options_button_image = pygame.transform.scale(self.options_button_image, (self.side_width, self.side_height))
        self.score_button_image = pygame.image.load("assets/images/button_score.png")
        self.score_button_image = pygame.transform.scale(self.score_button_image, (self.side_width, self.side_height))

        self.right_button = pygame.image.load("assets/images/doodle_jump_button.png")
        self.right_button = pygame.transform.scale(self.right_button, (self.button_width, self.button_height))
        self.left_button = pygame.transform.rotate(self.right_button, 180)
        self.choose_button = pygame.image.load("assets/images/doodle_jump_choose.png")
        self.choose_button = pygame.transform.scale(self.choose_button, (self.button_width, self.button_height))
        self.choose_button_hitbox = pygame.Rect(self.button_coordinates["choose_button"]["x"], self.button_coordinates["choose_button"]["y"], self.button_height, self.button_width)

        self.state = "menu"
        self.choose = False

    def draw(self, screen):
        screen.blit(self.play_button_image, (self.button_coordinates["play_button"]["x"], self.button_coordinates["play_button"]["y"]))
        screen.blit(self.toys_button_image, (self.button_coordinates["toys_button"]["x"], self.button_coordinates["toys_button"]["y"]))
        screen.blit(self.store_button_image, (self.button_coordinates["store_button"]["x"], self.button_coordinates["store_button"]["y"]))
        screen.blit(self.options_button_image, (self.button_coordinates["options_button"]["x"], self.button_coordinates["options_button"]["y"]))
        screen.blit(self.score_button_image, (self.button_coordinates["score_button"]["x"], self.button_coordinates["score_button"]["y"]))

        self.play_button_hitbox = pygame.Rect(self.button_coordinates["play_button"]["x"], self.button_coordinates["play_button"]["y"], self.main_width, self.main_height)
        self.toys_button_hitbox = pygame.Rect(self.button_coordinates["toys_button"]["x"], self.button_coordinates["toys_button"]["y"], self.main_width, self.main_height)
        self.menu_button_hitbox = pygame.Rect(self.button_coordinates["menu_button"]["x"], self.button_coordinates["menu_button"]["y"], self.main_width, self.main_height)
        self.store_button_hitbox = pygame.Rect(self.button_coordinates["store_button"]["x"], self.button_coordinates["store_button"]["y"], self.side_width, self.side_height)
        self.options_button_hitbox = pygame.Rect(self.button_coordinates["options_button"]["x"], self.button_coordinates["options_button"]["y"], self.side_width, self.side_height)
        self.score_button_hitbox = pygame.Rect(self.button_coordinates["score_button"]["x"], self.button_coordinates["score_button"]["y"], self.side_width, self.side_height)

        # pygame.draw.rect(screen, (255, 0, 0), self.play_button_hitbox, 2)
        # pygame.draw.rect(screen, (255, 0, 0), self.toys_button_hitbox, 2)
        # pygame.draw.rect(screen, (255, 0, 0), self.menu_button_hitbox, 2)
        # pygame.draw.rect(screen, (255, 0, 0), self.store_button_hitbox, 2)
        # pygame.draw.rect(screen, (255, 0, 0), self.options_button_hitbox, 2)
        # pygame.draw.rect(screen, (255, 0, 0), self.score_button_hitbox, 2)

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.cursor = pygame.Rect(mouse_x, mouse_y, 1, 1)

        if self.cursor.colliderect(self.play_button_hitbox) and self.click[0]:
            self.state = "game"
        elif self.cursor.colliderect(self.toys_button_hitbox) and self.click[0]:
            self.state = "toys"
        elif self.cursor.colliderect(self.store_button_hitbox) and self.click[0]:
            self.state = "store"
        elif self.cursor.colliderect(self.options_button_hitbox) and self.click[0]:
            self.state = "options"
        elif self.cursor.colliderect(self.score_button_hitbox) and self.click[0]:
            self.state = "score"
        elif self.cursor.colliderect(self.menu_button_hitbox) and self.click[0]:
            self.state = "menu"
        elif self.cursor.colliderect(self.choose_button_hitbox) and self.click[0]:
            self.choose = True



    def set_gamemode(self, gamemode):
        self.gamemode = gamemode

    def draw_menu_button(self, screen):
        screen.blit(self.menu_button_image, (self.button_coordinates["menu_button"]["x"], self.button_coordinates["menu_button"]["y"]))

    def draw_rlc_buttons(self, screen):
        screen.blit(self.right_button, (self.button_coordinates["right_button"]["x"], self.button_coordinates["right_button"]["y"]))
        screen.blit(self.left_button, (self.button_coordinates["left_button"]["x"], self.button_coordinates["left_button"]["y"]))
        screen.blit(self.choose_button, (self.button_coordinates["choose_button"]["x"], self.button_coordinates["choose_button"]["y"]))
        self.right_button_hitbox = pygame.Rect(self.button_coordinates["right_button"]["x"], self.button_coordinates["right_button"]["y"], self.button_height, self.button_width)
        self.left_button_hitbox = pygame.Rect(self.button_coordinates["left_button"]["x"], self.button_coordinates["left_button"]["y"], self.button_height, self.button_width)
        self.choose_button_hitbox = pygame.Rect(self.button_coordinates["choose_button"]["x"], self.button_coordinates["choose_button"]["y"], self.button_height, self.button_width)




