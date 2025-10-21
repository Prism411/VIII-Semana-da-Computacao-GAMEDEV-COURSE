import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Coletando Moeda")
clock = pygame.time.Clock()

# Quadrado (player)
quadrado_x = 175
quadrado_y = 125
tamanho = 50
velocidade = 5

# Círculo (moeda)
circulo_x = 100
circulo_y = 100
circulo_raio = 20
moeda_coletada = False  # NOVO: Flag para saber se coletou

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
    
    # NOVO: Criar retângulos para colisão
    # Retângulo do quadrado
    rect_quadrado = pygame.Rect(quadrado_x, quadrado_y, tamanho, tamanho)
    # Retângulo ao redor do círculo (aproximação)
    rect_circulo = pygame.Rect(circulo_x - circulo_raio, 
                                circulo_y - circulo_raio,
                                circulo_raio * 2, 
                                circulo_raio * 2)
    
    # NOVO: Verificar colisão
    if rect_quadrado.colliderect(rect_circulo) and not moeda_coletada:
        moeda_coletada = True  # Marca como coletada
        print("Moeda coletada!")  # Mensagem no terminal
    
    # Desenhar tudo
    screen.fill((50, 50, 50))
    
    # NOVO: Só desenha o círculo se NÃO foi coletado
    if not moeda_coletada:
        pygame.draw.circle(screen, (255, 255, 0), (circulo_x, circulo_y), circulo_raio)
    
    pygame.draw.rect(screen, (255, 0, 0), (quadrado_x, quadrado_y, tamanho, tamanho))
    
    pygame.display.flip()

pygame.quit()
sys.exit()