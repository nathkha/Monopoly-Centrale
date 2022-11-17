import pygame
import random
import os

class Case():
    def __init__(case,name,index,info):
        case.name = name
        case.index = index #place on the board, this will be useful
        case.info=info

    def __str__(self):
        print("Name:"+self.name+" Position: "+str(self.index)+str(self.info))



class Street(Case):
    hotel=0
    house=0
    def __init__(self,name,price,index,color,owner,info):
        super().__init__(name,index,info)
        self.color=color
        self.price=price
        self.owner=owner
    def __str__(self):
        print("Name: "+self.name+" price: "+str(self.price)+" index: "+str(self.index)+" color: "+self.color+" owner: "+self.owner)

class Chance(Case):
    def __init__(self,name,index,info):
        super().__init__(name,index,info)

class Crous(Case):
    def __init__(self,name,price,index,owner,info):
        super().__init__(name,index,info)
        self.owner=owner
        self.price=price

class Company(Case):
    def __init__(self,name,price,index,owner,info):
        super().__init__(name,index,info)
        self.owner=owner
        self.price=price

case_0 = Case('GO',0,'gives 200 if player goes through it')
case_1 = Street('F3-05',60,1,'brown','','if bought, other players need to pay rent')
case_2 = Chance('community chest',2,'pick a community chest card')
case_3 = Street('F3-06',60,3,'brown','','if bought, other players need to pay rent')
case_4 = Case('School fee',4,'pay_100')
case_5 = Crous('Crous Breguet',150,5,'','if bought, other players need to pay rent + rent increases if owner has several crous')
case_6 = Street('F2-05',100,6,'light blue',"",'if bought, other players need to pay rent')
case_7 = Chance('chance',7,'pick a chance card')
case_8 = Street('F2-06',110,8,'light blue',"",'if bought, other players need to pay rent')
case_9 = Street('F2-07',120,9,'light blue',"",'if bought, other players need to pay rent')
case_10 = Case('Musée',10,'if only passing, no effect, else need a double to get out')
case_11 = Street('césal I',140,11,'pink',"",'if bought, other players need to pay rent')
case_12 = Company('electricity',150,12,'','if bought, other players need to pay rent + rent increases if owner has water also')

list_cases = [case_0, case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9, case_10, case_11, case_12]

def list_players():
    shape=["hat","iron","car","boat"]
    list_players=[]
    n=int(input("How many players ?"))
    for i in range(n):
        x=input("What is the name of the player ?")
        list_players.append(Players(x,shape[i],0,2500,[]))
    return list_players


class pieces():
    def __init__(self, name,x,y,width,height,position):
        self.name=name
        self.rect= pygame.Rect(x,y,width,height)
        self.position= position

piece_1 = pieces("car",780,770,80,60,0)
piece_2 = pieces("dog",810,830,80,60,0)

class Players:

    def __init__(player,name,pieces,position, money,properties):
        player.name=name
        player.pieces=pieces
        player.position = position
        player.money = money
        player.properties=properties

    def __strposition__(player): #Giving the position to the players as a number is useless
         return list_cases[player.position].name


    def __str__(player):#Print the information about the player
        print("Name: "+player.name,end="\n")

        print(player.__strposition__(),end="")
        print(" Money: "+str(player.money),end="\n")
        for i in player.properties:
            print(i.name,sep=";")

    def buy_case(player,case):
        if(isinstance(case,Street) or isinstance(case,Company) or isinstance(case,Crous)): #We check the case can be bought
            if(player.money>case.price): #Check if the player has enough money
                player.properties.append(case)
                player.money=player.money-case.price
                case.owner=player
            else: #If the player doesn't have enough money, we do nothing
                print("Not enough money, comeback later")
                return

    def check_colors(player,case):
        a=case.color
        s=0
        for i in player.properties:
            if(i.color==a):
                s+=1
        return s

    def number_companies(player):
        s=0
        for i in player.properties:
            if(isinstance(i,Company)):
                s+=1
        return s

    def buy_house(player,case):
        if(isinstance(case,Street)):
            if(player.check_colors(case)==3):
                print('You can build a house for 100')
                x=int(input("How many houses do you want ? "))
                if(100*x>player.money):
                    print("Not enough money for this number of houses, you have ", player.money)
                    x=int(input("How many houses do you want ? "))
                case.house=x
                case.price+=100*x
                player.money-=100*x
        else:
            print("Impossible to build a house on this case, you need all the properties of the same colour")
            return

    def mortgage(player):
        for i in player.properties:
            i.__str__()
            print("1.Sell this property to the bank ? ")
            print("2.Keep it")
            x=int(input("Choice: "))
            if(x==1):
                player.properties.remove(i)
                player.money+=i.price
            else:
                continue







