# Introdução ao Game Dev com Pygame

## Sobre o Curso

Este repositório contém todos os exercícios e desafios desenvolvidos durante a **VIII Semana da Computação**, no curso de **Introdução ao Game Dev** ministrado por **Jáder Louis de Souza Gonçalves**.

O curso oferece uma introdução prática ao desenvolvimento de jogos utilizando Python e a biblioteca Pygame, cobrindo desde conceitos básicos até a criação de um jogo funcional com mecânicas de colisão e pontuação.

---

## Estrutura do Projeto

```
INTRODUCAO A GAME DEV/
│
├── TESTES/                    # Exercícios progressivos de aprendizado
│   ├── Teste_UM.py           # Teste 01: Criação de janela básica
│   ├── Teste_DOIS.py         # Teste 02: Detecção de eventos de teclado
│   ├── Teste_TRES.py         # Teste 03: Desenho de formas geométricas
│   └── Teste_QUATRO.py       # Teste 04: Movimentação e colisão com círculo
│
├── DESAFIOS/                  # Desafios práticos incrementais
│   ├── DESAFIO_UM.py         # Desafio 01: Controle de FPS
│   ├── DESAFIO_DOIS.py       # Desafio 02: Sistema de cores interativo
│   ├── DESAFIO_TRES.py       # Desafio 03: Movimentação de quadrado
│   ├── DESAFIO_QUATRO        # Desafio 04: Limitação de bordas
│   ├── DESAFIO_CINCO.py      # Desafio 05: Coleta de moeda simples
│   └── DESAFIO_FINAL.py      # Desafio Final: Sistema completo de coleta
│
├── Curso VIII Semana Comp.pdf
├── Dinamicas VIII semana COMP.pdf
└── SLIDE_AULA_01.pdf
```

---

## Requisitos

### Dependências

- **Python 3.x**
- **Pygame**

### Instalação

```bash
pip install pygame
```

---

## Conteúdo do Curso

### TESTES - Exercícios Progressivos

#### [Teste_UM.py](TESTES/Teste_UM.py)
**Objetivo:** Criar uma janela básica do Pygame

**Conceitos abordados:**
- Inicialização do Pygame (`pygame.init()`)
- Criação de janela/tela (400x300 pixels)
- Loop principal do jogo (`while running`)
- Sistema de eventos (`pygame.event.get()`)
- Preenchimento de tela com cor (`screen.fill()`)
- Atualização de display (`pygame.display.flip()`)
- Encerramento correto do jogo

**Como executar:**
```bash
python TESTES/Teste_UM.py
```

---

#### [Teste_DOIS.py](TESTES/Teste_DOIS.py)
**Objetivo:** Implementar detecção de eventos de teclado

**Conceitos abordados:**
- Controle de FPS (`pygame.time.Clock()`)
- Detecção de teclas pressionadas (`pygame.KEYDOWN`)
- Tratamento de eventos específicos (tecla R)
- Variáveis de estado (`cor_fundo`)

**Como executar:**
```bash
python TESTES/Teste_DOIS.py
```

**Controles:**
- Pressione **R** para testar detecção (mensagem no console)

---

#### [Teste_TRES.py](TESTES/Teste_TRES.py)
**Objetivo:** Desenhar formas geométricas na tela

**Conceitos abordados:**
- Desenho de retângulos (`pygame.draw.rect()`)
- Sistema de coordenadas (x, y, largura, altura)
- Cores RGB
- Limpeza de tela a cada frame

**Como executar:**
```bash
python TESTES/Teste_TRES.py
```

---

#### [Teste_QUATRO.py](TESTES/Teste_QUATRO.py)
**Objetivo:** Criar movimentação controlável e adicionar objetos de coleta

**Conceitos abordados:**
- Desenho de círculos (`pygame.draw.circle()`)
- Movimentação com setas do teclado
- Sistema de velocidade
- Limitação de movimento nas bordas da tela
- Múltiplos objetos na tela

**Como executar:**
```bash
python TESTES/Teste_QUATRO.py
```

**Controles:**
- **Setas direcionais:** Mover quadrado vermelho
- O quadrado não pode sair da tela

---

### DESAFIOS - Exercícios Práticos

#### [DESAFIO_UM.py](DESAFIOS/DESAFIO_UM.py)
**Objetivo:** Implementar controle de FPS

**Conceitos:**
- Objeto `Clock` para controle de frames
- Limitação a 60 FPS
- Exibição de FPS no console

**Como executar:**
```bash
python DESAFIOS/DESAFIO_UM.py
```

---

#### [DESAFIO_DOIS.py](DESAFIOS/DESAFIO_DOIS.py)
**Objetivo:** Criar sistema interativo de mudança de cores

**Conceitos:**
- Múltiplos eventos de teclado
- Mudança dinâmica de cores
- Estruturas condicionais (if/elif)

**Como executar:**
```bash
python DESAFIOS/DESAFIO_DOIS.py
```

**Controles:**
- **R:** Vermelho
- **G:** Verde
- **B:** Azul

---

