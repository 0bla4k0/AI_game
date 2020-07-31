import random
import pygame

pygame.init()

# display_width, display_height = pygame.display.Info().current_w, pygame.display.Info().current_h # Берем информацию о мониторе пользователя
global i, m, display, k
display = pygame.display.set_mode((1920, 1080))  # Задаем полный экран для игры
pygame.display.set_caption('IF (AI == true) {}')  # Название для игры
clock = pygame.time.Clock()  # Задаем функцию кол-ва кадров
font_type = r"font\pixel_font.ttf"
icon_first_level = pygame.image.load('pictures/pic1.png')
icon_second_level = pygame.image.load('pictures/pic2.png')
icon_third_level = pygame.image.load('pictures/pic3.png')
icon_fourth_level = pygame.image.load('pictures/pic4.png')
icon_fifth_level = pygame.image.load('pictures/pic5.png')
icon_sixth_level = pygame.image.load('pictures/pic6.png')
icon_extra_level = pygame.image.load('pictures/extra pic0.png')
pic_level1 = pygame.image.load('pictures/pic1_1.png')
pic_level2 = pygame.image.load('pictures/pic2_1.png')
pic_level3 = pygame.image.load('pictures/pic3_1.png')
pic_extra_lvl = pygame.image.load('pictures/extra pic1.png')
pic_level4 = pygame.image.load('pictures/pic4_1.png')
pic_level5 = pygame.image.load('pictures/pic5_1.png')
pic_level6 = pygame.image.load('pictures/pic6_1.png')
picAI = [pygame.image.load('pictures/picAI1.png'), pygame.image.load('pictures/picAI2.png'), pygame.image.load('pictures/picAI3.png'), pygame.image.load('pictures/picAI4.png'), pygame.image.load('pictures/picAI5.png'), pygame.image.load('pictures/picAI6.png'), pygame.image.load('pictures/picAI7.png')]
img = open("cache/cache.txt", 'r')
index_img = int(img.read(1))
img.close()
InputBlock = pygame.image.load("pictures/InputBlock.png")
OutputBlock1 = pygame.image.load("pictures/OutputBlock1.png")
OutputBlock2 = pygame.image.load("pictures/OutputBlock2.png")
BinBlock = pygame.image.load("pictures/bin.png")
StudyBlock = pygame.image.load("pictures/StudyBlock.png")
EaysBlock1 = pygame.image.load('pictures/EaysLEVEL1.png')
click_mouse = pygame.mixer.Sound("sounds/click.ogg")
Eyes = [pygame.image.load('pictures/game_level1_1.png'), pygame.image.load('pictures/game_level1_2.png'), pygame.image.load('pictures/game_level1_3.png'), pygame.image.load('pictures/game_level1_4.png')]
Figures = [pygame.image.load('pictures/0.png'), pygame.image.load('pictures/tre.png'), pygame.image.load('pictures/squ.png')]
pygame.mixer.music.load("sounds/OST.mp3")
pygame.mixer.music.set_volume(0.008)
i = 1
m = 1
k = 1


class Button():
    '''
        Вводим класс для получение физических кнопок управления.
    '''

    def __init__(self, width, height):
        '''
            Получаем на вход значения ширины и высоты кнопки.
            В стандартных параметрах стоят цвета для разных ситуаций.
        '''
        self.width = width
        self.height = height
        self.active_colour = (170, 0, 0)
        self.pressed_colour = (117, 0, 0)
        self.inactive_colour = (204, 204, 204)

    def draw_button(self, x, y, message, action=None, class_button=None, image=None, text=None, active_image=None):
        '''
            Рисуем кнопки для разных ситуаций, в конце делаем текст для кнопки.
        '''
        global font_clr
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        font_clr = (0, 0, 0)
        if class_button == 1:
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(display, self.active_colour, (x, y, self.width, self.height))
                font_clr = (255, 255, 255)
                if click[0] == 1:
                    click_mouse.play()
                    pygame.draw.rect(display, self.pressed_colour, (x, y, self.width, self.height))
                    pygame.draw.rect(display, (0, 0, 162), (x - 15, y + 25, 10, 10))
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                            quit()
                        action()
            else:
                font_clr = (0, 0, 0)
                pygame.draw.rect(display, self.inactive_colour, (x, y, self.width, self.height))
                pygame.draw.rect(display, (0, 0, 162), (x - 15, y + 30, 10, 10))
        elif class_button == 2:
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(display, (0, 0, 255, 50), (x, y, self.width, self.height))
                display.blit(active_image, (x - 7, y - 5))
                pygame.draw.rect(display, (204, 204, 204), (1090, 125, 810, 817))
                text()
                if click[0] == 1:
                    click_mouse.play()
                    if action is not None:
                        action()
            else:
                display.blit(image, (x, y))
        elif class_button == 4:
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(display, (0, 0, 0), (x - 3, y - 3, self.width + 6, self.height + 6))
                pygame.draw.rect(display, (230, 65, 75), (x, y, self.width, self.height))
                font_clr = (255, 255, 255)
                if click[0] == 1:
                    click_mouse.play()
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                            quit()
                        action()
            else:
                font_clr = (0, 0, 0)
                pygame.draw.rect(display, (0, 0, 0), (x - 3, y - 3, self.width + 6, self.height + 6))
                pygame.draw.rect(display, (204, 204, 204), (x, y, self.width, self.height))
        elif class_button == 3:
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(display, (0, 0, 0), (x + 3, y + 3, self.width + 6, self.height + 6))
                pygame.draw.rect(display, (196, 196, 196), (x, y, self.width, self.height))
                font_clr = (0, 0, 0)
                if click[0] == 1:
                    click_mouse.play()
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                            quit()
                        action()
            else:
                font_clr = (240, 240, 240)
                pygame.draw.rect(display, (255, 255, 255), (x - 3, y - 3, self.width + 6, self.height + 6))
                pygame.draw.rect(display, (51, 51, 51), (x, y, self.width, self.height))
        print_text(message, x + 10, y + 10, font_clr)


def windowMOD():
    global i, display
    if i == 1:
        i = 0
        display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    else:
        i = 1
        display = pygame.display.set_mode((1920, 1080))


def musicMOD():
    global m
    if m == 1:
        m = 0
        pygame.mixer.music.pause()
    else:
        m = 1
        pygame.mixer.music.set_volume(0.008)
        pygame.mixer.music.play(-1)

colour = (68, 130, 46)

def first_level():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 58)
    text = font_type.render("ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ", True, (56, 58, 145))
    display.blit(text, (1100, 130))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 120)
    text = font_type.render("В МЕДИЦИНЕ", True, (255, 50, 50))
    display.blit(text, (1100, 165))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 40)
    text = font_type.render("#ЗАДАЧА:", True, colour)
    display.blit(text, (1100, 300))
    text = font_type.render("#ОБУЧЕНИЕ:", True, colour)
    display.blit(text, (1100, 460))
    text = font_type.render("#Плюсы:", True, colour)
    display.blit(text, (1100, 650))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 30)
    text = font_type.render("На этом уровне Вы создадите исскуственный", True, (87, 87, 87))
    display.blit(text, (1100, 350))
    text = font_type.render("интеллект, который поможет офтальмологам в", True, (87, 87, 87))
    display.blit(text, (1100, 380))
    text = font_type.render("обследовании пациентов.", True, (87, 87, 87))
    display.blit(text, (1100, 410))
    text = font_type.render("Вам предстоит использовать визуальное", True, (87, 87, 87))
    display.blit(text, (1100, 510))
    text = font_type.render("программирование, чтобы создать нейросеть.", True, (87, 87, 87))
    display.blit(text, (1100, 540))
    text = font_type.render("После вам нужно будет обучить интеллект,", True, (87, 87, 87))
    display.blit(text, (1100, 570))
    text = font_type.render("проходя мини-игру.", True, (87, 87, 87))
    display.blit(text, (1100, 600))
    text = font_type.render("Созданное Вами творение будет выводить ", True, (87, 87, 87))
    display.blit(text, (1100, 700))
    text = font_type.render("полную информацию об состоянии глаз", True, (87, 87, 87))
    display.blit(text, (1100, 730))
    text = font_type.render("пациентов, тем самым Вам удастся снизить", True, (87, 87, 87))
    display.blit(text, (1100, 760))
    text = font_type.render("нагрузку с врачей, которые могут заниматься", True, (87, 87, 87))
    display.blit(text, (1100, 790))
    text = font_type.render("чем-то более важным в этот момент.", True, (87, 87, 87))
    display.blit(text, (1100, 820))


