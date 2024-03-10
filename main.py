# import sys module 
import pygame 
import sys 
import random
import time


pygame.init() 
timer = pygame.time.Clock() 
size_x = 1000
size_y = 560
RED = (230, 0, 0)
screen = pygame.display.set_mode([size_x, size_y], pygame.RESIZABLE)
pygame.display.set_caption('image')

virtual_surface = pygame.Surface([size_x, size_y])

#изображение
imp = pygame.image.load("klava.png")
default_image_size = (750, 250)
imp = pygame.transform.scale(imp, default_image_size)
default_image_position = (120, 300)
food_image = pygame.image.load('LeftHand2.png')
character_image = pygame.image.load('LeftHand2.png')

#шрифт
base_font = pygame.font.SysFont("liberationmono", 25) 
menu_font = pygame.font.SysFont("liberationmono", 20)
train_font = pygame.font.SysFont("liberationmono", 50)

user_text = '' 

input_rect = pygame.Rect(30, 100, size_x - 30 * 2, 32)
menu_rect = pygame.Rect (30, 20, 60, 30)
train_rect = pygame.Rect(350, 100, 300, 80)
newtext_rect = pygame.Rect(350, 200, 300, 80)


#цвет для активного
color_active = pygame.Color('lightskyblue3') 

#цвет для не активного 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 

active = False


def find_max():
    arr = []
    bd = open("score.txt", "r")
    for line in bd:
        arr.append(int(line))

    m = max(arr)
    bd = open("score.txt", "w")
    bd.write(str(m) + '\n')
    bd.close()
    return m


def get_words():
    f = open('sample2.txt').read()
    words = f.split(' ')
    lenght = 0
    sentence = ''
    while (lenght < 63):
        word = random.choice(words) + ' '
        l_word = len(word) + 1
        if (l_word + lenght) >= 63:
            return sentence
        else:
            sentence = sentence + word
            lenght += l_word
			
lines = [get_words(), get_words(), get_words()]

def Refresh():
    lines[0] = lines[1]
    lines[1] = lines[2]
    lines[2] = get_words()

#кнопка меню
def menu_button():
    pygame.draw.rect(virtual_surface, (170, 170, 170), menu_rect)
    text_menu = menu_font.render("exit", 0, (0, 0, 0))
    virtual_surface.blit(text_menu, (menu_rect.x+5, menu_rect.y + 5))


