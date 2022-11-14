import pygame
import random

pygame.init()

#Definition variables
width, height = 900, 900
white = (255,255,255)
black = (0,0,0)
FPS = 200
Monopoly_board_image = pygame.image.load('monopoly board.jpeg')
Monopoly_board = pygame.transform.scale(Monopoly_board_image, (900, 900))
WIN = pygame.display.set_mode((width,height))
pygame.display.set_caption('Monopoly')



#images and trnasformation of them
car_image= pygame.image.load('monopoly car.png')
car = pygame.transform.scale(car_image, (80, 60))
dice_image= pygame.image.load('Dice image.jpg')
dice_car=pygame.transform.scale(dice_image, (80, 60))
dog_image = pygame.image.load('dog_image.png')
dog = pygame.transform.scale(dog_image, (80, 60))

#discussion rectangle 
discussion_rectangle= pygame.Rect(250,250,400,400)
font= pygame.font.SysFont("Times New Roman",15, True,False) #case text about which nb it goes to

text_surface_throw_dice_for_car = font.render('throw dice for car', True, (black))
text_surface_throw_dice_for_dog = font.render('throw dice for dog', True, (black))






class pieces():
    def __init__(self, x,y,width,height,position):
        self.rect= pygame.Rect(x,y,width,height)
        self.position= position 

piece_1 = pieces(780,770,80,60,0)
piece_2 = pieces(810,830,80,60,0)




class buttons():
    def __init__(self,x,y,width,height,piece):
        self.rect= pygame.Rect(x,y,width,height)
        self.piece=piece
        self.clicked= False


    def click (self):
        pos = pygame.mouse.get_pos() #position mouse
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and self.clicked==False:
            self.clicked=True    
            throw_dice(self.piece) 
            
                     
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False


button_throw_dice_for_car=buttons(320,550,80,60,piece_1)
button_throw_dice_for_dog=buttons(490,550,80,60,piece_2)






#We define all the cases as pygame rectangles
case_go = pygame.Rect(770,770,120,120)
case_brown_1 = pygame.Rect(695,770,77,120)
case_community_chess_1=pygame.Rect(630,770,68,120)
case_brown_2=pygame.Rect(560,770,70,120)
case_income_tax_1=pygame.Rect(487,770,73,120)
case_train_station_1=pygame.Rect(415,770,73,120)
case_light_blue_1=pygame.Rect(343,770,73,120)
case_luck_1=pygame.Rect(271,770,73,120)
case_light_blue_2=pygame.Rect(199,770,73,120)
case_light_blue_3=pygame.Rect(127,770,73,120)
case_jail= pygame.Rect(10,770,120,120)
case_pink_1=pygame.Rect(10,700,120,70)
case_electricity=pygame.Rect(10,629,120,71)
case_pink_2=pygame.Rect(10,558,120,71)
case_pink_3=pygame.Rect(10,487,120,71)
case_train_station_2=pygame.Rect(10,416,120,71)
case_orange_1=pygame.Rect(10,345,120,71)
case_community_chess_2=pygame.Rect(10,274,120,71)
case_orange_2=pygame.Rect(10,203,120,71)
case_orange_3=pygame.Rect(10,130,120,71)
case_free_parking= pygame.Rect(10,10,120,120)
case_red_1=pygame.Rect(127,10,74,120)
case_luck_2=pygame.Rect(200,10,70,120)
case_red_2=pygame.Rect(272,10,72,120)
case_red_3=pygame.Rect(344,10,72,120)
case_train_station_3=pygame.Rect(416,10,72,120)
case_yellow_1=pygame.Rect(488,10,72,120)
case_yellow_2=pygame.Rect(560,10,72,120)
case_water=pygame.Rect(632,10,72,120)
case_yellow_3=pygame.Rect(704,10,70,120)
case_go_to_jail = pygame.Rect(770,10,120,120)
case_green_1 = pygame.Rect(770,130,120,71)
case_green_2 = pygame.Rect(770,201,120,71)
case_community_chess_3 = pygame.Rect(770,272,120,71)
case_green_3 = pygame.Rect(770,343,120,74)
case_train_station_4 = pygame.Rect(770,417,120,72)
case_luck_3 = pygame.Rect(770,489,120,72)
case_dark_blue_1 = pygame.Rect(770,561,120,72)
case_luxury_tax= pygame.Rect(770,633,120,68)
case_dark_blue_2 = pygame.Rect(770,701,120,72)