def second_level():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 58)
    text = font_type.render("ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ", True, (56, 58, 145))
    display.blit(text, (1100, 130))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 73)
    text = font_type.render("В СОЦИАЛЬНЫХ СЕТЯХ", True, (255, 50, 50))
    display.blit(text, (1100, 180))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 40)
    text = font_type.render("#ЗАДАЧА:", True, colour)
    display.blit(text, (1100, 270))
    text = font_type.render("#ОБУЧЕНИЕ:", True, colour)
    display.blit(text, (1100, 430))
    text = font_type.render("#Плюсы:", True, colour)
    display.blit(text, (1100, 620))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 30)
    text = font_type.render("На этом уровне Вы обучите искусственный", True, (87, 87, 87))
    display.blit(text, (1100, 320))
    text = font_type.render("интеллект, который используется в популярной", True, (87, 87, 87))
    display.blit(text, (1100, 350))
    text = font_type.render("социальной сети.", True, (87, 87, 87))
    display.blit(text, (1100, 380))
    text = font_type.render("Вам предстоит использовать визуальное", True, (87, 87, 87))
    display.blit(text, (1100, 480))
    text = font_type.render("программирование, чтобы создать нейросеть.", True, (87, 87, 87))
    display.blit(text, (1100, 510))
    text = font_type.render("После вам нужно будет обучить интеллект,", True, (87, 87, 87))
    display.blit(text, (1100, 540))
    text = font_type.render("используя данные пользоватей.", True, (87, 87, 87))
    display.blit(text, (1100, 570))
    text = font_type.render("Своей работой вы сохраните время людей в", True, (87, 87, 87))
    display.blit(text, (1100, 670))
    text = font_type.render("поисках нужной информации, музыки и т.д.", True, (87, 87, 87))
    display.blit(text, (1100, 700))


def third_level():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 58)
    text = font_type.render("ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ", True, (56, 58, 145))
    display.blit(text, (1100, 130))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 89)
    text = font_type.render("НА ПРЕДПРИЯТИЯХ", True, (255, 50, 50))
    display.blit(text, (1100, 175))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 40)
    text = font_type.render("#ЗАДАЧА:", True, colour)
    display.blit(text, (1100, 280))
    text = font_type.render("#ОБУЧЕНИЕ:", True, colour)
    display.blit(text, (1100, 500))
    text = font_type.render("#Плюсы:", True, colour)
    display.blit(text, (1100, 680))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 30)
    text = font_type.render("На этом уровне вы поможете фабрике по", True, (87, 87, 87))
    display.blit(text, (1100, 330))
    text = font_type.render("производству коробок сделать нейросеть, ", True, (87, 87, 87))
    display.blit(text, (1100, 360))
    text = font_type.render("которая будет автоматически отделять", True, (87, 87, 87))
    display.blit(text, (1100, 390))
    text = font_type.render("квадратные и круглые коробки, а другие ", True, (87, 87, 87))
    display.blit(text, (1100, 420))
    text = font_type.render("будет отправлять к бракованными вещам. ", True, (87, 87, 87))
    display.blit(text, (1100, 450))
    text = font_type.render("Вам предстоит использовать визуальное", True, (87, 87, 87))
    display.blit(text, (1100, 550))
    text = font_type.render("программирование, чтобы создать нейросеть.", True, (87, 87, 87))
    display.blit(text, (1100, 580))
    text = font_type.render("После вам нужно будет обучить интеллект,", True, (87, 87, 87))
    display.blit(text, (1100, 610))
    text = font_type.render("используя много данных о формах коробок.", True, (87, 87, 87))
    display.blit(text, (1100, 640))
    text = font_type.render("Сделав это, вы ускорите работу на", True, (87, 87, 87))
    display.blit(text, (1100, 730))
    text = font_type.render("производстве, сократите травмы сотрудников,", True, (87, 87, 87))
    display.blit(text, (1100, 760))
    text = font_type.render("которые делали это в ручную, и т.д.", True, (87, 87, 87))
    display.blit(text, (1100, 790))

def fourth_level():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 58)
    text = font_type.render("ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ", True, (56, 58, 145))
    display.blit(text, (1100, 130))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 123)
    text = font_type.render("В ЧАТ-БОТАХ", True, (255, 50, 50))
    display.blit(text, (1100, 175))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 40)
    text = font_type.render("#ЗАДАЧА:", True, colour)
    display.blit(text, (1100, 315))
    text = font_type.render("#ОБУЧЕНИЕ:", True, colour)
    display.blit(text, (1100, 505))
    text = font_type.render("#Плюсы:", True, colour)
    display.blit(text, (1100, 695))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 30)
    text = font_type.render("На этом уровне вы сделаете чат-бота с", True, (87, 87, 87))
    display.blit(text, (1100, 365))
    text = font_type.render("искусственным интеллектом, который будет ", True, (87, 87, 87))
    display.blit(text, (1100, 395))
    text = font_type.render("работать в большом сервисе, отвечая на", True, (87, 87, 87))
    display.blit(text, (1100, 425))
    text = font_type.render("вопросы пользователей.", True, (87, 87, 87))
    display.blit(text, (1100, 455))
    text = font_type.render("Вам предстоит использовать визуальное", True, (87, 87, 87))
    display.blit(text, (1100, 555))
    text = font_type.render("программирование, чтобы создать нейросеть.", True, (87, 87, 87))
    display.blit(text, (1100, 585))
    text = font_type.render("После вам нужно будет обучить интеллект,", True, (87, 87, 87))
    display.blit(text, (1100, 615))
    text = font_type.render("проходя мини-игру.", True, (87, 87, 87))
    display.blit(text, (1100, 645))
    text = font_type.render("Сделав это, вы ускорите работу", True, (87, 87, 87))
    display.blit(text, (1100, 745))
    text = font_type.render("работу сервиса, тем самым уменьшите", True, (87, 87, 87))
    display.blit(text, (1100, 775))
    text = font_type.render("ожидание пользователей, сохранив им время.", True, (87, 87, 87))
    display.blit(text, (1100, 805))


def fifth_level():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 58)
    text = font_type.render("ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ", True, (56, 58, 145))
    display.blit(text, (1100, 130))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 64)
    text = font_type.render("В КОМПЬЮТЕРНЫХ ИГРАХ", True, (255, 50, 50))
    display.blit(text, (1100, 180))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 40)
    text = font_type.render("#ЗАДАЧА:", True, colour)
    display.blit(text, (1100, 260))
    text = font_type.render("#ОБУЧЕНИЕ:", True, colour)
    display.blit(text, (1100, 420))
    text = font_type.render("#Плюсы:", True, colour)
    display.blit(text, (1100, 610))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 30)
    text = font_type.render("На этом уровне вы создадите и обучите", True, (87, 87, 87))
    display.blit(text, (1100, 310))
    text = font_type.render("нейросеть, которая будет использоваться в", True, (87, 87, 87))
    display.blit(text, (1100, 340))
    text = font_type.render("новом современном шутере.", True, (87, 87, 87))
    display.blit(text, (1100, 370))
    text = font_type.render("Вам предстоит использовать визуальное", True, (87, 87, 87))
    display.blit(text, (1100, 470))
    text = font_type.render("программирование, чтобы создать ИИ.", True, (87, 87, 87))
    display.blit(text, (1100, 500))
    text = font_type.render("После вам нужно будет обучить интеллект,", True, (87, 87, 87))
    display.blit(text, (1100, 530))
    text = font_type.render("проходя мини-игру.", True, (87, 87, 87))
    display.blit(text, (1100, 560))
    text = font_type.render("Своей работой вы разнообразите геймплей", True, (87, 87, 87))
    display.blit(text, (1100, 660))
    text = font_type.render("игры, сохронив у пользователя желание играть", True, (87, 87, 87))
    display.blit(text, (1100, 690))
    text = font_type.render("следующий раз.", True, (87, 87, 87))
    display.blit(text, (1100, 720))


