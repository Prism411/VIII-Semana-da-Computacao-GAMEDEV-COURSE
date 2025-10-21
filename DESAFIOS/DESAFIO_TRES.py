import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Movendo Quadrado")
clock = pygame.time.Clock()

# NOVO: Variáveis para posição do quadrado
quadrado_x = 175
quadrado_y = 125
velocidade = 5  # Pixels por frame

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # NOVO: Verifica quais teclas estão pressionadas AGORA
    teclas = pygame.key.get_pressed()
    # NOVO: Move o quadrado baseado nas teclas
    if teclas[pygame.K_LEFT]:
        quadrado_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        quadrado_x += velocidade
    if teclas[pygame.K_UP]:
        quadrado_y -= velocidade
    if teclas[pygame.K_DOWN]:
        quadrado_y += velocidade
    # Limpa a tela
    screen.fill((50, 50, 50))
    # NOVO: Desenha o quadrado na posição atualizada
    pygame.draw.rect(screen, (255, 0, 0), (quadrado_x, quadrado_y, 50, 50))
    pygame.display.flip()

pygame.quit()
sys.exit()