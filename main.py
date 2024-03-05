# import sys module 
import pygame 
import sys 
import random
import time

pygame.init() 
timer = pygame.time.Clock() 
size_x = 1000
size_y = 800
screen = pygame.display.set_mode([size_x, size_y])
pygame.display.set_caption('image')

#изображение
imp = pygame.image.load("klava.png").convert()

food_image = pygame.image.load('LeftHand2.png')
character_image = pygame.image.load('LeftHand2.png')

#шрифт
base_font = pygame.font.SysFont("liberationmono", 25) 
user_text = '' 
#liberationmono
#62
#Notosansmonocjkkr
# прямоугольник для текста
#, set_underlline = True
input_rect = pygame.Rect(30, 100, size_x - 30 * 2, 32) 

#цвет для активного
color_active = pygame.Color('lightskyblue3') 

#цвет для не активного 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 

active = False



class Hands(pygame.sprite.Sprite):
    def __init__(self, char):
        super().__init__()
        self.char = char
        if self.char in ['п', 'а', 'к', 'е', 'п', 'и', 'м', 'с', 'и', '5', '6', ':', '%']:
            print(char)
            self.image = pygame.transform.scale(character_image, (100, 100))
            self.rect = self.image.get_rect()
            if char == 'а':
                self.rect.x = 300
                self.rect.y = 520
            elif char == 'п':
                self.rect.x = 300 + 50
                self.rect.y = 520
            #elif char == 'к':

            

        else:
            self.image = pygame.transform.scale(character_image, (100, 100))
            self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def grow(self):
        self.size += 10

    def is_collision(self, food):
        if self.rect.x < food.rect.x < self.rect.x + self.size and self.rect.y < food.rect.y < self.rect.y + self.size:
            return True
        return False







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



def Delay():
    start_time = pygame.time.get_ticks()
    curr_time = pygame.time.get_ticks()
    while (curr_time - start_time) < 300:
        for event in pygame.event.get():
            p = event.type
            curr_time = pygame.time.get_ticks()
            pygame.draw.rect(screen, (230, 0, 0), input_rect)
            pygame.display.flip()  
			

    

lines = [get_words(), get_words(), get_words()]

def Refresh():
    lines[0] = lines[1]
    lines[1] = lines[2]
    lines[2] = get_words
print(lines)

ind = 0
flag = True



while True: 
    for event in pygame.event.get(): 

        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
            #ПРОВЕРЯЕМ ЧТО БЫЛ клик мышью
        #if event.type == pygame.MOUSEBUTTONDOWN: 
        #    if input_rect.collidepoint(event.pos): 
        #        active = True
        #    else: 
        #        active = False
            
            #проверяем что было нажатие на клавиатуре
        if event.type == pygame.KEYDOWN: 
            #time_start = pygame.time()
            # Check for backspace 
            #if event.key == pygame.K_BACKSPACE: 

                # get text input from 0 to -1 i.e. end. 
                #user_text = user_text[:-1] 
            #if lines[0][ind] in [":", ";", "{", "}", "(", ")", ""]
            if event.unicode == lines[0][ind]:
                user_text += event.unicode
                cur_char = lines[0][ind]
                hand_c = Hands(cur_char)
                hand_c.draw()
                ind += 1
                if len(lines[0]) == ind:
                    lines[0] = lines[1]
                    lines[1] = lines[2]
                    lines[2] = get_words()
                    ind = 0
                    user_text = ''
            elif event.unicode != '':
                #рисуем прямоугольник



                pygame.draw.rect(screen, (230, 0, 0), input_rect) 
                #pygame.display.flip() 
                #определяем наш текст цвет
                text_surface = base_font.render(user_text, 0, (0, 0, 0)) 
                
                
                #рисуем текст 
                screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
                
                #вставляем клавиатуру
                screen.blit(imp, (35, size_y//2 - 50))

                cur_char = lines[0][ind]
                hand_c = Hands(cur_char)
                hand_c.draw()



                line_s = lines[0][ : ind]
                text_surface1 = base_font.render(line_s, 0, (170, 170, 170)) 
                screen.blit(text_surface1, (input_rect.x+5, input_rect.y + 40))

                line_f = lines[0][ind:]
                text_surface2 = base_font.render(line_f, 0, (0, 0, 0)) 
                screen.blit(text_surface2, (text_surface1.get_width()+34, input_rect.y + 40))


                for i in range(1, 3):
                    line = lines[i]
                    text_surface = base_font.render(line, 0, (0, 0, 0)) 
                    #рисуем текст 
                    screen.blit(text_surface, (input_rect.x+5, input_rect.y + 40*(i + 1))) 

                line_0 = lines[0][ind]
                new_base_font = pygame.font.SysFont("liberationmono", 25)
                new_base_font.set_underline(1)
                char = new_base_font.render(line_0, 0, (0, 0, 0))
                screen.blit(char, (text_surface1.get_width()+34, input_rect.y + 40))



                #pygame.display.flip() 
                #pygame.time.wait(300)
                #Delay()
                #pygame.draw.rect(screen, color, input_rect)
                pygame.display.flip()  
                time.sleep(0.3)

    
    #заливаем фон
    screen.fill((255, 255, 255)) 

    if active: 
        color = color_active 
    else: 
        color = color_passive 
        
    #рисуем прямоугольник
    pygame.draw.rect(screen, color, input_rect) 

    #определяем наш текст цвет
    text_surface = base_font.render(user_text, 0, (0, 0, 0)) 
    
    
    #рисуем текст 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
    
    #вставляем клавиатуру
    screen.blit(imp, (35, 350))


    cur_char = lines[0][ind]
    hand_c = Hands(cur_char)
    hand_c.draw()



    line_s = lines[0][ : ind]
    text_surface1 = base_font.render(line_s, 0, (170, 170, 170)) 
    screen.blit(text_surface1, (input_rect.x+5, input_rect.y + 40))

    line_f = lines[0][ind:]
    text_surface2 = base_font.render(line_f, 0, (0, 0, 0)) 
    screen.blit(text_surface2, (text_surface1.get_width()+34, input_rect.y + 40))


    for i in range(1, 3):
        line = lines[i]
        text_surface = base_font.render(line, 0, (0, 0, 0)) 
        #рисуем текст 
        screen.blit(text_surface, (input_rect.x+5, input_rect.y + 40*(i + 1))) 

    line_0 = lines[0][ind]
    new_base_font = pygame.font.SysFont("liberationmono", 25)
    new_base_font.set_underline(1)
    char = new_base_font.render(line_0, 0, (0, 0, 0))
    screen.blit(char, (text_surface1.get_width()+34, input_rect.y + 40))

    pygame.display.flip() 

    #расширяем окошко
	#input_rect.w = max(100, text_surface.get_width()+10) 
	
	# display.flip() will update only a portion of the 
	# screen to updated, not full area 
    #60 кадров в секунду 
    timer.tick(100) 
    