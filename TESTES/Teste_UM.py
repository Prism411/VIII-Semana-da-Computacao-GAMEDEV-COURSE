import pygame
import sys

# Inicializa o Pygame
pygame.init()

screen = pygame.display.set_mode((400, 300)) # Cria a Tela 400x300
pygame.display.set_caption("Teste Pygame")  #Define nome da Janela

running = True # Váriavel de Controle do estado do Jogo
while running:   # Enquanto estiver rodando
  for event in pygame.event.get(): # Escuta por evento
    if event.type == pygame.QUIT: # se tiver algum evento:
      running = False # estado do jogo = falso, fim de jogo!

  # Preenche a tela com cor azul
  print("preenchendo a tela")
  screen.fill((0, 100, 200))  
  # Atualiza a tela
  pygame.display.flip()

pygame.quit() # Encerra Jogo
sys.exit() # Encerra Janela