def sixth_level():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 58)
    text = font_type.render("ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ", True, (56, 58, 145))
    display.blit(text, (1100, 130))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 135)
    text = font_type.render("В МАШИНАХ", True, (255, 50, 50))
    display.blit(text, (1100, 165))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 40)
    text = font_type.render("#ЗАДАЧА:", True, colour)
    display.blit(text, (1100, 320))
    text = font_type.render("#ОБУЧЕНИЕ:", True, colour)
    display.blit(text, (1100, 450))
    text = font_type.render("#Плюсы:", True, colour)
    display.blit(text, (1100, 640))
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 30)
    text = font_type.render("На этом уровне Вы создадите автомобиль", True, (87, 87, 87))
    display.blit(text, (1100, 370))
    text = font_type.render("с автопилотом на основе нейросетей", True, (87, 87, 87))
    display.blit(text, (1100, 400))
    text = font_type.render("Вам предстоит использовать визуальное", True, (87, 87, 87))
    display.blit(text, (1100, 500))
    text = font_type.render("программирование, чтобы создать нейросеть.", True, (87, 87, 87))
    display.blit(text, (1100, 530))
    text = font_type.render("После вам нужно будет обучить интеллект,", True, (87, 87, 87))
    display.blit(text, (1100, 560))
    text = font_type.render("проходя мини-игру.", True, (87, 87, 87))
    display.blit(text, (1100, 590))
    text = font_type.render("Созданное Вами творение, возможно, сделает", True, (87, 87, 87))
    display.blit(text, (1100, 690))
    text = font_type.render("прорыв в этом направлении, снизит количество", True, (87, 87, 87))
    display.blit(text, (1100, 720))
    text = font_type.render("ДТП на дорогах, сделает жизнь более удобней.", True, (87, 87, 87))
    display.blit(text, (1100, 750))


def const_text():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 33)
    text = font_type.render('Ваш искусственный интеллект развит на 100%', True, (87, 87, 87))
    text1 = font_type.render('Выбирайте уровень и начинайте играть!', True, (87, 87, 87))
    img = open("cache/cache.txt", 'r')
    index_img = int(img.read(1))
    img.close()
    display.blit(picAI[index_img], (1070, 132))
    display.blit(text, (1090, 902))
    display.blit(text1, (1140, 132))


def menu_game():
    global k
    if k == 1:
        pygame.mixer.music.play(-1)
        k = 0
    start_button = Button(350, 65)
    quit_button = Button(170, 65)
    windowMOD_button = Button(180, 65)
    musicMOD_button = Button(210, 65)
    show = True
    while show:
        font_type = r"font\pixel_font.ttf"
        font_type = pygame.font.Font(font_type, 45)
        UPPER_MENU(1)
        decoration_for_menu()
        description_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 240 < mouse[0] < 340 and 50 < mouse[1] < 100 and click[0] == 1:
            click_mouse.play()
            game_loop()
        if 370 < mouse[0] < 500 and 50 < mouse[1] < 100 and click[0] == 1:
            pygame.quit()
            quit()
        if i == 0:
            text = font_type.render("ВЫКЛ", True, (170, 55, 55))
        else:
            text = font_type.render("ВКЛ", True, (86, 163, 59))
        if m == 0:
            text1 = font_type.render("ВЫКЛ", True, (170, 55, 55))
        else:
            text1 = font_type.render("ВКЛ", True, (86, 163, 59))
        display.blit(text, (290, 215))
        display.blit(text1, (290, 280))
        start_button.draw_button(50, 135, "Выбор уровня", start_game, 1)
        windowMOD_button.draw_button(50, 205, "В окне: ", windowMOD, 1)
        musicMOD_button.draw_button(50, 275, "Музыка: ", musicMOD, 1)
        quit_button.draw_button(50, 345, "Выход", quit, 1)
        pygame.display.update()
        clock.tick(60)


def description_menu():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 40)
    text = font_type.render('"if AI == true" - это игра,', True, (87, 87, 87))
    display.blit(text, (1330, 120))

    def description_menu_2():
        font_type = r"font\pixel_font.ttf"
        font_type = pygame.font.Font(font_type, 30)
        text = font_type.render("в которой Вы в игровой форме", True, (87, 87, 87))
        display.blit(text, (1330, 165))
        text = font_type.render("узнаете, что такое искусственный", True, (87, 87, 87))
        display.blit(text, (1330, 195))
        text = font_type.render("интеллект, путем решения не", True, (87, 87, 87))
        display.blit(text, (1330, 225))
        text = font_type.render("сложных головоломок. После каж-", True, (87, 87, 87))
        display.blit(text, (1330, 255))
        text = font_type.render("дого уровня будет ссылка на", True, (87, 87, 87))
        display.blit(text, (1330, 285))
        text = font_type.render("источник с полной информацией.", True, (87, 87, 87))
        display.blit(text, (1330, 315))
        text = font_type.render("В течении игры Вы будете помо-", True, (87, 87, 87))
        display.blit(text, (1330, 345))
        text = font_type.render("гать нейрону, который в конце", True, (87, 87, 87))
        display.blit(text, (1330, 375))
        text = font_type.render("игры наградит вас полезной", True, (87, 87, 87))
        display.blit(text, (1330, 405))
        text = font_type.render("информацией об AI.", True, (87, 87, 87))
        display.blit(text, (1330, 435))
        text = font_type.render("Читайте, учите, применяйте!", True, (87, 87, 87))
        display.blit(text, (1330, 510))
        text = font_type.render("Alexey Kosenko, 2020", True, (87, 87, 87))
        display.blit(text, (1330, 540))

    description_menu_2()


def decoration_for_menu():
    pygame.draw.line(display, (24, 24, 162), [1320, 120], [1320, 960], 4)
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 35)
    text = font_type.render("// Пункт выбора уровней игры", True, (87, 87, 87))
    display.blit(text, (500, 150))
    text = font_type.render("// Переключение режима экрана", True, (87, 87, 87))
    display.blit(text, (500, 220))
    text = font_type.render("// ВКЛ-ВЫКЛ МУЗЫКИ", True, (87, 87, 87))
    display.blit(text, (500, 290))
    text = font_type.render("// Выход из игры", True, (87, 87, 87))
    display.blit(text, (500, 360))
    text = font_type.render("Manufacturer: Intel", True, (87, 87, 87))
    display.blit(text, (50, 430))
    text = font_type.render("Brand String: Intel(R) Core(TM) i7 CPU", True, (87, 87, 87))
    display.blit(text, (50, 465))
    text = font_type.render("Cache L1: 256 KB", True, (87, 87, 87))
    display.blit(text, (50, 500))
    text = font_type.render("Cache L2: 1024 KB", True, (87, 87, 87))
    display.blit(text, (50, 535))
    text = font_type.render("Cache L3: 8192 KB", True, (87, 87, 87))
    display.blit(text, (50, 570))
    text = font_type.render("Ratio Status: Unlocked (Min:09, Max:22)", True, (87, 87, 87))
    display.blit(text, (50, 605))
    text = font_type.render("Ratio Status: Unlocked (Min:09, Max:22)", True, (87, 87, 87))
    display.blit(text, (50, 605))
    text = font_type.render("Ratio Actual Value: 22", True, (87, 87, 87))
    display.blit(text, (50, 640))
    text = font_type.render("CPUID: 106E5", True, (87, 87, 87))
    display.blit(text, (50, 675))
    text_temperature = "CPU Temperature Control: " + str(random.randint(30, 32)) + str(" (C)")
    text = font_type.render(text_temperature, True, (87, 87, 87))
    display.blit(text, (50, 710))
    text_fan = "CPU Q-Fan Control: " + str(random.randint(800, 810)) + str(" (RPM)")
    text = font_type.render(text_fan, True, (87, 87, 87))
    display.blit(text, (50, 745))
    text = font_type.render("CPU Smart FAN Control: [Enabled]", True, (87, 87, 87))
    display.blit(text, (50, 780))
    text = font_type.render("CPU Smart FAN Mode: [PWM]", True, (87, 87, 87))
    display.blit(text, (50, 815))
    text = font_type.render("System Smart FAN Control: [Enabled]", True, (87, 87, 87))
    display.blit(text, (50, 850))
    text = font_type.render("Hello there, dude!", True, (87, 87, 87))
    display.blit(text, (50, 885))
    clock.tick(10)