#### [DESAFIO_TRES.py](DESAFIOS/DESAFIO_TRES.py)
**Objetivo:** Implementar movimentação suave de um quadrado

**Conceitos:**
- `pygame.key.get_pressed()` para movimento contínuo
- Variáveis de posição (x, y)
- Sistema de velocidade
- Redesenho constante da tela

**Como executar:**
```bash
python DESAFIOS/DESAFIO_TRES.py
```

**Controles:**
- **Setas direcionais:** Mover quadrado

---

#### [DESAFIO_QUATRO](DESAFIOS/DESAFIO_QUATRO)
**Objetivo:** Adicionar limites de borda para evitar que o jogador saia da tela

**Conceitos:**
- Detecção de limites da tela
- Restrição de movimento por coordenadas
- Lógica condicional para bordas

**Como executar:**
```bash
python DESAFIOS/DESAFIO_QUATRO
```

**Controles:**
- **Setas direcionais:** Mover (limitado às bordas)

---

#### [DESAFIO_CINCO.py](DESAFIOS/DESAFIO_CINCO.py)
**Objetivo:** Implementar sistema básico de colisão e coleta

**Conceitos:**
- Criação de `pygame.Rect` para detecção de colisão
- Método `colliderect()` para verificar sobreposição
- Flags de estado (`moeda_coletada`)
- Renderização condicional de objetos

**Como executar:**
```bash
python DESAFIOS/DESAFIO_CINCO.py
```

**Mecânicas:**
- Mova o quadrado vermelho até tocar a moeda amarela
- Mensagem de confirmação no console
- Moeda desaparece após coleta

---

#### [DESAFIO_FINAL.py](DESAFIOS/DESAFIO_FINAL.py) ⭐
**Objetivo:** Criar um jogo completo de coleta de moedas com geração aleatória

**Conceitos:**
- Módulo `random` para posições aleatórias
- Função `gerar_posicao_moeda()` personalizada
- Sistema de pontuação
- Regeneração de objetos coletáveis
- Jogo infinito com mecânica contínua

**Como executar:**
```bash
python DESAFIOS/DESAFIO_FINAL.py
```

**Mecânicas:**
- Controle o quadrado vermelho com as setas
- Colete moedas amarelas que aparecem aleatoriamente
- Cada moeda coletada aumenta a pontuação
- Nova moeda aparece automaticamente após coleta
- Pontuação exibida no console

**Controles:**
- **Setas direcionais:** Mover jogador
- **ESC ou fechar janela:** Sair do jogo

---

## Progressão de Aprendizado

O curso segue uma progressão didática clara:

1. **Fundamentos** → Criação de janela, loop de jogo, eventos
2. **Renderização** → Cores, formas geométricas, desenhos
3. **Interatividade** → Controle por teclado, detecção de input
4. **Movimento** → Posicionamento dinâmico, velocidade, FPS
5. **Física básica** → Colisão com bordas, limitação de área
6. **Game mechanics** → Detecção de colisão entre objetos
7. **Gameplay** → Sistema de pontuação, geração procedural

---

## Conceitos-Chave do Pygame

### Loop Principal do Jogo
```python
running = True
while running:
    # 1. Processar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Atualizar lógica do jogo
    # (movimento, colisões, pontuação)

    # 3. Desenhar na tela
    screen.fill(cor_fundo)
    pygame.draw.rect(screen, cor, (x, y, w, h))

    # 4. Atualizar display
    pygame.display.flip()
```

### Sistema de Coordenadas
- Origem (0,0) no canto **superior esquerdo**
- X aumenta para a **direita**
- Y aumenta para **baixo**

### Cores RGB
```python
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
cinza_escuro = (50, 50, 50)
```

### Detecção de Colisão
```python
rect1 = pygame.Rect(x1, y1, largura1, altura1)
rect2 = pygame.Rect(x2, y2, largura2, altura2)

if rect1.colliderect(rect2):
    # Houve colisão!
```

---

## Recursos Adicionais

### Documentação Incluída
- **Curso VIII Semana Comp.pdf** - Material teórico completo
- **Dinamicas VIII semana COMP.pdf** - Atividades propostas
- **SLIDE_AULA_01.pdf** - Slides da primeira aula

### Links Úteis
- [Documentação oficial do Pygame](https://www.pygame.org/docs/)
- [Pygame Wiki](https://www.pygame.org/wiki/)
- [Tutoriais Pygame](https://www.pygame.org/wiki/tutorials)

---

## Autor

**Instrutor:** Jáder Louis de Souza Gonçalves
**Evento:** VIII Semana da Computação

---

## Licença

Material educacional desenvolvido para fins didáticos.

---

## Próximos Passos

Após completar este curso, você pode:

1. Adicionar sistema de **vidas** e **game over**
2. Implementar **inimigos** que se movem
3. Criar diferentes **níveis de dificuldade**
4. Adicionar **sprites e imagens** em vez de formas geométricas
5. Implementar **sons e música**
6. Criar um **menu inicial** e **tela de pontuação**
7. Adicionar **power-ups** e **obstáculos**
8. Salvar **recordes** em arquivo

---

**Divirta-se programando!**
