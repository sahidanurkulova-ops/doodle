import pygame
import random
from player import Player
from platform import Platform
from buttons import Buttons
from controller import Controller
from skins import Skins
from monsters import Monster
from slider import VolumeControl


pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(3)

WIDTH, HEIGHT = 532, 850
FPS = 90

logo = pygame.image.load("assets/images/logo.png")
game_background = pygame.image.load("assets/images/background.png")
game_background = pygame.transform.scale(game_background, (WIDTH, HEIGHT))

menu_background = pygame.image.load("assets/images/menu.png")
menu_background = pygame.transform.scale(menu_background, (WIDTH, HEIGHT))

death_sound = pygame.mixer.Sound("assets/sounds/death.mp3")
new_highscore_sound = pygame.mixer.Sound("assets/sounds/win.mp3")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(logo)
pygame.display.set_caption("Doodle Jump")

clock = pygame.time.Clock()

font = pygame.font.Font("assets/fonts/al-seana.ttf", 42)
big_font = pygame.font.Font("assets/fonts/al-seana.ttf", 42)

player = Player()
buttons = Buttons()
controller = Controller()
skins = Skins()
monster = Monster()
slider = VolumeControl(100, 700, 300)


def create_platforms():
    result = [Platform("green", 215, 810)]

    current_y = 720
    for _ in range(8):
        x = random.randint(0, WIDTH - 100)
        result.append(Platform("green", x, current_y))
        current_y -= random.randint(70, 110)

    return result


def get_platform_rect(platform):
    if hasattr(platform, "hitbox"):
        return platform.hitbox
    if hasattr(platform, "rect"):
        return platform.rect
    if hasattr(platform, "x") and hasattr(platform, "y"):
        width = getattr(platform, "width", 100)
        height = getattr(platform, "height", 20)
        return pygame.Rect(platform.x, platform.y, width, height)

    return pygame.Rect(0, 0, 100, 20)


def draw_platforms(platforms):
    for platform in platforms:
        if hasattr(platform, "draw"):
            platform.draw(screen)


def generate_new_platform(platforms):
    highest_y = min(get_platform_rect(p).y for p in platforms)
    x = random.randint(0, WIDTH - 100)
    y = highest_y - random.randint(70, 110)
    platforms.append(Platform("green", x, y))


def reset_game():
    global platforms, score, game_over
    player.reset()
    platforms = create_platforms()
    score = 0
    game_over = False

def save_highscore(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

platforms = create_platforms()
score = 0
game_over = False
running = True
new_highscore = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if controller.gamemode == "game" and game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                new_highscore = True
                reset_game()

    controller.gamemode = buttons.state

    if controller.gamemode == "game":
        background = game_background
        screen.blit(background, (0, 0))

        with open("highscore.txt", "r") as file:
            highscore = int(file.read())

        buttons.draw_menu_button(screen)
        buttons.update(controller.gamemode)
        if score > 0:
            monster.draw(screen)
            monster.shoot(player)
        monster.update()

        keyboard = pygame.key.get_pressed()

        if not game_over:
            player.move(keyboard, WIDTH)
            player.apply_gravity()
            player.set_idle_image_by_state()
            player.switch_to_shooting(keyboard)

            # Столкновение с платформами только при падении вниз
            if player.vel_y > 0:
                for platform in platforms:
                    platform_rect = get_platform_rect(platform)

                    if (
                        player.rect.bottom >= platform_rect.top
                        and player.rect.bottom <= platform_rect.top + 20
                        and player.rect.right > platform_rect.left
                        and player.rect.left < platform_rect.right
                    ):
                        player.rect.bottom = platform_rect.top
                        player.do_jump()
                        break

            # Прокрутка мира вверх
            if player.rect.top < HEIGHT // 2:
                offset = HEIGHT // 2 - player.rect.top
                player.rect.top = HEIGHT // 2

                for platform in platforms:
                    platform_rect = get_platform_rect(platform)

                    if hasattr(platform, "y"):
                        platform.y += offset
                    if hasattr(platform, "rect"):
                        platform.rect.y += offset
                    if hasattr(platform, "hitbox"):
                        platform.hitbox.y += offset

                score += int(offset / 5)

            # Удаляем ушедшие вниз платформы
            new_platforms = []
            for platform in platforms:
                platform_rect = get_platform_rect(platform)
                if platform_rect.top < HEIGHT:
                    new_platforms.append(platform)
            platforms = new_platforms

            while len(platforms) < 9:
                generate_new_platform(platforms)

            # Проигрыш
            if player.rect.top > HEIGHT or player.hitbox.colliderect(monster.projectile_hitbox):
                death_sound.play()
                if score > highscore:
                    save_highscore(score)
                game_over = True

            if score > highscore:
                highscore = score
                if new_highscore:
                    new_highscore_sound.play()
                    new_highscore = False

        draw_platforms(platforms)
        player.draw(screen)

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        highscore_text = font.render(f"Highscore: {highscore}", True, (0, 0, 0))
        screen.blit(score_text, (WIDTH - 170, 15))
        screen.blit(highscore_text, (WIDTH - 220, 70))

        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 140))
            screen.blit(overlay, (0, 0))

            text1 = big_font.render("Game Over", True, (255, 255, 255))
            text2 = font.render(f"Score: {score}", True, (255, 255, 255))
            text3 = font.render("Press R to restart", True, (255, 255, 255))

            screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 - 80))
            screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 - 20))
            screen.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT // 2 + 30))

    elif controller.gamemode == "menu":
        background = menu_background
        screen.blit(background, (0, 0))
        buttons.draw(screen)
        buttons.update(controller.gamemode)

    elif controller.gamemode == "options":
        background = game_background
        screen.blit(background, (0, 0))
        buttons.draw_menu_button(screen)
        buttons.update(controller.gamemode)
        slider.handle_event(event)
        slider.draw(screen, font)

    elif controller.gamemode == "score":
        background = game_background
        screen.blit(background, (0, 0))
        buttons.draw_menu_button(screen)
        buttons.update(controller.gamemode)

    elif controller.gamemode == "store":
        background = game_background
        screen.blit(background, (0, 0))
        buttons.draw_menu_button(screen)
        buttons.update(controller.gamemode)

    elif controller.gamemode == "toys":
        background = game_background
        screen.blit(background, (0, 0))
        buttons.draw_menu_button(screen)
        buttons.draw_rlc_buttons(screen)
        skins.draw(screen)
        skins.switch(player)
        player.set_new_costume(skins)
        buttons.update(controller.gamemode)

    else:
        screen.blit(menu_background, (0, 0))

    pygame.display.flip()

pygame.quit()