#Fill the interface with stuff
def draw_monopoly():
    WIN.fill(white)
    WIN.blit(Monopoly_board, (0,0))    
    pygame.draw.rect(WIN,black,discussion_rectangle,2)
    pygame.draw.rect(WIN,black,case_go,2)
    pygame.draw.rect(WIN,black,case_brown_1,2)
    pygame.draw.rect(WIN,black,case_community_chess_1,2)
    pygame.draw.rect(WIN,black,case_brown_2,2)
    pygame.draw.rect(WIN,black,case_income_tax_1,2)
    pygame.draw.rect(WIN,black,case_train_station_1,2)
    pygame.draw.rect(WIN,black,case_light_blue_1,2)
    pygame.draw.rect(WIN,black,case_luck_1,2)
    pygame.draw.rect(WIN,black,case_light_blue_2,2)
    pygame.draw.rect(WIN,black,case_light_blue_3,2)
    pygame.draw.rect(WIN,black,case_jail,2)
    pygame.draw.rect(WIN,black,case_pink_1,2)
    pygame.draw.rect(WIN,black,case_electricity,2)
    pygame.draw.rect(WIN,black,case_pink_2,2)
    pygame.draw.rect(WIN,black,case_pink_3,2)
    pygame.draw.rect(WIN,black,case_train_station_2,2)
    pygame.draw.rect(WIN,black,case_orange_1,2)
    pygame.draw.rect(WIN,black,case_community_chess_2,2)
    pygame.draw.rect(WIN,black,case_orange_2,2)
    pygame.draw.rect(WIN,black,case_orange_3,2)
    pygame.draw.rect(WIN,black,case_free_parking,2)
    pygame.draw.rect(WIN,black,case_red_1,2)
    pygame.draw.rect(WIN,black,case_luck_2,2)
    pygame.draw.rect(WIN,black,case_red_2,2)
    pygame.draw.rect(WIN,black,case_red_3,2)
    pygame.draw.rect(WIN,black,case_train_station_3,2)
    pygame.draw.rect(WIN,black,case_yellow_1,2)
    pygame.draw.rect(WIN,black,case_yellow_2,2)
    pygame.draw.rect(WIN,black,case_water,2)
    pygame.draw.rect(WIN,black,case_yellow_3,2)
    pygame.draw.rect(WIN,black,case_go_to_jail,2)
    pygame.draw.rect(WIN,black,case_green_1,2)
    pygame.draw.rect(WIN,black,case_green_2,2)
    pygame.draw.rect(WIN,black,case_community_chess_3,2)
    pygame.draw.rect(WIN,black,case_green_3,2)
    pygame.draw.rect(WIN,black,case_train_station_4,2)
    pygame.draw.rect(WIN,black,case_luck_3,2)
    pygame.draw.rect(WIN,black,case_dark_blue_1,2)
    pygame.draw.rect(WIN,black,case_luxury_tax,2)
    pygame.draw.rect(WIN,black,case_dark_blue_2,2)






    WIN.blit(car,(piece_1.rect.x, piece_1.rect.y))
    WIN.blit(dog,(piece_2.rect.x, piece_2.rect.y))
    WIN.blit(dice_car,(button_throw_dice_for_car.rect.x,button_throw_dice_for_car.rect.y))    
    WIN.blit(dice_car,(button_throw_dice_for_dog.rect.x, button_throw_dice_for_dog.rect.y))
    WIN.blit(text_surface_throw_dice_for_car, (300,620))
    WIN.blit(text_surface_throw_dice_for_dog,(510,620))
    
    
    pygame.display.update()


def text_to_throw(piece,x):
    Text_to_display= font.render(f'{piece} moves {x}', True, (black))
    WIN.blit(Text_to_display,(250,250))
    pygame.display.update()
    