playt=Players("john",piece_1,0,2500,[])

playt.properties.append(case_1)

playt.properties.append(case_3)

playt2=Players("bob",piece_2,0,2500,[])
playt2.properties.append(case_8)
playt2.properties.append(case_9)




list_players=[playt,playt2]

def own(player,case):
    if(case in player.properties):
        return (1,player)
    if(case not in player.properties): #The case does not belong to the player
        for i in list_players:
            if(case in i.properties):
                return (0,i) # The case belongs to another player
        return (0,None) #The case belong to nobody




def own_2(player,case):
    tup=own(player,case)
    if(tup[0]==1):
        print("You are on your property")
        b=player.check_colors(case)
        if(b==3):
            print("You can buy accomodations on the case","You have",player.money,"of money")
            player.buy_house()
        else:
            print("Not enough properties, you need ",3-b," properties")
        return 0
    elif(tup[0]==0):
        if(tup[1]==None):
            print("This case belongs to nobody")
            case.__str__()
            print("Do you want to buy it ?","You have ",player.money," of money")
            print("1.Yes","2. No",sep="\n")
            x=int(input())
            if(x==1):
                player.buy_case(case)
            return 0
        else:
            print("You are on",tup[1].name,"property")
            print('You have to pay',case.price)
            if(player.money>=case.price):
                player.money-=case.price
                tup[1].money+=case.price
                print()
                return 0
            else:
                print("You don't have enough money")
                player.mortgage()
                if(player.money<case.price):
                    list_players.remove(player)#The player doesn' have enough money to pay even with the mortgages so he's out of the game
                    return -1
                else:
                    player.money-=case.price
                    tup[1].money+=case.price
                    return 0


def own_Crous(player,case):
    tup=own(player,case)
    if(tup[0]==1):
        print("You are on your property")
        return 0
    elif(tup[0]==0):
        if(tup[1]==None):
            print("This case belongs to nobody")
            case.__str__()
            print("Do you want to buy it ?","You have ",player.money," of money")
            print("1.Yes","2. No",sep="\n")
            x=int(input())
            if(x==1):
                player.buy_case(case)
            return 0
        else:
            print("You are on",tup[1].name,"property")
            print('You have to pay',case.price)
            if(player.money>=case.price):
                player.money-=case.price
                tup[1].money+=case.price
                print()
                return 0
            else:
                print("You don't have enough money")
                player.mortgage()
                if(player.money<case.price):
                    list_players.remove(player)#The player doesn' have enough money to pay even with the mortgages so he's out of the game
                    return -1
                else:
                    player.money-=case.price
                    tup[1].money+=case.price
                    return 0



def own_Company(player,case,dice):
    own_2(player,case)
    tup=own(player,case)
    if(tup[0]==1):
        print("You are on your property")
        return 0
    elif(tup[0]==0):
        if(tup[1]==None):
            print("This case belongs to nobody")
            case.__str__()
            print("Do you want to buy it ?","You have ",player.money," of money")
            print("1.Yes","2. No",sep="\n")
            x=int(input())
            if(x==1):
                player.buy_case(case)
            return 0
        else:
            print("You are on",tup[1].name,"property")
            e=tup[1].number_properties()
            print(tup[1].name,"has ",e," companies")
            if(e==1):
                b=4*dice
            elif(e==2):
                b=10*dice
            print('You have to pay',b)
            if(player.money>=b):
                player.money-=b
                tup[1].money+=b
                print()
                return 0
            else:
                print("You don't have enough money")
                player.mortgage()
                if(player.money<b):
                    list_players.remove(player)#The player doesn' have enough money to pay even with the mortgages so he's out of the game
                    return -1
                else:
                    player.money-=b
                    tup[1].money+=b
                    return 0


