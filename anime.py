import sys
import pygame

pygame.init()

# берем инфу об экране
screen_info = pygame.display.Info()
screen_width = screen_info.current_w # 1792
screen_height = screen_info.current_h # 1120

# окно с размером экрана
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# цвета
white = (255, 255, 255)
grey = (128, 128, 128)
silver = (192, 192, 192)


# 1 деталь (малый прямоугольник) корпуса
first_frame_x = screen_width / 2 - screen_width / 16
first_frame_y = 0
first_frame_width = screen_width / 8
first_frame_height = screen_height / 15
first_frame_color = grey

# 2 деталь (верхний элипс) корпуса
second_frame_points = (first_frame_x - first_frame_width * 2,
                       first_frame_height - 0.01 * screen_height,
                       first_frame_width * 5,
                       first_frame_height * 5)
second_frame_color = grey

# 3 деталь (нижний элипс) корпуса
third_frame_points = (first_frame_x - first_frame_width * 2,
                       screen_height - first_frame_height * 5,
                       first_frame_width * 5,
                       first_frame_height * 5)
third_frame_color = grey

# 4 деталь (большой прямоугольник) корпуса
fourth_frame_x = first_frame_x - first_frame_width * 2
fourth_frame_y = (first_frame_height - 0.01 * screen_height) + first_frame_height * 2.5
fourth_frame_width = first_frame_width * 5
fourth_frame_height = (screen_height - first_frame_height * 5) - (first_frame_height - 0.01 * screen_height)
fourth_frame_color = grey



# 1 деталь (верхний элипс) полости
first_cavity_points = (first_frame_x - first_frame_width * 1.5,
                       first_frame_height * 2,
                       first_frame_width * 5 / 1.25,
                       first_frame_height * 5 / 1.25)
first_cavity_color = silver

# 2 деталь (нижний элипс) полости
second_cavity_points = (first_frame_x - first_frame_width * 1.5,
                       screen_height - (first_frame_height + first_frame_height * 5 / 1.25),
                       first_frame_width * 5 / 1.25,
                       first_frame_height * 5 / 1.25)
second_cavity_color = silver

# 3 деталь (прямоугольник) полости
third_cavity_x = first_frame_x - first_frame_width * 1.5
third_cavity_y = first_frame_height * 2 + first_frame_height * 2.5 / 1.25
third_cavity_width = first_frame_width * 5 / 1.25
third_cavity_height = screen_height - (first_frame_height + first_frame_height * 5 / 1.25) - first_frame_height * 2
third_cavity_color = silver





# Основной аниме цикл
running = True
while running:

    # Заливка экрана цветов
    screen.fill(white)

    # пробел - закрыть
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = False







    # 1 деталь (малый прямоугольник) корпуса
    pygame.draw.rect(screen, first_frame_color, (first_frame_x, first_frame_y, first_frame_width, first_frame_height))

    # 2 деталь (верхний элипс) корпуса
    pygame.draw.ellipse(screen, second_frame_color, second_frame_points)

    # 3 деталь (нижний элипс) корпуса
    pygame.draw.ellipse(screen, third_frame_color, third_frame_points)

    # 4 деталь (большой прямоугольник) корпуса
    pygame.draw.rect(screen, third_frame_color, (fourth_frame_x, fourth_frame_y, fourth_frame_width, fourth_frame_height))



    # 1 деталь (верхний элипс) корпуса
    pygame.draw.ellipse(screen, first_cavity_color, first_cavity_points)

    # 2 деталь (нижний элипс) корпуса
    pygame.draw.ellipse(screen, second_cavity_color, second_cavity_points)

    # 3 деталь (прямоугольник) полости
    pygame.draw.rect(screen, third_cavity_color, (third_cavity_x, third_cavity_y, third_cavity_width, third_cavity_height))

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
