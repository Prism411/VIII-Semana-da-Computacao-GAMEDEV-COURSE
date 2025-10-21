import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Controlando FPS")

# NOVO: Criar objeto Clock para controlar FPS
clock = pygame.time.Clock()

running = True
while running:
    # NOVO: Limitar a 60 FPS (60 frames por segundo)
    clock.tick(60)
    print(clock.get_fps())  # Exibe o FPS atual no console
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 100, 200))
    pygame.display.flip()

pygame.quit()
sys.exit()