def UPPER_MENU(class_gui=None):
    if class_gui == 1:
        const_gui()
        pygame.draw.rect(display, (204, 204, 204), (99, 50, 128, 60))  # для названия вкладки
        pygame.draw.rect(display, (0, 0, 168), (250, 50, 128, 50))  # для названия вкладки
        font_type = r"font\pixel_font.ttf"
        font_type = pygame.font.Font(font_type, 40)
        text_3 = font_type.render("Меню", True, (0, 0, 168))
        display.blit(text_3, (113, 50))
        text_4 = font_type.render("Игра", True, (204, 204, 204))
        display.blit(text_4, (250, 50))
        text_5 = font_type.render("Выход", True, (204, 204, 204))
        display.blit(text_5, (370, 50))
    if class_gui == 2:
        const_gui()
        pygame.draw.rect(display, (204, 204, 204), (230, 50, 120, 50))  # для названия вкладки
        pygame.draw.rect(display, (0, 0, 168), (99, 50, 128, 30))  # для названия вкладки
        font_type = r"font\pixel_font.ttf"
        font_type = pygame.font.Font(font_type, 40)
        text_3 = font_type.render("Меню", True, (204, 204, 204))
        display.blit(text_3, (113, 50))
        text_4 = font_type.render("Игра", True, (0, 0, 168))
        display.blit(text_4, (250, 50))
        text_5 = font_type.render("Выход", True, (204, 204, 204))
        display.blit(text_5, (370, 50))
    if class_gui == 3:
        const_gui()
        pygame.draw.rect(display, (204, 204, 204), (350, 50, 100, 50))  # для названия вкладки
        pygame.draw.rect(display, (0, 0, 168), (99, 50, 128, 30))  # для названия вкладки
        font_type = r"font\pixel_font.ttf"
        font_type = pygame.font.Font(font_type, 40)
        text_3 = font_type.render("Меню", True, (204, 204, 204))
        display.blit(text_3, (113, 50))
        text_4 = font_type.render("Игра", True, (204, 204, 204))
        display.blit(text_4, (250, 50))
        text_5 = font_type.render("КОД", True, (0, 0, 168))
        display.blit(text_5, (365, 50))
        text_6 = font_type.render("Обучение", True, (204, 204, 204))
        display.blit(text_6, (460, 50))
    if class_gui == 4:
        font_type = r"font\pixel_font.ttf"
        font_type = pygame.font.Font(font_type, 50)
        text = font_type.render("v.1.00 (C)Copyright 2020, 0bla4k0", True, (0, 0, 0))
        text_2 = font_type.render("if AI == true", True, (0, 0, 0))
        display.fill((51, 51, 51))
        pygame.draw.rect(display, (255, 255, 87), (0, 0, 1920, 100))  # вторая шапка сверху
        pygame.draw.rect(display, (255, 85, 85), (0, 0, 1920, 50))  # шапка для названия(первая)
        display.blit(text_2, (768, -5))
        pygame.draw.rect(display, (255, 85, 85), (0, 980, 1920, 100))  # нижняя шапка
        pygame.draw.rect(display, (255, 255, 87), (15, 120, 1890, 840), 4)  # рамка
        display.blit(text, (576, 1000))
        pygame.draw.rect(display, (51, 51, 51), (450, 50, 200, 50))  # для названия вкладки
        pygame.draw.rect(display, (255, 255, 87), (99, 50, 128, 30))  # для названия вкладки
        font_type = r"font\pixel_font.ttf"
        font_type = pygame.font.Font(font_type, 40)
        text_3 = font_type.render("Меню", True, (51, 51, 51))
        display.blit(text_3, (113, 50))
        text_4 = font_type.render("Игра", True, (51, 51, 51))
        display.blit(text_4, (250, 50))
        text_5 = font_type.render("КОД", True, (51, 51, 51))
        display.blit(text_5, (365, 50))
        text_6 = font_type.render("Обучение", True, (255, 255, 87))
        display.blit(text_6, (460, 50))
    if class_gui == 5:
        const_gui()
        pygame.draw.rect(display, (204, 204, 204), (350, 50, 100, 50))  # для названия вкладки
        pygame.draw.rect(display, (0, 0, 168), (99, 50, 128, 30))  # для названия вкладки
        font_type = r"font\pixel_font.ttf"
        font_type = pygame.font.Font(font_type, 40)
        text_3 = font_type.render("Меню", True, (204, 204, 204))
        display.blit(text_3, (113, 50))
        text_4 = font_type.render("Игра", True, (204, 204, 204))
        display.blit(text_4, (250, 50))
        text_5 = font_type.render("КОД", True, (0, 0, 168))
        display.blit(text_5, (365, 50))


def const_gui():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 50)
    text = font_type.render("v.1.00 (C)Copyright 2020, 0bla4k0", True, (0, 0, 0))
    text_2 = font_type.render("if AI == true", True, (0, 0, 0))
    display.fill((204, 204, 204))
    pygame.draw.rect(display, (0, 0, 168), (0, 0, 1920, 100))  # вторая шапка сверху
    pygame.draw.rect(display, (0, 170, 170), (0, 0, 1920, 50))  # шапка для названия(первая)
    display.blit(text_2, (768, -5))
    pygame.draw.rect(display, (0, 170, 170), (0, 980, 1920, 100))  # нижняя шапка
    pygame.draw.rect(display, (24, 24, 162), (15, 120, 1890, 840), 4)  # рамка
    display.blit(text, (576, 1000))


def start_game():
    game_loop()


def game_loop():
    game = True
    level_button = Button(292, 350)
    lvl_button = Button(940, 350)
    control_button = Button(200, 70)
    pygame.time.delay(300)
    while game:
        print(pygame.mouse.get_pos())
        UPPER_MENU(2)
        pygame.draw.line(display, (24, 24, 162), [1080, 120], [1080, 960], 4)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 99 < mouse[0] < 227 and 50 < mouse[1] < 100 and click[0] == 1:
            click_mouse.play()
            menu_game()
        if 370 < mouse[0] < 500 and 50 < mouse[1] < 100 and click[0] == 1:
            pygame.quit()
            quit()
        if keys[pygame.K_ESCAPE]:
            click_mouse.play()
            menu_game()
        const_text()
        level_button.draw_button(46, 152, "", first_main_level, 2, icon_first_level, first_level, pic_level1)
        level_button.draw_button(370, 152, "", None, 2, icon_second_level, second_level, pic_level2)
        level_button.draw_button(694, 152, "", second_main_level, 2, icon_third_level, third_level, pic_level3)
        level_button.draw_button(46, 530, "", None, 2, icon_fourth_level, fourth_level, pic_level4)
        level_button.draw_button(370, 530, "", None, 2, icon_fifth_level, fifth_level, pic_level5)
        level_button.draw_button(694, 530, "", None, 2, icon_sixth_level, sixth_level, pic_level6)
        control_button.draw_button(46, 885, "В МЕНЮ", menu_game, 1)
        pygame.display.update()
        clock.tick(60)