scores = []
curr_record = 0
def start_the_train():
    ind = 0
    user_text = ''
    current_size = screen.get_size()
    running = True
    amount = 0
    time_start = 0
    flag = False
    score = 0
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                current_size = event.size

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if menu_rect.collidepoint(event.pos):
                    running = False
                    time_start = 0
                    amount = 0
                    curr_record = max(scores)
                    bd =  open('score.txt', 'a')
                    bd.write(str(curr_record) + '\n')
                    bd.close()
                    menu()

            if event.type == pygame.KEYDOWN: 
                if time_start == 0:
                    time_start = pygame.time.get_ticks()
                # Check for backspace 
                #if event.key == pygame.K_BACKSPACE: 

                    # get text input from 0 to -1 i.e. end. 
                    #user_text = user_text[:-1] 
                #if lines[0][ind] in [":", ";", "{", "}", "(", ")", ""]
                if event.unicode == lines[0][ind]:

                    if lines[0][ind] == ' ':
                        flag = True
                    user_text += event.unicode
                    amount += 1
                    ind += 1

                    if len(lines[0]) == ind:
                        lines[0] = lines[1]
                        lines[1] = lines[2]
                        lines[2] = get_words()
                        ind = 0
                        user_text = ''


                elif event.unicode != '':
                    #рисуем прямоугольник
                    pygame.draw.rect(virtual_surface, (230, 0, 0), input_rect) 
                    #pygame.display.flip() 
                    #определяем наш текст цвет
                    text_surface = base_font.render(user_text, 0, (0, 0, 0)) 
                    #рисуем текст 
                    virtual_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
                    
                    #вставляем клавиатуру
                    virtual_surface.blit(imp, default_image_position)



                    line_s = lines[0][ : ind]
                    text_surface1 = base_font.render(line_s, 0, (170, 170, 170)) 
                    virtual_surface.blit(text_surface1, (input_rect.x+5, input_rect.y + 40))

                    line_f = lines[0][ind:]
                    text_surface2 = base_font.render(line_f, 0, (0, 0, 0)) 
                    virtual_surface.blit(text_surface2, (text_surface1.get_width()+34, input_rect.y + 40))


                    for i in range(1, 3):
                        line = lines[i]
                        text_surface = base_font.render(line, 0, (0, 0, 0)) 
                        #рисуем текст 
                        virtual_surface.blit(text_surface, (input_rect.x+5, input_rect.y + 40*(i + 1))) 

                    line_0 = lines[0][ind]
                    new_base_font = pygame.font.SysFont("liberationmono", 25)
                    new_base_font.set_underline(1)
                    char = new_base_font.render(line_0, 0, (0, 0, 0))
                    virtual_surface.blit(char, (text_surface1.get_width()+34, input_rect.y + 40))



                    #pygame.display.flip() 
                    #pygame.time.wait(300)
                    #Delay()
                    #pygame.draw.rect(screen, color, input_rect)
                    menu_button()
 

                    scaled_surface = pygame.transform.scale(virtual_surface, current_size)
                    screen.blit(scaled_surface, (0, 0))
                    pygame.display.flip()  
                    time.sleep(0.3)



        
        #заливаем фон
        virtual_surface.fill((255, 255, 255)) 
            
        #рисуем прямоугольник

        pygame.draw.rect(virtual_surface, color, input_rect) 
        #score = amount/(time_start - time_finish)
        #text_score = base_font.render(str(score), 0, (0, 0, 0))
        #определяем наш текст цвет
        text_surface = base_font.render(user_text, 0, (0, 0, 0)) 
        
        time_finish = pygame.time.get_ticks()
        if flag:
            if (time_finish - time_start) < 1:
                score = 0.0
                flag = False
            else:
                score = int(amount/(time_finish - time_start) * 1000 * 60)
                flag = False
                scores.append(score)



        text_score = base_font.render(str(score) + ' симв/мин', 0, (0, 0, 0))
        virtual_surface.blit(text_score, (800, 30))
        menu_button()

        
        #рисуем текст 
        virtual_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        #virtual_surface.blit(text_score, (900, 30))
        
        #вставляем клавиатуру
        virtual_surface.blit(imp, default_image_position)



        line_s = lines[0][ : ind]
        text_surface1 = base_font.render(line_s, 0, (170, 170, 170)) 
        virtual_surface.blit(text_surface1, (input_rect.x+5, input_rect.y + 40))

        line_f = lines[0][ind:]
        text_surface2 = base_font.render(line_f, 0, (0, 0, 0)) 
        virtual_surface.blit(text_surface2, (text_surface1.get_width()+34, input_rect.y + 40))


        for i in range(1, 3):
            line = lines[i]
            text_surface = base_font.render(line, 0, (0, 0, 0)) 
            #рисуем текст 
            virtual_surface.blit(text_surface, (input_rect.x+5, input_rect.y + 40*(i + 1))) 

        line_0 = lines[0][ind]
        new_base_font = pygame.font.SysFont("liberationmono", 25)
        new_base_font.set_underline(1)
        char = new_base_font.render(line_0, 0, (0, 0, 0))
        virtual_surface.blit(char, (text_surface1.get_width()+34, input_rect.y + 40))
        
        scaled_surface = pygame.transform.scale(virtual_surface, current_size)
        screen.blit(scaled_surface, (0, 0))
        pygame.display.flip() 

        #расширяем окошко
        #input_rect.w = max(100, text_surface.get_width()+10) 
        
        # display.flip() will update only a portion of the 
        # screen to updated, not full area 
        #60 кадров в секунду 
        timer.tick(60)



def menu():
    running = True
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

            if event.type == pygame.VIDEORESIZE:
                current_size = event.size


            if event.type == pygame.MOUSEBUTTONDOWN: 
                if train_rect.collidepoint(event.pos):
                    running = False
                    start_the_train()
        rec = str(find_max())

        virtual_surface.fill((255, 255, 255))
        pygame.draw.rect(virtual_surface, color, train_rect)
        text_surface = train_font.render("тренировка", 0, (0, 0, 0)) 
        virtual_surface.blit(text_surface, (train_rect.x+1, train_rect.y+5))

        text_rec = base_font.render("Рекорд: " + rec + " симв/мин", 0, (0, 0, 0))
        virtual_surface.blit(text_rec, (50, 50))
        current_size = screen.get_size()
        scaled_surface = pygame.transform.scale(virtual_surface, current_size)
        screen.blit(scaled_surface, (0, 0))
        pygame.display.flip() 
        timer.tick(60)

menu()



    
