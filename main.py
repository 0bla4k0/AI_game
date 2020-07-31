import pygame
pygame.init()
clock = pygame.time.Clock() # Задаем функцию кол-ва кадров

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h # Берем данные о монеторе пользователя, чтобы указать границы поля игры.
global window
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Выводим во весь экран игру, без данных выше.
pygame.display.set_caption("AI")
# x, y = 300, 300
# x1, y1 = 600, 600
# x2, y2 = 800, 800
# x3, y3 = 1000, 1000
# line_x, line_y = x + 53, y + 29
# line_x_1, line_y_1 = x1 + 53, y1 + 12
# line_x_2, line_y_2 = x1 + 53, y1 + 47
# per_INPUT_BLOCK = False
# per_SECOND_BLOCK = False
# per_THIRD_BLOCK = False
# per_FOURTH_BLOCK = False
# line_first = False
# line_SECOND_1_BLOCK = False
# line_SECOND_2_BLOCK = False
# VAR_FROM_INPUT_BLOCK = 0
# VAR_FROM_SECOND_BLOCK_1 = 0
# VAR_FROM_SECOND_BLOCK_2 = 0

def game_loop():
    global window
    x, y = 300, 300
    x1, y1 = 600, 600
    x2, y2 = 800, 800
    x3, y3 = 1000, 1000
    line_x, line_y = x + 53, y + 29
    line_x_1, line_y_1 = x1 + 53, y1 + 12
    line_x_2, line_y_2 = x1 + 53, y1 + 47
    per_INPUT_BLOCK = False
    per_SECOND_BLOCK = False
    per_THIRD_BLOCK = False
    per_FOURTH_BLOCK = False
    line_first = False
    line_SECOND_1_BLOCK = False
    line_SECOND_2_BLOCK = False
    VAR_FROM_INPUT_BLOCK = 0
    VAR_FROM_SECOND_BLOCK_1 = 0
    VAR_FROM_SECOND_BLOCK_2 = 0
    while True:
        keys = pygame.key.get_pressed()
        window.fill((0, 0, 0))
        pygame.draw.line(window, (255, 0, 0), [x + 53, y + 29], [line_x, line_y],
                         4)  # LINE FROM INPUT BLOCK TO SECOND
        pygame.draw.line(window, (255, 0, 0), [x1 + 53, y1 + 12], [line_x_1, line_y_1],
                         4)  # LINE FROM INPUT BLOCK TO SECOND
        pygame.draw.line(window, (255, 0, 0), [x1 + 53, y1 + 47], [line_x_2, line_y_2],
                         4)  # LINE FROM INPUT BLOCK TO SECOND
        pygame.draw.rect(window, (0, 0, 255), (x, y, 60, 60)) # INPUT BLOCK
        pygame.draw.rect(window, (255, 255, 255), (1500, 600, 120, 60))  #
        pygame.draw.rect(window, (17, 243, 0), (x + 50, y + 25, 10, 10))  # SMALL OUTPUT FROM INPUT BLOCK
        pygame.draw.rect(window, (0, 0, 255), (x1, y1, 60, 60)) # SECOND BLOCK
        pygame.draw.rect(window, (0, 0, 255), (x2, y2, 60, 60)) # 3 block
        pygame.draw.rect(window, (0, 0, 255), (x3, y3, 60, 60)) # 4 block
        pygame.draw.rect(window, (17, 243, 0), (x2, y2 + 25, 10, 10))  # 3 BLOCK INPUT
        pygame.draw.rect(window, (17, 243, 0), (x3, y3 + 25, 10, 10))  # 4 BLOCK INPUT
        pygame.draw.rect(window, (17, 243, 0), (x1, y1 + 25, 10, 10)) # SECOND BLOCK INPUT
        pygame.draw.rect(window, (17, 243, 0), (x1 + 50, y1 + 12, 10, 10)) # SECOND BLOCK OUTPUT 1
        pygame.draw.rect(window, (17, 243, 0), (x1 + 50, y1 + 36, 10, 10)) # SECOND BLOCK OUTPUT 2
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < event.pos[0] < x + 50 and y < event.pos[1] < y + 60:        # УЗНАЕМ НАХОДИТЬСЯ ЛИ КУРСОР В ОБЛАСТИ ВХОДНОГО ПРЯМОУГОЛЬНИКА
                    per_INPUT_BLOCK = True
                if x1 < event.pos[0] < x1 + 50 and y1 < event.pos[1] < y1 + 60:     # УЗНАЕМ НАХОДИТЬСЯ ЛИ КУРСОР В ОБЛАСТИ ВТРОГО БЛОКА
                    per_SECOND_BLOCK = True
                if x2 < event.pos[0] < x2 + 50 and y2 < event.pos[1] < y2 + 60:        # УЗНАЕМ НАХОДИТЬСЯ ЛИ КУРСОР В ОБЛАСТИ ТРЕТЬЕГО БЛОКА
                    per_THIRD_BLOCK = True
                if x3 < event.pos[0] < x3 + 50 and y3 < event.pos[1] < y3 + 60:     # УЗНАЕМ НАХОДИТЬСЯ ЛИ КУРСОР В ОБЛАСТИ ЧЕТВЕРТОГО БЛОКА
                    per_FOURTH_BLOCK = True
                if x + 50 < event.pos[0] < x + 60 and y + 25 < event.pos[1] < y + 35: # УЗНАЕМ НАХОДИТЬСЯ ЛИ КУРСОР В ОБЛАСТИ КВАДРАТА ЛИНИИ ПЕРВОГО БЛОКА
                    line_first = True
                if x1 + 50 < event.pos[0] < x1 + 60 and y1 <= event.pos[1] <= y1 + 25: # УЗНАЕМ НАХОДИТЬСЯ ЛИ КУРСОР В ОБЛАСТИ КВАДРАТА ЛИНИИ ВТОРОГО БЛОКА 1
                    line_SECOND_1_BLOCK = True
                if x1 + 50 < event.pos[0] < x1 + 60 and y1 + 30 < event.pos[1] < y1 + 60: # УЗНАЕМ НАХОДИТЬСЯ ЛИ КУРСОР В ОБЛАСТИ КВАДРАТА ЛИНИИ ВТОРОГО БЛОКА 2
                    line_SECOND_2_BLOCK = True

            if event.type == pygame.MOUSEBUTTONUP:    # ЕСЛИ БЛОК НЕ УДЕРЖИВАЕТСЯ, ТО СБРОС
                per_INPUT_BLOCK = False
                per_SECOND_BLOCK = False
                per_THIRD_BLOCK = False
                per_FOURTH_BLOCK = False
                line_first = False
                line_SECOND_1_BLOCK = False
                line_SECOND_2_BLOCK = False
                if VAR_FROM_INPUT_BLOCK == 0:                           # ЕСЛИ ЛИНИЯ НЕ ЗАЦЕИЛАСЬ, ТО СБРОС ДО ИСХОДНОГО СОСТОЯНИЯ
                    line_x, line_y = x + 53, y + 29
                if VAR_FROM_SECOND_BLOCK_1 == 0:
                    line_x_1, line_y_1 = x1 + 53, y1 + 12
                if VAR_FROM_SECOND_BLOCK_2 == 0:
                    line_x_2, line_y_2 = x1 + 53, y1 + 47

            if event.type == pygame.MOUSEMOTION and line_first == True:
                line_x, line_y = event. pos[0], event.pos[1]
                if x1 <= line_x <= x1 + 15 and y1 <= line_y <= y1 + 60:
                    line_x, line_y = x1 + 5, y1 + 30
                    VAR_FROM_INPUT_BLOCK = 1
                else:
                    VAR_FROM_INPUT_BLOCK = 0

            if event.type == pygame.MOUSEMOTION and line_SECOND_1_BLOCK == True:
                line_x_1, line_y_1 = event. pos[0], event.pos[1]
                if x2 <= line_x_1 <= x2 + 15 and y2 <= line_y_1 <= y2 + 60:
                    line_x_1, line_y_1 = x2 + 5, y2 + 30
                    VAR_FROM_SECOND_BLOCK_1 = 1
                elif x3 <= line_x_1 <= x3 + 15 and y3 <= line_y_1 <= y3 + 60:
                    line_x_1, line_y_1 = x3 + 5, y3 + 30
                    VAR_FROM_SECOND_BLOCK_1 = 2
                else:
                    VAR_FROM_SECOND_BLOCK_1 = 0

            if event.type == pygame.MOUSEMOTION and line_SECOND_2_BLOCK == True:
                line_x_2, line_y_2 = event. pos[0], event.pos[1]
                if x2 <= line_x_2 <= x2 + 15 and y2 <= line_y_2 <= y2 + 60:
                    line_x_2, line_y_2 = x2 + 5, y2 + 30
                    VAR_FROM_SECOND_BLOCK_2 = 1
                elif x3 <= line_x_2 <= x3 + 15 and y3 <= line_y_2 <= y3 + 60:
                    line_x_2, line_y_2 = x3 + 5, y3 + 30
                    VAR_FROM_SECOND_BLOCK_2 = 2
                else:
                    VAR_FROM_SECOND_BLOCK_2 = 0

            # КУБЫ
            if event.type == pygame.MOUSEMOTION and per_SECOND_BLOCK == True:
                x1, y1 = event.pos[0] - 30, event.pos[1] - 30
                if VAR_FROM_INPUT_BLOCK == 1:
                    line_x, line_y = x1 + 5, y1 + 30
                if VAR_FROM_SECOND_BLOCK_1 == 1:
                    line_x_1, line_y_1 = x2 + 5, y2 + 30
                if VAR_FROM_SECOND_BLOCK_1 == 2:
                    line_x_1, line_y_1 = x3 + 5, y3 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 1:
                    line_x_2, line_y_2 = x2 + 5, y2 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 2:
                    line_x_2, line_y_2 = x3 + 5, y3 + 30
                if VAR_FROM_SECOND_BLOCK_1 == 0:
                    line_x_1, line_y_1 = x1 + 5, y1 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 0:
                    line_x_2, line_y_2 = x1 + 5, y1 + 30
            if event.type == pygame.MOUSEMOTION and per_THIRD_BLOCK == True:
                x2, y2 = event.pos[0] - 30, event.pos[1] - 30
                if VAR_FROM_INPUT_BLOCK == 1:
                    line_x, line_y = x1 + 5, y1 + 30
                if VAR_FROM_SECOND_BLOCK_1 == 1:
                    line_x_1, line_y_1 = x2 + 5, y2 + 30
                if VAR_FROM_SECOND_BLOCK_1 == 2:
                    line_x_1, line_y_1 = x3 + 5, y3 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 1:
                    line_x_2, line_y_2 = x2 + 5, y2 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 2:
                    line_x_2, line_y_2 = x3 + 5, y3 + 30
            if event.type == pygame.MOUSEMOTION and per_FOURTH_BLOCK == True:
                x3, y3 = event.pos[0] - 30, event.pos[1] - 30
                if VAR_FROM_INPUT_BLOCK == 1:
                    line_x, line_y = x1 + 5, y1 + 30
                if VAR_FROM_SECOND_BLOCK_1 == 1:
                    line_x_1, line_y_1 = x2 + 5, y2 + 30
                if VAR_FROM_SECOND_BLOCK_1 == 2:
                    line_x_1, line_y_1 = x3 + 5, y3 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 1:
                    line_x_2, line_y_2 = x2 + 5, y2 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 2:
                    line_x_2, line_y_2 = x3 + 5, y3 + 30
            if event.type == pygame.MOUSEMOTION and per_INPUT_BLOCK == True:
                x, y = event. pos[0] - 30, event.pos[1] - 30
                if VAR_FROM_INPUT_BLOCK == 1:
                    line_x, line_y = x1 + 5, y1 + 30
                if VAR_FROM_INPUT_BLOCK == 0:
                    line_x, line_y = x + 5, y + 30
                if VAR_FROM_SECOND_BLOCK_1 == 1:
                    line_x_1, line_y_1 = x2 + 5, y2 + 30
                if VAR_FROM_SECOND_BLOCK_1 == 2:
                    line_x_1, line_y_1 = x3 + 5, y3 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 1:
                    line_x_2, line_y_2 = x2 + 5, y2 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 2:
                    line_x_2, line_y_2 = x3 + 5, y3 + 30
                if VAR_FROM_SECOND_BLOCK_1 == 0:
                    line_x_1, line_y_1 = x1 + 5, y1 + 30
                if VAR_FROM_SECOND_BLOCK_2 == 0:
                    line_x_2, line_y_2 = x1 + 5, y1 + 30
            if event.type == pygame.QUIT:
                pygame.quit()
            if keys[pygame.K_ESCAPE]:
                exit()
            click = pygame.mouse.get_pressed()
            if click[0] == 1 and 1500 <= event.pos[0] <= 1620 and 600 <= event.pos[1] <= 660:
                window = pygame.display.set_mode((1920, 1080))
                pygame.draw.rect(window, (255, 255, 255), (1500, 600, 120, 60))
                pygame.time.delay(100)
                pygame.draw.rect(window, (255, 0, 0), (1500, 600, 120, 60))
                pause(VAR_FROM_INPUT_BLOCK + VAR_FROM_SECOND_BLOCK_1 + VAR_FROM_SECOND_BLOCK_2)
        pygame.display.update()

def print_text(message, x, y, font_colour, font_size=45):
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    window.blit(text, (x, y))

def pause(m):
    paus = True
    while paus:
        for event in pygame.event.get():

            if m == 4:
                print_text("COoL, хуй", 600, 600, (255, 0, 0), 120)
            else:
                print_text("LOX", 600, 600, (255, 0, 0), 400)

            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paus = False
                game_loop()
            pygame.display.update()

game_loop()


# while 1:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             exit()
#
#     window.fill((255, 255, 255))
#
#     if pygame.mouse.get_focused():
#         pos = pygame.mouse.get_pos()
#         pygame.draw.rect(window, (0, 0, 162), (pos[0] - 10, pos[1] - 10, 20, 20))
#
#     pygame.display.update()
#
#     pygame.time.delay(20)

