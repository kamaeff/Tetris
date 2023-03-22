import pygame
from copy import deepcopy
from random import choice, randrange


W, H = 10, 20
Tile = 45
Game_Res = W * Tile, H * Tile
FPS = 60

pygame.init()
game_sc = pygame.display.set_mode(Game_Res)
clock = pygame.time.Clock()

animation_count, animation_speed, animation_limit = 0, 80, 1500
field = [[0 for i in range(W)] for j in range (H)]

grid = [pygame.Rect(x * Tile, y * Tile, Tile, Tile) for x in range(W) for y in range (H)]

figures_pos = [ [(-1, 0), (-2, 0), (0, 0), (1, 0)],
                [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                [(0, 0), (-1, 0), (0, 1), (-1, -1)] ]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, Tile - 2, Tile - 2)

figure = deepcopy(choice(figures))

def check():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True

while True:
    dx, rotate = 0, False
    game_sc.fill(pygame.Color('#A66F00'))
    
    # Кнопки
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                animation_limit = 100
            elif event.key == pygame.K_UP:
                rotate = True
        
            
    # Двигаем x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check():
            figure = deepcopy(figure_old)
            break
    
    # Двигаем y
    animation_count += animation_speed
    if animation_count > animation_limit:
        animation_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = pygame.Color('White')
                figure = deepcopy(choice(figures))
                animation_limit = 2000
                break
    
    # Поворот
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check(): 
                figure = deepcopy(figure_old)
                break
            
    # Обнуление
    line = H - 1
    for row in range(H - 1, -1, -1):
        count = 0
        for i in range(W):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < W:
            line -= 1    
    # Отрисовка 
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]        
            
    for i in range(4):
        figure_rect.x = figure[i].x * Tile 
        figure_rect.y = figure[i].y * Tile
        
        pygame.draw.rect(game_sc, pygame.Color('white'), figure_rect)     
        
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x * Tile, y * Tile
                pygame.draw.rect(game_sc, col, figure_rect)   
            
    pygame.display.flip()
    clock.tick(FPS)