def first_main_level():
    touch_InputBlock = False
    touch_StudyBlock = False
    touch_OutputBlock1 = False
    touch_OutputBlock2 = False
    touch_EaysBlock1 = False
    line_InputBlock = False
    line_StudyBlock1 = False
    line_StudyBlock2 = False
    x, y = 1600, 700
    x1, y1 = 1295, 635
    x2, y2 = 1600, 400
    x3, y3 = 1600, 550
    x4, y4 = 1470, 590
    line_x, line_y = x + 53, y + 29
    line_x_1, line_y_1 = x1 + 53, y1 + 12
    line_x_2, line_y_2 = x1 + 53, y1 + 47
    var_InputBlock = 0
    var_StudyBlock1 = 0
    var_StudyBlock2 = 0
    var_levelBlock = 0
    control_button = Button(510, 75)

    def game(x, y, x1, y1, x2, y2, x3, y3, x4, y4, line_x, line_y, line_x_1, line_y_1, line_x_2, line_y_2, var_InputBlock,
             var_StudyBlock1, var_StudyBlock2, var_levelBlock, touch_InputBlock, touch_StudyBlock, touch_OutputBlock1, touch_OutputBlock2,
             touch_EaysBlock1, line_InputBlock, line_StudyBlock1, line_StudyBlock2):
        level_1 = True
        global l
        l = 0
        while level_1:
            def study_game():
                global l
                game = True
                k = 0
                x = random.randint(20, 1800)
                y = random.randint(200, 800)
                img = random.choice(Eyes)
                img_index = Eyes.index(img)
                UPPER_MENU(4)
                start_ticks = pygame.time.get_ticks()
                while game:
                    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    if img_index == 0:
                        if mouse[0] > x and mouse[0] < x + 70 and mouse[1] > y and mouse[1] < y + 58 and click[0] == 1:
                            x = random.randint(20, 1800)
                            y = random.randint(200, 800)
                            img = random.choice(Eyes)
                            img_index = Eyes.index(img)
                            k += 1
                        if mouse[0] > x and mouse[0] < x + 70 and mouse[1] > y and mouse[1] < y + 58 and click[2] == 1:
                            x = random.randint(20, 1800)
                            y = random.randint(200, 800)
                            img = random.choice(Eyes)
                            img_index = Eyes.index(img)
                            k -= 1
                    else:
                        if mouse[0] > x and mouse[0] < x + 70 and mouse[1] > y and mouse[1] < y + 58 and click[2] == 1:
                            x = random.randint(20, 1800)
                            y = random.randint(200, 800)
                            img = random.choice(Eyes)
                            img_index = Eyes.index(img)
                            k += 1
                        if mouse[0] > x and mouse[0] < x + 70 and mouse[1] > y and mouse[1] < y + 58 and click[0] == 1:
                            x = random.randint(20, 1800)
                            y = random.randint(200, 800)
                            img = random.choice(Eyes)
                            img_index = Eyes.index(img)
                            k -= 1
                    UPPER_MENU(4)
                    display.blit(img, (x, y))
                    if round((10 - seconds), 0) == 0:
                        if k > 10:
                            l = 1
                        else:
                            l = 0
                        break
                    if k <= 10:
                        print_text('{0}'.format(k), 1152, 142, (0, 0, 0), 50)
                        print_text('{0}'.format(k), 1150, 140, (228,22,42), 50)
                    elif k > 10:
                        print_text('{0}'.format(k), 1152, 142, (0, 0, 0), 50)
                        print_text('{0}'.format(k), 1150, 140, (19, 150, 37), 50)
                    print_text('Количетсво очков: ', 652, 142, (0, 0, 0), 50)
                    print_text("Количетсво очков: ", 650, 140, (255, 255, 255), 50)
                    print_text('Времени осталось: ', 660, 892, (0, 0, 0), 50)
                    print_text("Времени осталось: ", 658, 890, (255, 255, 255), 50)
                    print_text('{0}'.format(round((10 - seconds), 1)), 1162, 892, (0, 0, 0), 50)
                    print_text('{0}'.format(round((10 - seconds), 1)), 1160, 890, (87, 130, 255), 50)
                    print(mouse)
                    pygame.display.update()
                    clock.tick(60)

            def study_first_level():
                game = True
                button = Button(405, 80)
                while game:
                    print(pygame.mouse.get_pos())
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    UPPER_MENU(4)
                    print_text("Обучите искуссвтвенный интеллект определять здоровые глаза.", 180, 300, (255, 255, 255))
                    print_text("У вас будет 15 секунд, вам нужно набрать больше 10 баллов.", 200, 350, (255, 255, 255))
                    print_text("Нажимайте ЛКМ, когда увидите здоровый глаз: ", 210, 500, (204, 204, 204))
                    display.blit(Eyes[0], (1568, 500))
                    display.blit(Eyes[2], (1568, 600))
                    print_text("Нажимайте ПКМ, когда увидите не здоровый глаз: ", 210, 600, (204, 204, 204))
                    button.draw_button(752, 680, "Начать обучение", study_game, 3)
                    if l == 0:
                        print_text("Не пройдено.", 810, 890, (231, 31, 31))
                    else:
                        print_text("Вернитесь к коду.", 752, 780, (255, 255, 255))
                        print_text("Пройдено.", 830, 890, (68, 162, 30))
                    if 99 < mouse[0] < 227 and 50 < mouse[1] < 100 and click[0] == 1:
                        click_mouse.play()
                        menu_game()
                    if 240 < mouse[0] < 340 and 50 < mouse[1] < 100 and click[0] == 1:
                        click_mouse.play()
                        game_loop()
                    if 351 < mouse[0] < 445 and 50 < mouse[1] < 100 and click[0] == 1:
                        click_mouse.play()
                        break
                    pygame.display.update()
                    clock.tick(60)

            keys = pygame.key.get_pressed()
            print(pygame.mouse.get_pos())
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            UPPER_MENU(3)
            pygame.draw.line(display, (0, 0, 168), [x + 234, y + 76], [line_x, line_y],
                             10)  # LINE FROM INPUT BLOCK TO SECOND
            pygame.draw.line(display, (0, 0, 168), [x1 + 256, y1 + 80], [line_x_1, line_y_1],
                             10)  # LINE FROM INPUT BLOCK TO SECOND
            pygame.draw.line(display, (0, 0, 168), [x1 + 255, y1 + 165], [line_x_2, line_y_2],
                             10)  # LINE FROM INPUT BLOCK TO SECOND
            pygame.draw.line(display, (24, 24, 162), [1250, 120], [1250, 960], 4)
            pygame.draw.line(display, (24, 24, 162), [1250, 358], [1905, 358], 4)
            pygame.draw.line(display, (24, 24, 162), [1250, 856], [1905, 856], 4)
            print_text("#Задача:", 1265, 130, (87, 87, 87), 50)
            if var_levelBlock + var_InputBlock + var_StudyBlock2 + var_StudyBlock1 == 7:
                print_text("1) Собрать программу, где сначала", 1265, 185, (24, 121, 29), 30)
                print_text("идет входной блок, обучающий, а", 1265, 215, (24, 121, 29), 30)
                print_text("затем здоровый глаз идет на 1 вых.", 1265, 245, (24, 121, 29), 30)
            else:
                print_text("1) Собрать программу, где сначала", 1265, 185, (170, 55, 55), 30)
                print_text("идет входной блок, обучающий, а", 1265, 215, (170, 55, 55), 30)
                print_text("затем здоровый глаз идет на 1 вых.", 1265, 245, (170, 55, 55), 30)
            if l == 1:
                print_text("2) Обучить ИИ.", 1265, 275, (24, 121, 29), 30)
            else:
                print_text("2) Обучить ИИ.", 1265, 275, (170, 55, 55), 30)
            print_text("3) Проверить систему.", 1265, 305, (87, 87, 87), 30)
            control_button.draw_button(1320, 870, "Запустить нейросеть", None, 4)
            display.blit(OutputBlock1, (x2, y2))
            display.blit(OutputBlock2, (x3, y3))
            display.blit(InputBlock, (x, y))
            display.blit(StudyBlock, (x1, y1))
            display.blit(EaysBlock1, (x4, y4))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x < event.pos[0] < x + 217 and y < event.pos[1] < y + 125:
                        touch_InputBlock = True
                    if x1 < event.pos[0] < x1 + 237 and y1 < event.pos[1] < y1 + 191:
                        touch_StudyBlock = True
                    if x2 < event.pos[0] < x2 + 250 and y2 < event.pos[1] < y2 + 125:
                        touch_OutputBlock1 = True
                    if x3 < event.pos[0] < x3 + 250 and y3 < event.pos[1] < y3 + 125:
                        touch_OutputBlock2 = True
                    if x4 < event.pos[0] < x4 + 97 and y4 < event.pos[1] < y4 + 35:
                        touch_EaysBlock1 = True
                    if x + 217 < event.pos[0] < x + 250 and y + 25 < event.pos[1] < y + 125:
                        line_InputBlock = True
                    if x1 + 237 < event.pos[0] < x1 + 273 and y1 <= event.pos[1] <= y1 + 116:
                        line_StudyBlock1 = True
                    if x1 + 237 < event.pos[0] < x1 + 273 and y1 + 120 < event.pos[1] < y1 + 196:
                        line_StudyBlock2 = True
                if event.type == pygame.MOUSEBUTTONUP:  # ЕСЛИ БЛОК НЕ УДЕРЖИВАЕТСЯ, ТО СБРОС
                    touch_InputBlock = False
                    touch_StudyBlock = False
                    touch_OutputBlock1 = False
                    touch_OutputBlock2 = False
                    touch_EaysBlock1 = False
                    line_InputBlock = False
                    line_StudyBlock1 = False
                    line_StudyBlock2 = False
                    if var_InputBlock == 0:  # ЕСЛИ ЛИНИЯ НЕ ЗАЦЕИЛАСЬ, ТО СБРОС ДО ИСХОДНОГО СОСТОЯНИЯ
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62

                if event.type == pygame.MOUSEMOTION and line_InputBlock == True:
                    line_x, line_y = event.pos[0], event.pos[1]
                    if x1 <= line_x <= x1 + 42 and y1 <= line_y <= y1 + 189:
                        line_x, line_y = x1 + 19, y1 + 122
                        var_InputBlock = 1
                    else:
                        var_InputBlock = 0

                if event.type == pygame.MOUSEMOTION and line_StudyBlock1 == True:
                    line_x_1, line_y_1 = event.pos[0], event.pos[1]
                    if x2 <= line_x_1 <= x2 + 33 and y2 <= line_y_1 <= y2 + 124:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                        var_StudyBlock1 = 3
                    elif x3 <= line_x_1 <= x3 + 33 and y3 <= line_y_1 <= y3 + 124:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                        var_StudyBlock1 = 2
                    else:
                        var_StudyBlock1 = 0

                if event.type == pygame.MOUSEMOTION and line_StudyBlock2 == True:
                    line_x_2, line_y_2 = event.pos[0], event.pos[1]
                    if x2 <= line_x_2 <= x2 + 33 and y2 <= line_y_2 <= y2 + 124:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                        var_StudyBlock2 = 1
                    elif x3 <= line_x_2 <= x3 + 33 and y3 <= line_y_2 <= y3 + 124:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                        var_StudyBlock2 = 2
                    else:
                        var_StudyBlock2 = 0

                if event.type == pygame.MOUSEMOTION and touch_EaysBlock1 == True:
                    x4, y4 = event.pos[0] - 45, event.pos[1] - 17
                    if x1 <= event.pos[0] <= x1 + 273 and y1 <= event.pos[1] <= y1 + 191:
                        x4, y4 = x1 + 132, y1 + 62
                        var_levelBlock = 1
                    else:
                        var_levelBlock = 0
                if event.type == pygame.MOUSEMOTION and touch_InputBlock == True:
                    x, y = event.pos[0] - 125, event.pos[1] - 60
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62
                    if var_levelBlock == 0:
                        pass
                    if var_InputBlock == 1:
                        line_x, line_y = x1 + 19, y1 + 122
                    if var_InputBlock == 0:
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 3:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                    if var_StudyBlock1 == 2:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                    if var_StudyBlock2 == 1:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                    if var_StudyBlock2 == 2:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                if event.type == pygame.MOUSEMOTION and touch_StudyBlock == True:
                    x1, y1 = event.pos[0] - 130, event.pos[1] - 85
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62
                    if var_levelBlock == 0:
                        pass
                    if var_InputBlock == 1:
                        line_x, line_y = x1 + 19, y1 + 122
                    if var_InputBlock == 0:
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 3:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                    if var_StudyBlock1 == 2:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                    if var_StudyBlock2 == 1:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                    if var_StudyBlock2 == 2:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                if event.type == pygame.MOUSEMOTION and touch_OutputBlock1 == True:
                    x2, y2 = event.pos[0] - 125, event.pos[1] - 60
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62
                    if var_levelBlock == 0:
                        pass
                    if var_InputBlock == 1:
                        line_x, line_y = x1 + 19, y1 + 122
                    if var_InputBlock == 0:
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 3:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                    if var_StudyBlock1 == 2:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                    if var_StudyBlock2 == 1:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                    if var_StudyBlock2 == 2:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                if event.type == pygame.MOUSEMOTION and touch_OutputBlock2 == True:
                    x3, y3 = event.pos[0] - 125, event.pos[1] - 60
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62
                    if var_levelBlock == 0:
                        pass
                    if var_InputBlock == 1:
                        line_x, line_y = x1 + 19, y1 + 122
                    if var_InputBlock == 0:
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 3:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                    if var_StudyBlock1 == 2:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                    if var_StudyBlock2 == 1:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                    if var_StudyBlock2 == 2:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if 99 < mouse[0] < 227 and 50 < mouse[1] < 100 and click[0] == 1:
                click_mouse.play()
                menu_game()
            if 240 < mouse[0] < 340 and 50 < mouse[1] < 100 and click[0] == 1:
                click_mouse.play()
                game_loop()
            if 454 < mouse[0] < 651 and 50 < mouse[1] < 100 and click[0] == 1:
                click_mouse.play()
                study_first_level()
            print(var_levelBlock + var_InputBlock + var_StudyBlock2 + var_StudyBlock1)
            pygame.display.update()
            clock.tick(60)

    game(x, y, x1, y1, x2, y2, x3, y3, x4, y4, line_x, line_y, line_x_1, line_y_1, line_x_2, line_y_2, var_InputBlock,
             var_StudyBlock1, var_StudyBlock2, var_levelBlock, touch_InputBlock, touch_StudyBlock, touch_OutputBlock1, touch_OutputBlock2,
             touch_EaysBlock1, line_InputBlock, line_StudyBlock1, line_StudyBlock2)
    pygame.display.update()
    clock.tick(60)

