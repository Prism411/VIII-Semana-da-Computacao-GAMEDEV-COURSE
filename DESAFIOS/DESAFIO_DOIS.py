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
                cor_fundo = (200, 0, 0)  # Vermelho
            elif event.key == pygame.K_g:  # Tecla G
                cor_fundo = (0, 200, 0)  # Verde
            elif event.key == pygame.K_b:  # Tecla B
                cor_fundo = (0, 0, 200)  # Azul
    
    # NOVO: Usar a variável cor_fundo
    screen.fill(cor_fundo)
    pygame.display.flip()

pygame.quit()
sys.exit()