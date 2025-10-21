import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Desenhando Formas")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Limpa a tela
    screen.fill((50, 50, 50))  # Cinza escuro
    
    # NOVO: Desenhar um retângulo vermelho
    # pygame.draw.rect(tela, cor, (x, y, largura, altura))
    pygame.draw.rect(screen, (255, 0, 0), (175, 125, 50, 50))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
