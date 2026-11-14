# main.py
import pygame
import math
from data import CONSTELLATIONS
from recognizer import recognize

pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Угадай созвездие")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28)

stars = []          # звёзды, которые поставил игрок
lines = []          # пары индексов звёзд
selected = None     # звезда, с которой начинаем линию
message = "Ставь звёзды кликом, соединяй правой кнопкой. Enter — проверить."

def find_star(pos, radius=15):
    """Возвращает номер звезды рядом с кликом или None."""
    for i, s in enumerate(stars):
        if math.dist(pos, s) < radius:
            return i
    return None

running = True
while running:
    # 1. Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:                  # левая кнопка — новая звезда
                stars.append(event.pos)
            elif event.button == 3:                # правая — соединить
                i = find_star(event.pos)
                if i is not None:
                    if selected is None:
                        selected = i
                    else:
                        lines.append((selected, i))
                        selected = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and len(stars) >= 3:
                result = recognize(stars, CONSTELLATIONS)
                message = f"Похоже на: {result[0][0]}"
            elif event.key == pygame.K_c:          # C — очистить
                stars.clear(); lines.clear()

    # 2. Отрисовка
    screen.fill((8, 10, 30))                       # тёмно-синее небо
    for a, b in lines:
        pygame.draw.line(screen, (120, 160, 255), stars[a], stars[b], 2)
    for s in stars:
        pygame.draw.circle(screen, (255, 255, 220), s, 5)
    screen.blit(font.render(message, True, (230, 230, 255)), (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
