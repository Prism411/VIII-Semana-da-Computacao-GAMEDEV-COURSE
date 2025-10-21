import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Mudando Cores")
clock = pygame.time.Clock()

# NOVO: Variável para armazenar a cor atual
cor_fundo = (0, 100, 200)  # Começa azul

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # NOVO: Detectar teclas pressionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Tecla R
                print("R pressionado!")

    pygame.display.flip()

pygame.quit()
sys.exit()