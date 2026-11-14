#!/usr/bin/python3
"""Черепашка рисует жабу."""
import turtle

# ---------- Настройки ----------
t = turtle.Turtle()
t.speed(0)              # максимум (0 = без задержки)
t.hideturtle()
turtle.bgcolor("#e8f5d0")   # светлый болотный фон
turtle.title("Жаба")

# Палитра
GREEN_DARK  = "#3b6b2a"
GREEN_BODY  = "#6fa83a"
GREEN_LIGHT = "#a4c96b"
BELLY       = "#d8e8a8"
EYE_WHITE   = "#f7f7e8"
PUPIL       = "#1a1a1a"
SPOT        = "#4a7a2a"
MOUTH       = "#2b3f1a"

# ---------- Вспомогательные ----------
def jump(x, y):
    """Переместиться без линии."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def ellipse(rx, ry, color, outline=None, width=2):
    """Эллипс с центром в текущей позиции (рисуем через сжатие окружности)."""
    t.penup()
    t.setheading(0)
    t.fillcolor(color)
    t.pencolor(outline if outline else color)
    t.pensize(width)
    t.begin_fill()
    for _ in range(2):
        t.circle(rx, 90)
        t.circle(ry, 90)
    t.end_fill()

def filled_circle(x, y, r, color, outline=None, width=2):
    jump(x, y - r)
    t.setheading(0)
    t.fillcolor(color)
    t.pencolor(outline if outline else color)
    t.pensize(width)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# ---------- Рисуем жабу ----------

# Тело (низ — шире)
jump(0, -120)
ellipse(140, 100, GREEN_BODY, outline=GREEN_DARK, width=3)

# Живот (светлый овал поверх)
jump(0, -110)
ellipse(110, 70, BELLY, outline=GREEN_DARK, width=2)

# Спинка — верхняя часть головы/тела
jump(0, 40)
ellipse(130, 90, GREEN_BODY, outline=GREEN_DARK, width=3)

# Голова — сверху, чуть шире
jump(0, 90)
ellipse(120, 70, GREEN_LIGHT, outline=GREEN_DARK, width=3)

# ---------- Глаза ----------
# Правый глаз
filled_circle(70, 150, 40, EYE_WHITE, outline=GREEN_DARK, width=3)
# Левый глаз
filled_circle(-70, 150, 40, EYE_WHITE, outline=GREEN_DARK, width=3)

# Зрачки (смотрят чуть вверх-внутрь)
filled_circle(72, 158, 18, PUPIL)
filled_circle(-68, 158, 18, PUPIL)

# Блики
filled_circle(78, 165, 6, "white")
filled_circle(-62, 165, 6, "white")

# ---------- Рот ----------
jump(-45, 95)
t.setheading(-20)
t.pencolor(MOUTH)
t.pensize(4)
t.circle(60, 60)        # дуга улыбки

# ---------- Ноздри ----------
filled_circle(18, 115, 4, MOUTH)
filled_circle(-18, 115, 4, MOUTH)

# ---------- Пятна на теле ----------
spots = [
    (-90, 10, 12), (-40, -30, 10), (30, 20, 14),
    (80, -20, 10), (10, -70, 9), (-70, -80, 11),
    (55, -80, 8), (100, 30, 9),
]
for sx, sy, r in spots:
    filled_circle(sx, sy, r, SPOT)

# ---------- Лапки ----------
def leg(x, y, angle, toes=3):
    """Лапа: палочка + пальцы-кружки."""
    jump(x, y)
    t.setheading(angle)
    t.pencolor(GREEN_DARK)
    t.pensize(14)
    t.forward(60)                      # «бедро»
    # пальцы
    fx, fy = t.pos()
    for da in (-30, 0, 30):
        jump(fx, fy)
        t.setheading(angle + da)
        t.pensize(8)
        t.forward(25)
        tx, ty = t.pos()
        filled_circle(tx, ty, 8, GREEN_DARK)

# задние лапы (углом вниз-наружу)
leg(-110, -100, -150)
leg(110, -100, -30)

# передние лапы
leg(-95, 20, 200)
leg(95, 20, -20)

# ---------- Подпись ----------
jump(0, -230)
t.setheading(0)
t.pencolor(GREEN_DARK)
t.write("ква", align="center", font=("Arial", 18, "italic"))

# ---------- Готово ----------
turtle.done()
