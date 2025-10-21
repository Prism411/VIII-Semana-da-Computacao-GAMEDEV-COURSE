import pygame
import sys
import random  # Biblioteca para números aleatórios

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Coletando Moedas Aleatórias")
clock = pygame.time.Clock()

# Quadrado (player)
quadrado_x = 175
quadrado_y = 125
tamanho = 50
velocidade = 5

# Círculo (moeda)
circulo_raio = 20

# Função para gerar posição aleatória para a moeda
def gerar_posicao_moeda():
    """
    Gera uma posição aleatória dentro da tela,
    respeitando as bordas para a moeda não aparecer cortada
    """
    # randint gera um número inteiro aleatório entre min e max (inclusive)
    x = random.randint(circulo_raio, 400 - circulo_raio)
    y = random.randint(circulo_raio, 300 - circulo_raio)
    return x, y

# Gera a primeira posição da moeda
circulo_x, circulo_y = gerar_posicao_moeda()

# Contador de moedas coletadas
pontos = 0

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    teclas = pygame.key.get_pressed()
    
    # Movimentação do player
    if teclas[pygame.K_LEFT]:
        quadrado_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        quadrado_x += velocidade
    if teclas[pygame.K_UP]:
        quadrado_y -= velocidade
    if teclas[pygame.K_DOWN]:
        quadrado_y += velocidade
    
    # Limitar bordas do player
    if quadrado_x < 0:
        quadrado_x = 0
    if quadrado_x > 400 - tamanho:
        quadrado_x = 400 - tamanho
    if quadrado_y < 0:
        quadrado_y = 0
    if quadrado_y > 300 - tamanho:
        quadrado_y = 300 - tamanho
    
    # Criar retângulos para colisão
    rect_quadrado = pygame.Rect(quadrado_x, quadrado_y, tamanho, tamanho)
    rect_circulo = pygame.Rect(circulo_x - circulo_raio, 
                                circulo_y - circulo_raio,
                                circulo_raio * 2, 
                                circulo_raio * 2)
    
    # Verificar colisão com a moeda
    if rect_quadrado.colliderect(rect_circulo):
        pontos += 1  # Aumenta pontuação
        print(f"Moeda coletada! Total: {pontos}")
        
        # Gera nova posição aleatória para a moeda
        circulo_x, circulo_y = gerar_posicao_moeda()
    
    # Desenhar tudo
    screen.fill((50, 50, 50))
    
    # Desenha a moeda (sempre visível, muda de posição quando coletada)
    pygame.draw.circle(screen, (255, 255, 0), (circulo_x, circulo_y), circulo_raio)
    
    # Desenha o player
    pygame.draw.rect(screen, (255, 0, 0), (quadrado_x, quadrado_y, tamanho, tamanho))
    
    pygame.display.flip()

pygame.quit()
sys.exit()