def repeat_the_index(player):
    if player.position >= len(list_cases):
        print("You went through the Go Case, you get 200")
        player.money+=200
        player.position = player.position % len(list_cases)
        return player.position
    else:
        return player.position

import random

def random_dice_throw(player):
    a = random.randint(1,6)
    b = random.randint(1,6)
    x = a+b
    print("Dice gave us", x)
    player.position = player.position+x                     #street_effect(player.position+x)
    print(f'{player.shape} moves to {list_cases[repeat_the_index(player)].name}')
    return (a,b)


def trad_case_to_position(name): #We have the name of the case and we want the index
        for i in list_cases:
            if(i.name==name):
                return i.index


class Cards:
    def __init__(card, tyype, index, action,amount,location,text):
        card.tyype = tyype
        card.index = index
        card.action = action
        card.amount=amount
        card.location=location
        card.text = text

    def recognize(card,player):
        if(card.action=="receive"):
            player.money+=card.amount
        elif(card.action=="pay"):
            player.money-=card.amount
        else:
            x=trad_case_to_position(card.location)
            player.position=x
            if(x<player.position): #We go back to the 'Go' case, so we have to give the player the money due
                player.money+=200


#Idea is to recognize a card
#For now 3 types of action: Pay, receive, Go_to
#Amount: The amount we owe or we receive
#Location: Where the card tell us to go


community_chest_card_1 = Cards('community_chest_card', 1, 'pay',100,'same', 'you faked having covid, pay the doctor 150')
community_chest_card_2 = Cards('community_chest_card', 2, 'pay',100,'same', 'pay the CVEC 100')
community_chest_card_3 = Cards('community_chest_card', 3, 'receive',80,"same", 'student fee error, get 80 back')

list_community_chest_cards = [community_chest_card_1, community_chest_card_2, community_chest_card_3]

chance_card_1 = Cards('chance_card', 1, 'receive',10,'same', 'You have won second prize in a beauty contest. Collect 10')
chance_card_2 = Cards('chance_card', 2, 'pay',60,'same', 'You destroyed your cesal appartement, pay 60')
chance_card_3 = Cards('chance_card', 3, 'receive',20,'same', 'its your birthday, receive 20 from every player')
chance_card_4 = Cards('chance_card',4,'go_to',0,'GO','You just graduated, go to the beginning of the game')

list_chance_cards = [chance_card_1, chance_card_2, chance_card_3,chance_card_4]


def pick_a_random_community_chest_card ():
    x = random.randint (0,2)
    random_pick = list_community_chest_cards[x]
    print (random_pick.text)
    return random_pick




def pick_a_random_chance_card ():
    x = random.randint (0,2)
    random_pick = list_chance_cards[x]
    print (random_pick.text)
    return random_pick



def play(player,dice):#dice=x
    print("Player: ",player.name)
    print("Money: ",player.money)
    case=list_cases[player.position] #We get the case where the player is
    if(isinstance(case,Street)):
        own_2(player,case)
    elif(isinstance(case,Chance)):
        if(case.name=="chance"):
            card=pick_a_random_chance_card()
            recognize(card,player)
        elif(case.name=="community chest"):
            card=pick_a_random_community_chest_card()
            recognize(card,player)
    elif(isinstance(case,Crous)):
        own_Crous(player,case)
    elif(isinstance(case,Company)):
        own_company(player,case,dice)
    elif(isinstance(case,Case) and case.name=="Musée"):
        print("Nothing happening, have a drink !")
    elif(isinstance(case,Case) and case.name=="fee"):
        player.money-=100





pygame.init()

os.chdir("C:\\Users\\nathan\\Downloads")

#Definition variables
width, height = 900, 900
white = (255,255,255)
black = (0,0,0)
FPS = 20
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









def recognize_piece(piece):
    for i in list_players:
        if(piece.name==i.pieces.name):
            return i


class buttons():
    def __init__(self,x,y,width,height,piece):
        self.rect= pygame.Rect(x,y,width,height)
        self.piece=piece
        self.clicked= False


    def click (self):
        pos = pygame.mouse.get_pos() #position mouse
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and self.clicked==False:
            self.clicked=True
            play=recognize_piece(self.piece)
            e=throw_dice(play)
            return e


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