def throw_dice(piece):
    x=random.randint(1,6)
    piece.position=piece.position+x
    text_to_throw(piece,x)  
   
    if piece.position>39:
        piece.position = piece.position - 40
    if piece.position ==0:
        piece.rect.x = case_go.x
        piece.rect.y = case_go.y
    if piece.position ==1:
        piece.rect.x = case_brown_1.x
        piece.rect.y = case_go.y
    if piece.position ==2:
        piece.rect.x = case_community_chess_1.x
        piece.rect.y = case_go.y
    if piece.position==3:
        piece.rect.x = case_brown_2.x
        piece.rect.y = case_go.y
    if piece.position==4:
        piece.rect.x = case_income_tax_1.x
        piece.rect.y = case_go.y
    if piece.position==5:
        piece.rect.x = case_train_station_1.x
        piece.rect.y = case_go.y
    if piece.position==6:
        piece.rect.x = case_light_blue_1.x
        piece.rect.y = case_go.y
    if piece.position==7:
        piece.rect.x = case_luck_1.x
        piece.rect.y = case_go.y
    if piece.position==8:
        piece.rect.x = case_light_blue_2.x
        piece.rect.y = case_go.y
    if piece.position==9:
        piece.rect.x = case_light_blue_3.x
        piece.rect.y = case_go.y
    if piece.position==10:
        piece.rect.x = case_jail.x
        piece.rect.y = case_go.y
    if piece.position==11:
        piece.rect.x = case_jail.x
        piece.rect.y = case_pink_1.y
    if piece.position==12:
        piece.rect.x = case_jail.x
        piece.rect.y = case_electricity.y
    if piece.position==13:
        piece.rect.x = case_jail.x
        piece.rect.y = case_pink_2.y
    if piece.position==14:
        piece.rect.x = case_jail.x
        piece.rect.y = case_pink_3.y
    if piece.position==15:
        piece.rect.x = case_jail.x
        piece.rect.y = case_train_station_2.y
    if piece.position==16:
        piece.rect.x = case_jail.x
        piece.rect.y = case_orange_1.y
    if piece.position==17:
        piece.rect.x = case_jail.x
        piece.rect.y = case_community_chess_2.y
    if piece.position==18:
        piece.rect.x = case_jail.x
        piece.rect.y = case_orange_2.y
    if piece.position==19:
        piece.rect.x = case_jail.x
        piece.rect.y = case_orange_3.y
    if piece.position==20:
        piece.rect.x = case_jail.x
        piece.rect.y = case_free_parking.y    
    if piece.position==21:
        piece.rect.x = case_red_1.x
        piece.rect.y = case_free_parking.y    
    if piece.position==22:
        piece.rect.x = case_luck_2.x
        piece.rect.y = case_free_parking.y
    if piece.position==23:
        piece.rect.x = case_red_2.x
        piece.rect.y = case_free_parking.y
    if piece.position==24:
        piece.rect.x = case_red_3.x
        piece.rect.y = case_free_parking.y
    if piece.position==25:
        piece.rect.x = case_train_station_3.x
        piece.rect.y = case_free_parking.y
    if piece.position==26:
        piece.rect.x = case_yellow_1.x
        piece.rect.y = case_free_parking.y
    if piece.position==27:
        piece.rect.x = case_yellow_2.x
        piece.rect.y = case_free_parking.y
    if piece.position==28:
        piece.rect.x = case_water.x
        piece.rect.y = case_free_parking.y
    if piece.position==29:
        piece.rect.x = case_yellow_3.x
        piece.rect.y = case_free_parking.y
    if piece.position==30:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_free_parking.y
    if piece.position==31:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_green_1.y
    if piece.position==32:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_green_2.y
    if piece.position==33:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_community_chess_3.y
    if piece.position==34:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_green_3.y
    if piece.position==35:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_train_station_4.y
    if piece.position==36:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_luck_3.y
    if piece.position==37:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_dark_blue_1.y
    if piece.position==38:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_luxury_tax.y
    if piece.position==39:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_dark_blue_2.y

    
    
    
    


    






def main():
    clock =pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_monopoly()
        buttons.click(button_throw_dice_for_car)
        buttons.click(button_throw_dice_for_dog)


        
    pygame.quit()


main()

