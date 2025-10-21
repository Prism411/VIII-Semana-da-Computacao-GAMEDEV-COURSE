import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Quadrado e Círculo")
clock = pygame.time.Clock()

# Quadrado
quadrado_x = 175
quadrado_y = 125
tamanho = 50
velocidade = 5

# NOVO: Círculo (uma "moeda")
circulo_x = 100
circulo_y = 100
circulo_raio = 20

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        quadrado_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        quadrado_x += velocidade
    if teclas[pygame.K_UP]:
        quadrado_y -= velocidade
    if teclas[pygame.K_DOWN]:
        quadrado_y += velocidade
    
    # Limitar bordas
    if quadrado_x < 0:
        quadrado_x = 0
    if quadrado_x > 400 - tamanho:
        quadrado_x = 400 - tamanho
    if quadrado_y < 0:
        quadrado_y = 0
    if quadrado_y > 300 - tamanho:
        quadrado_y = 300 - tamanho
    
    # Desenhar tudo
    screen.fill((50, 50, 50))
    
    # NOVO: Desenhar círculo
    # pygame.draw.circle(tela, cor, (centro_x, centro_y), raio)
    pygame.draw.circle(screen, (255, 255, 0), (circulo_x, circulo_y), circulo_raio)
    
    # Desenhar quadrado (por cima)
    pygame.draw.rect(screen, (255, 0, 0), (quadrado_x, quadrado_y, tamanho, tamanho))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