def throw_dice(player):
    x=random.randint(1,6)
    player.position=player.position+x
    piece=player.pieces
    piece.position+=x
    text_to_throw(piece,x)


    if player.position>39:
        piece.position = piece.position - 40
    if player.position ==0:
        piece.rect.x = case_go.x
        piece.rect.y = case_go.y
    if player.position ==1:
        piece.rect.x = case_brown_1.x
        piece.rect.y = case_go.y
    if player.position ==2:
        piece.rect.x = case_community_chess_1.x
        piece.rect.y = case_go.y
    if player.position==3:
        piece.rect.x = case_brown_2.x
        piece.rect.y = case_go.y
    if player.position==4:
        piece.rect.x = case_income_tax_1.x
        piece.rect.y = case_go.y
    if player.position==5:
        piece.rect.x = case_train_station_1.x
        piece.rect.y = case_go.y
    if player.position==6:
        piece.rect.x = case_light_blue_1.x
        piece.rect.y = case_go.y
    if player.position==7:
        piece.rect.x = case_luck_1.x
        piece.rect.y = case_go.y
    if player.position==8:
        piece.rect.x = case_light_blue_2.x
        piece.rect.y = case_go.y
    if player.position==9:
        piece.rect.x = case_light_blue_3.x
        piece.rect.y = case_go.y
    if player.position==10:
        piece.rect.x = case_jail.x
        piece.rect.y = case_go.y
    if player.position==11:
        piece.rect.x = case_jail.x
        piece.rect.y = case_pink_1.y
    if player.position==12:
        piece.rect.x = case_jail.x
        piece.rect.y = case_electricity.y
    if player.position==13:
        piece.rect.x = case_jail.x
        piece.rect.y = case_pink_2.y
    if player.position==14:
        piece.rect.x = case_jail.x
        piece.rect.y = case_pink_3.y
    if player.position==15:
        piece.rect.x = case_jail.x
        piece.rect.y = case_train_station_2.y
    if player.position==16:
        piece.rect.x = case_jail.x
        piece.rect.y = case_orange_1.y
    if player.position==17:
        piece.rect.x = case_jail.x
        piece.rect.y = case_community_chess_2.y
    if player.position==18:
        piece.rect.x = case_jail.x
        piece.rect.y = case_orange_2.y
    if player.position==19:
        piece.rect.x = case_jail.x
        piece.rect.y = case_orange_3.y
    if player.position==20:
        piece.rect.x = case_jail.x
        piece.rect.y = case_free_parking.y
    if player.position==21:
        piece.rect.x = case_red_1.x
        piece.rect.y = case_free_parking.y
    if player.position==22:
        piece.rect.x = case_luck_2.x
        piece.rect.y = case_free_parking.y
    if player.position==23:
        piece.rect.x = case_red_2.x
        piece.rect.y = case_free_parking.y
    if player.position==24:
        piece.rect.x = case_red_3.x
        piece.rect.y = case_free_parking.y
    if player.position==25:
        piece.rect.x = case_train_station_3.x
        piece.rect.y = case_free_parking.y
    if player.position==26:
        piece.rect.x = case_yellow_1.x
        piece.rect.y = case_free_parking.y
    if player.position==27:
        piece.rect.x = case_yellow_2.x
        piece.rect.y = case_free_parking.y
    if player.position==28:
        piece.rect.x = case_water.x
        piece.rect.y = case_free_parking.y
    if player.position==29:
        piece.rect.x = case_yellow_3.x
        piece.rect.y = case_free_parking.y
    if player.position==30:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_free_parking.y
    if player.position==31:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_green_1.y
    if player.position==32:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_green_2.y
    if player.position==33:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_community_chess_3.y
    if player.position==34:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_green_3.y
    if player.position==35:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_train_station_4.y
    if player.position==36:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_luck_3.y
    if player.position==37:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_dark_blue_1.y
    if player.position==38:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_luxury_tax.y
    if player.position==39:
        piece.rect.x = case_go_to_jail.x
        piece.rect.y = case_dark_blue_2.y
    return x




def main():
    clock =pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_monopoly()
        for i in list_players:
            dice=buttons.click(button_throw_dice_for_car)
            p=recognize_piece(button_throw_dice_for_car.piece)
            play(p,dice)
            buttons.click(button_throw_dice_for_dog)




    pygame.quit()


main()