def second_main_level():
    touch_InputBlock = False
    touch_StudyBlock = False
    touch_OutputBlock1 = False
    touch_OutputBlock2 = False
    touch_EaysBlock1 = False
    line_InputBlock = False
    line_StudyBlock1 = False
    line_StudyBlock2 = False
    x, y = 1600, 700
    x1, y1 = 1295, 635
    x2, y2 = 1600, 400
    x3, y3 = 1600, 550
    x4, y4 = 1470, 590
    line_x, line_y = x + 53, y + 29
    line_x_1, line_y_1 = x1 + 53, y1 + 12
    line_x_2, line_y_2 = x1 + 53, y1 + 47
    var_InputBlock = 0
    var_StudyBlock1 = 0
    var_StudyBlock2 = 0
    var_levelBlock = 0
    control_button = Button(510, 75)

    def game(x, y, x1, y1, x2, y2, x3, y3, x4, y4, line_x, line_y, line_x_1, line_y_1, line_x_2, line_y_2, var_InputBlock,
             var_StudyBlock1, var_StudyBlock2, var_levelBlock, touch_InputBlock, touch_StudyBlock, touch_OutputBlock1, touch_OutputBlock2,
             touch_EaysBlock1, line_InputBlock, line_StudyBlock1, line_StudyBlock2):
        level_1 = True
        global l
        l = 0
        while level_1:
            def study_game():
                global l
                game = True
                k = 0
                x = random.randint(20, 1800)
                y = random.randint(200, 800)
                img = random.choice(Eyes)
                img_index = Eyes.index(img)
                UPPER_MENU(4)
                start_ticks = pygame.time.get_ticks()
                while game:
                    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    if img_index == 0:
                        if mouse[0] > x and mouse[0] < x + 70 and mouse[1] > y and mouse[1] < y + 58 and click[0] == 1:
                            x = random.randint(20, 1800)
                            y = random.randint(200, 800)
                            img = random.choice(Eyes)
                            img_index = Eyes.index(img)
                            k += 1
                        if mouse[0] > x and mouse[0] < x + 70 and mouse[1] > y and mouse[1] < y + 58 and click[2] == 1:
                            x = random.randint(20, 1800)
                            y = random.randint(200, 800)
                            img = random.choice(Eyes)
                            img_index = Eyes.index(img)
                            k -= 1
                    else:
                        if mouse[0] > x and mouse[0] < x + 70 and mouse[1] > y and mouse[1] < y + 58 and click[2] == 1:
                            x = random.randint(20, 1800)
                            y = random.randint(200, 800)
                            img = random.choice(Eyes)
                            img_index = Eyes.index(img)
                            k += 1
                        if mouse[0] > x and mouse[0] < x + 70 and mouse[1] > y and mouse[1] < y + 58 and click[0] == 1:
                            x = random.randint(20, 1800)
                            y = random.randint(200, 800)
                            img = random.choice(Eyes)
                            img_index = Eyes.index(img)
                            k -= 1
                    UPPER_MENU(4)
                    display.blit(img, (x, y))
                    if round((10 - seconds), 0) == 0:
                        if k > 10:
                            l = 1
                        else:
                            l = 0
                        break
                    if k <= 10:
                        print_text('{0}'.format(k), 1152, 142, (0, 0, 0), 50)
                        print_text('{0}'.format(k), 1150, 140, (228,22,42), 50)
                    elif k > 10:
                        print_text('{0}'.format(k), 1152, 142, (0, 0, 0), 50)
                        print_text('{0}'.format(k), 1150, 140, (19, 150, 37), 50)
                    print_text('Количетсво очков: ', 652, 142, (0, 0, 0), 50)
                    print_text("Количетсво очков: ", 650, 140, (255, 255, 255), 50)
                    print_text('Времени осталось: ', 660, 892, (0, 0, 0), 50)
                    print_text("Времени осталось: ", 658, 890, (255, 255, 255), 50)
                    print_text('{0}'.format(round((10 - seconds), 1)), 1162, 892, (0, 0, 0), 50)
                    print_text('{0}'.format(round((10 - seconds), 1)), 1160, 890, (87, 130, 255), 50)
                    print(mouse)
                    pygame.display.update()
                    clock.tick(60)

            def study_first_level():
                game = True
                button = Button(405, 80)
                while game:
                    print(pygame.mouse.get_pos())
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    UPPER_MENU(4)
                    print_text("Обучите искуссвтвенный интеллект определять здоровые глаза.", 180, 300, (255, 255, 255))
                    print_text("У вас будет 15 секунд, вам нужно набрать больше 10 баллов.", 200, 350, (255, 255, 255))
                    print_text("Нажимайте ЛКМ, когда увидите здоровый глаз: ", 210, 500, (204, 204, 204))
                    display.blit(Eyes[0], (1568, 500))
                    display.blit(Eyes[2], (1568, 600))
                    print_text("Нажимайте ПКМ, когда увидите не здоровый глаз: ", 210, 600, (204, 204, 204))
                    button.draw_button(752, 680, "Начать обучение", study_game, 3)
                    if l == 0:
                        print_text("Не пройдено.", 810, 890, (231, 31, 31))
                    else:
                        print_text("Вернитесь к коду.", 752, 780, (255, 255, 255))
                        print_text("Пройдено.", 830, 890, (68, 162, 30))
                    if 99 < mouse[0] < 227 and 50 < mouse[1] < 100 and click[0] == 1:
                        click_mouse.play()
                        menu_game()
                    if 240 < mouse[0] < 340 and 50 < mouse[1] < 100 and click[0] == 1:
                        click_mouse.play()
                        game_loop()
                    if 351 < mouse[0] < 445 and 50 < mouse[1] < 100 and click[0] == 1:
                        click_mouse.play()
                        break
                    pygame.display.update()
                    clock.tick(60)

            keys = pygame.key.get_pressed()
            print(pygame.mouse.get_pos())
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            UPPER_MENU(3)
            pygame.draw.line(display, (0, 0, 168), [x + 234, y + 76], [line_x, line_y],
                             10)  # LINE FROM INPUT BLOCK TO SECOND
            pygame.draw.line(display, (0, 0, 168), [x1 + 256, y1 + 80], [line_x_1, line_y_1],
                             10)  # LINE FROM INPUT BLOCK TO SECOND
            pygame.draw.line(display, (0, 0, 168), [x1 + 255, y1 + 165], [line_x_2, line_y_2],
                             10)  # LINE FROM INPUT BLOCK TO SECOND
            pygame.draw.line(display, (24, 24, 162), [1250, 120], [1250, 960], 4)
            pygame.draw.line(display, (24, 24, 162), [1250, 358], [1905, 358], 4)
            pygame.draw.line(display, (24, 24, 162), [1250, 856], [1905, 856], 4)
            print_text("#Задача:", 1265, 130, (87, 87, 87), 50)
            if var_levelBlock + var_InputBlock + var_StudyBlock2 + var_StudyBlock1 == 7:
                print_text("1) Собрать программу, где сначала", 1265, 185, (24, 121, 29), 30)
                print_text("идет входной блок, обучающий, а", 1265, 215, (24, 121, 29), 30)
                print_text("затем здоровый глаз идет на 1 вых.", 1265, 245, (24, 121, 29), 30)
            else:
                print_text("1) Собрать программу, где сначала", 1265, 185, (170, 55, 55), 30)
                print_text("идет входной блок, обучающий, а", 1265, 215, (170, 55, 55), 30)
                print_text("затем здоровый глаз идет на 1 вых.", 1265, 245, (170, 55, 55), 30)
            if l == 1:
                print_text("2) Обучить ИИ.", 1265, 275, (24, 121, 29), 30)
            else:
                print_text("2) Обучить ИИ.", 1265, 275, (170, 55, 55), 30)
            print_text("3) Проверить систему.", 1265, 305, (87, 87, 87), 30)
            control_button.draw_button(1320, 870, "Запустить нейросеть", None, 4)
            display.blit(OutputBlock1, (x2, y2))
            display.blit(OutputBlock2, (x3, y3))
            display.blit(InputBlock, (x, y))
            display.blit(StudyBlock, (x1, y1))
            display.blit(EaysBlock1, (x4, y4))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x < event.pos[0] < x + 217 and y < event.pos[1] < y + 125:
                        touch_InputBlock = True
                    if x1 < event.pos[0] < x1 + 237 and y1 < event.pos[1] < y1 + 191:
                        touch_StudyBlock = True
                    if x2 < event.pos[0] < x2 + 250 and y2 < event.pos[1] < y2 + 125:
                        touch_OutputBlock1 = True
                    if x3 < event.pos[0] < x3 + 250 and y3 < event.pos[1] < y3 + 125:
                        touch_OutputBlock2 = True
                    if x4 < event.pos[0] < x4 + 97 and y4 < event.pos[1] < y4 + 35:
                        touch_EaysBlock1 = True
                    if x + 217 < event.pos[0] < x + 250 and y + 25 < event.pos[1] < y + 125:
                        line_InputBlock = True
                    if x1 + 237 < event.pos[0] < x1 + 273 and y1 <= event.pos[1] <= y1 + 116:
                        line_StudyBlock1 = True
                    if x1 + 237 < event.pos[0] < x1 + 273 and y1 + 120 < event.pos[1] < y1 + 196:
                        line_StudyBlock2 = True
                if event.type == pygame.MOUSEBUTTONUP:  # ЕСЛИ БЛОК НЕ УДЕРЖИВАЕТСЯ, ТО СБРОС
                    touch_InputBlock = False
                    touch_StudyBlock = False
                    touch_OutputBlock1 = False
                    touch_OutputBlock2 = False
                    touch_EaysBlock1 = False
                    line_InputBlock = False
                    line_StudyBlock1 = False
                    line_StudyBlock2 = False
                    if var_InputBlock == 0:  # ЕСЛИ ЛИНИЯ НЕ ЗАЦЕИЛАСЬ, ТО СБРОС ДО ИСХОДНОГО СОСТОЯНИЯ
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62

                if event.type == pygame.MOUSEMOTION and line_InputBlock == True:
                    line_x, line_y = event.pos[0], event.pos[1]
                    if x1 <= line_x <= x1 + 42 and y1 <= line_y <= y1 + 189:
                        line_x, line_y = x1 + 19, y1 + 122
                        var_InputBlock = 1
                    else:
                        var_InputBlock = 0

                if event.type == pygame.MOUSEMOTION and line_StudyBlock1 == True:
                    line_x_1, line_y_1 = event.pos[0], event.pos[1]
                    if x2 <= line_x_1 <= x2 + 33 and y2 <= line_y_1 <= y2 + 124:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                        var_StudyBlock1 = 3
                    elif x3 <= line_x_1 <= x3 + 33 and y3 <= line_y_1 <= y3 + 124:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                        var_StudyBlock1 = 2
                    else:
                        var_StudyBlock1 = 0

                if event.type == pygame.MOUSEMOTION and line_StudyBlock2 == True:
                    line_x_2, line_y_2 = event.pos[0], event.pos[1]
                    if x2 <= line_x_2 <= x2 + 33 and y2 <= line_y_2 <= y2 + 124:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                        var_StudyBlock2 = 1
                    elif x3 <= line_x_2 <= x3 + 33 and y3 <= line_y_2 <= y3 + 124:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                        var_StudyBlock2 = 2
                    else:
                        var_StudyBlock2 = 0

                if event.type == pygame.MOUSEMOTION and touch_EaysBlock1 == True:
                    x4, y4 = event.pos[0] - 45, event.pos[1] - 17
                    if x1 <= event.pos[0] <= x1 + 273 and y1 <= event.pos[1] <= y1 + 191:
                        x4, y4 = x1 + 132, y1 + 62
                        var_levelBlock = 1
                    else:
                        var_levelBlock = 0
                if event.type == pygame.MOUSEMOTION and touch_InputBlock == True:
                    x, y = event.pos[0] - 125, event.pos[1] - 60
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62
                    if var_levelBlock == 0:
                        pass
                    if var_InputBlock == 1:
                        line_x, line_y = x1 + 19, y1 + 122
                    if var_InputBlock == 0:
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 3:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                    if var_StudyBlock1 == 2:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                    if var_StudyBlock2 == 1:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                    if var_StudyBlock2 == 2:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                if event.type == pygame.MOUSEMOTION and touch_StudyBlock == True:
                    x1, y1 = event.pos[0] - 130, event.pos[1] - 85
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62
                    if var_levelBlock == 0:
                        pass
                    if var_InputBlock == 1:
                        line_x, line_y = x1 + 19, y1 + 122
                    if var_InputBlock == 0:
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 3:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                    if var_StudyBlock1 == 2:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                    if var_StudyBlock2 == 1:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                    if var_StudyBlock2 == 2:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                if event.type == pygame.MOUSEMOTION and touch_OutputBlock1 == True:
                    x2, y2 = event.pos[0] - 125, event.pos[1] - 60
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62
                    if var_levelBlock == 0:
                        pass
                    if var_InputBlock == 1:
                        line_x, line_y = x1 + 19, y1 + 122
                    if var_InputBlock == 0:
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 3:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                    if var_StudyBlock1 == 2:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                    if var_StudyBlock2 == 1:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                    if var_StudyBlock2 == 2:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                if event.type == pygame.MOUSEMOTION and touch_OutputBlock2 == True:
                    x3, y3 = event.pos[0] - 125, event.pos[1] - 60
                    if var_levelBlock == 1:
                        x4, y4 = x1 + 132, y1 + 62
                    if var_levelBlock == 0:
                        pass
                    if var_InputBlock == 1:
                        line_x, line_y = x1 + 19, y1 + 122
                    if var_InputBlock == 0:
                        line_x, line_y = x + 234, y + 76
                    if var_StudyBlock1 == 3:
                        line_x_1, line_y_1 = x2 + 17, y2 + 78
                    if var_StudyBlock1 == 2:
                        line_x_1, line_y_1 = x3 + 17, y3 + 78
                    if var_StudyBlock2 == 1:
                        line_x_2, line_y_2 = x2 + 17, y2 + 78
                    if var_StudyBlock2 == 2:
                        line_x_2, line_y_2 = x3 + 17, y3 + 78
                    if var_StudyBlock1 == 0:
                        line_x_1, line_y_1 = x1 + 256, y1 + 80
                    if var_StudyBlock2 == 0:
                        line_x_2, line_y_2 = x1 + 255, y1 + 165
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if 99 < mouse[0] < 227 and 50 < mouse[1] < 100 and click[0] == 1:
                click_mouse.play()
                menu_game()
            if 240 < mouse[0] < 340 and 50 < mouse[1] < 100 and click[0] == 1:
                click_mouse.play()
                game_loop()
            if 454 < mouse[0] < 651 and 50 < mouse[1] < 100 and click[0] == 1:
                click_mouse.play()
                study_first_level()
            print(var_levelBlock + var_InputBlock + var_StudyBlock2 + var_StudyBlock1)
            pygame.display.update()
            clock.tick(60)

    game(x, y, x1, y1, x2, y2, x3, y3, x4, y4, line_x, line_y, line_x_1, line_y_1, line_x_2, line_y_2, var_InputBlock,
             var_StudyBlock1, var_StudyBlock2, var_levelBlock, touch_InputBlock, touch_StudyBlock, touch_OutputBlock1, touch_OutputBlock2,
             touch_EaysBlock1, line_InputBlock, line_StudyBlock1, line_StudyBlock2)
    pygame.display.update()
    clock.tick(60)


def print_text(message, x, y, font_colour, font_size=45):
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    display.blit(text, (x, y))


def decoration_for_start():
    font_type = r"font\pixel_font.ttf"
    font_type = pygame.font.Font(font_type, 140)
    text = font_type.render("IF (AI == TRUE) {}", True, (240, 240, 240))
    display.blit(text, (360, 300))
    text = font_type.render("|", True, (240, 240, 240))
    display.blit(text, (1635, 290))
    pygame.draw.rect(display, (51, 51, 51), (1635, 290, 30, 60))
    text = font_type.render("|", True, (240, 240, 240))
    display.blit(text, (1635, 290))
    pygame.draw.rect(display, (51, 51, 51), (1635, 290, 30, 60))


def start_button_game():
    game = True
    button = Button(255, 80)
    while game:
        print(pygame.mouse.get_pos())
        display.fill((51, 51, 51))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        decoration_for_start()
        button.draw_button(830, 530, "Запустить", menu_game, 3)
        button.draw_button(830, 630, " Выйти", quit, 3)
        pygame.display.update()
        clock.tick(60)

start_button_game()

pygame.quit()
quit()
