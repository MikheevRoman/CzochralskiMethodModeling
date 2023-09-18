import sys
import pygame




def playing_animation(w_t, w_kr):
    pygame.init()

    pygame.display.set_caption("Графическое представление")

    # берем инфу об экране
    screen_width = 1000
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    # цвета
    white = (255, 255, 255)
    light_grey = (144, 144, 144)
    grey = (128, 128, 128)
    silver = (192, 192, 192)
    orange = (255, 140, 0)
    light_orange = (255, 79, 0)

    # спиды
    palka_speed = 1
    lava_speed = 0.3


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
    first_cavity_color = white

    # 2 деталь (нижний элипс) полости (по сути дно стакана)
    second_cavity_points = (first_frame_x - first_frame_width * 1.5,
                           screen_height - (first_frame_height + first_frame_height * 5 / 1.25),
                           first_frame_width * 5 / 1.25,
                           first_frame_height * 5 / 1.25)
    second_cavity_color = light_grey

    # 3 деталь (прямоугольник) полости
    third_cavity_x = first_frame_x - first_frame_width * 1.5
    third_cavity_y = first_frame_height * 2 + first_frame_height * 2.5 / 1.25
    third_cavity_width = first_frame_width * 5 / 1.25
    third_cavity_height = screen_height - (first_frame_height + first_frame_height * 5 / 1.25) - first_frame_height * 2
    third_cavity_color = white



    # 1 деталь стакана (прямоугольник)
    first_glass_x = first_frame_x - first_frame_width * 1.5
    first_glass_y = first_frame_height * 2 + first_frame_height * 2.5 / 1.25 + (screen_height - (first_frame_height + first_frame_height * 5 / 1.25) - first_frame_height * 2)/2
    first_glass_width = first_frame_width * 5 / 1.25
    first_glass_height = (screen_height - (first_frame_height + first_frame_height * 5 / 1.25) - first_frame_height * 2)/2
    first_glass_color = silver

    # 2 деталь (нижний элипс) стакан лава
    second_glass_points = (first_frame_x - first_frame_width * 1.5,
                           screen_height - (first_frame_height + first_frame_height * 5.3),
                           first_frame_width * 5 / 1.25,
                           first_frame_height * 5 / 1.1)
    second_glass_color = orange

    # 3 деталь (верхний элипс) стакан
    third_glass_points = (first_frame_x - first_frame_width * 1.5,
                           first_frame_height * 6.1,
                           first_frame_width * 5 / 1.25,
                           first_frame_height * 5 / 1.25)
    third_glass_color = silver

    # 4 деталь (левый прямоугольник) стакан
    fourth_glass_x = first_frame_x - first_frame_width * 1.5
    fourth_glass_y = first_frame_height * 7
    fourth_glass_width = first_frame_height * 5 * 0.15
    fourth_glass_height = first_frame_height * 5.2
    fourth_glass_color = light_grey

    # 5 деталь (правый прямоугольник) стакан
    fifth_glass_x = first_frame_x + first_frame_width * 2.18
    fifth_glass_y = first_frame_height * 7
    fifth_glass_width = first_frame_height * 5 * 0.15
    fifth_glass_height = first_frame_height * 5.2
    fifth_glass_color = light_grey

    # 6 деталь (прямоугольник) стакан лава
    sixth_glass_x = first_frame_x - first_frame_width * 1.5
    sixth_glass_y = first_frame_height * 8
    sixth_glass_width = first_frame_width * 5 / 1.25
    sixth_glass_height = first_frame_height * 4
    sixth_glass_color = orange

    # 7 деталь (верхний элипс) лава
    seventh_glass_points = (first_frame_x - first_frame_width * 1.5,
                           first_frame_height * 7,
                           first_frame_width * 5 / 1.25,
                           first_frame_height * 5 / 1.25)
    seventh_glass_color = orange

    # 1 деталь (белый прямоугольник сверху) палка
    first_palka_x = screen_width / 2 - first_frame_width / 4
    first_palka_y = 0
    first_palka_width = first_frame_width / 2
    first_palka_height = first_frame_height * 3
    first_palka_color = white

    # 2 деталь (тонкая палка) палка
    second_palka_x = screen_width / 2 - first_frame_width / 16
    second_palka_y = 0
    second_palka_width = first_frame_width / 8
    second_palka_height = first_frame_height * 8.5
    second_palka_color = light_grey

    # 3 деталь (трегульник) от палки
    third_palka_points = [(screen_width / 2 - first_frame_width * 0.006, first_frame_height * 8.4),
                          (screen_width / 2 - first_frame_width / 4, first_frame_height * 8.75),
                          (screen_width / 2 + first_frame_width / 4, first_frame_height * 8.75)] # верх, лево, право
    third_palka_color = light_orange

    # 4 деталь (толстая палка) лава
    fourth_palka_x = screen_width / 2 - first_frame_width / 4
    fourth_palka_y = first_frame_height * 8.75
    fourth_palka_width = first_frame_width / 2
    fourth_palka_height = first_frame_height * 3.25
    fourth_palka_color = light_orange

    # кнопка начала анимации
    button_rect = pygame.Rect(10, 10, 240, 40)
    button_color = (0, 255, 0)
    button_text = "Начать анимацию"
    font = pygame.font.Font(None, 36)
    text_surface = font.render(button_text, True, (0, 0, 0))

    animation_started = False


    # Основной аниме цикл
    running = True
    while running:

        # Заливка экрана цветов
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    if not animation_started:
                        animation_started = True
                        second_palka_y = 0
                        fourth_palka_y = first_frame_height * 8.75
                        third_palka_points = [(screen_width / 2 - first_frame_width * 0.006, first_frame_height * 8.4),
                                              (screen_width / 2 - first_frame_width / 4, first_frame_height * 8.75),
                                              (screen_width / 2 + first_frame_width / 4, first_frame_height * 8.75)]
                        sixth_glass_y = first_frame_height * 8
                        sixth_glass_height = first_frame_height * 4
                        seventh_glass_points = (first_frame_x - first_frame_width * 1.5,
                                                first_frame_height * 7,
                                                first_frame_width * 5 / 1.25,
                                                first_frame_height * 5 / 1.25)



        if fourth_palka_y <= first_frame_height * 3:
            animation_started = False


        if animation_started:
            second_palka_y -= palka_speed
            fourth_palka_y -= palka_speed

            third_palka_points = [(x, y - palka_speed) for x, y in third_palka_points]

            if fourth_palka_y + fourth_palka_height >= sixth_glass_y:
                sixth_glass_y += lava_speed
                sixth_glass_height -= lava_speed

                x, y, width, height = seventh_glass_points
                y += lava_speed
                seventh_glass_points = (x, y, width, height)
        else:
            # Рисуем кнопку
            pygame.draw.rect(screen, button_color, button_rect)
            screen.blit(text_surface, (20, 20))


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

        # 3 деталь (прямоугольник) полости
        pygame.draw.rect(screen, third_cavity_color, (third_cavity_x, third_cavity_y, third_cavity_width, third_cavity_height))

        # 2 деталь (нижний элипс) корпуса
        pygame.draw.ellipse(screen, second_cavity_color, second_cavity_points)

        # 2 деталь (нижний элипс) стакан
        pygame.draw.ellipse(screen, second_glass_color, second_glass_points)

        # 1 деталь (прямоугольник сильвер)
        pygame.draw.rect(screen, first_glass_color, (first_glass_x, first_glass_y, first_glass_width, first_glass_height))

        # 3 деталь (верхний элипс) стакан
        pygame.draw.ellipse(screen, third_glass_color, third_glass_points)

        # 7 деталь (верхний элипс) лава
        pygame.draw.ellipse(screen, seventh_glass_color, seventh_glass_points)

        # 1 деталь (прямоугольник) палка
        pygame.draw.rect(screen, first_palka_color, (first_palka_x, first_palka_y, first_palka_width, first_palka_height))

        # 3 деталь (треугольник)
        pygame.draw.polygon(screen, third_palka_color, third_palka_points)

        # 4 деталь (толстая палка) палка
        pygame.draw.rect(screen, fourth_palka_color, (fourth_palka_x, fourth_palka_y, fourth_palka_width, fourth_palka_height))

        # 6 деталь (прямоугольник лава)
        pygame.draw.rect(screen, sixth_glass_color, (sixth_glass_x, sixth_glass_y, sixth_glass_width, sixth_glass_height))

        # 2 деталь (палка) палка
        pygame.draw.rect(screen, second_palka_color, (second_palka_x, second_palka_y, second_palka_width, second_palka_height))

        # 4 деталь (левый прямоугольник) стакан
        pygame.draw.rect(screen, fourth_glass_color, (fourth_glass_x, fourth_glass_y, fourth_glass_width, fourth_glass_height))

        # 5 деталь (правый прямоугольник) стакан
        pygame.draw.rect(screen, fifth_glass_color, (fifth_glass_x, fifth_glass_y, fifth_glass_width, fifth_glass_height))

        pygame.time.delay(10)

        # Обновление экрана
        pygame.display.flip()

    pygame.quit()
