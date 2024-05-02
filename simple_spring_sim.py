import math
import pygame

pygame.init()
pygame.display.set_caption("spring simulation")


extension = 20
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
fps = 144
running = True
velocity = pygame.Vector2(0, 0)
acceleration = pygame.Vector2(0, 0)
mass = 50
mass_pos = pygame.Vector2(640, 360 + extension)
k = 10
play = False
friction = True
font = pygame.font.Font(None, 32)
playing_surface = font.render(
    "Playing                    (space)", True, "black")
paused_surface = font.render(
    "Paused                    (space)", True, "black")
friction_on_surface = font.render(
    "Friction = ON         (backspace)", True, "black")
friction_off_surface = font.render(
    "Friction = OFF        (backspace)", True, "black")


# functions
def calcForce(springConst, extension):
    return ((-1)*springConst) * extension


def calcAcc(force, mass):
    return force/mass


def drawMass(massValue):
    pygame.draw.rect(screen, "dark blue", (640-(massValue/2),
                     mass_pos.y-(massValue/2), massValue, massValue))


def drawSpring():
    pygame.draw.rect(screen, ("dark grey"), (640-(k/4), 0, k/2, mass_pos.y))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = not play
            if event.key == pygame.K_BACKSPACE:
                friction = not friction

    mass_surface = font.render(f"Mass:               {
                               str(mass)}    (w,s)", True, "black")
    extension_surface = font.render(
        f"Extension:       {str(extension)}  (up,down)", True, "black")
    SpringConst_surface = font.render(
        f"Spring Const: {str(k)}    (x,z)", True, "black")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    if keys[pygame.K_UP]:
        if extension < 400:
            extension += 1
    if keys[pygame.K_DOWN]:
        if extension > -400:
            extension -= 1

    if keys[pygame.K_w]:
        if mass < 350:
            mass += 1
    if keys[pygame.K_s]:
        if mass > 10:
            mass -= 1

    if keys[pygame.K_x]:
        if k < 70:
            k += 0.5
    if keys[pygame.K_z]:
        if k > 4:
            k -= 0.5

    if play:
        mass_pos.y += velocity.y * dt
        velocity.y += calcAcc(calcForce(k, mass_pos.y-360), mass) * dt
        if friction:
            velocity.y *= 0.985
    else:
        mass_pos.y = 360 + extension
        velocity.y = 0

    screen.fill("light blue")
    drawSpring()
    drawMass(mass)
    screen.blit(mass_surface, (0, 0))
    screen.blit(extension_surface, (0, 20))
    screen.blit(SpringConst_surface, (0, 40))
    if play:
        screen.blit(playing_surface, (0, 80))
    else:
        screen.blit(paused_surface, (0, 80))
    if friction:
        screen.blit(friction_on_surface, (0, 60))
    else:
        screen.blit(friction_off_surface, (0, 60))

    pygame.display.flip()

    dt = clock.tick(fps) / 50

pygame.quit()
