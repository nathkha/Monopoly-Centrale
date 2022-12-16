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

    def __init__(self,name,price,index,color,owner,info,house=0,hotel=0):
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

    def __str__(self):
        print("Name: "+self.name+" Dimensions: (x,y)=(",str(self.rect.x)+","+str(self.rect.y)+") "+"(width,height)=( "+str(self.rect.width)+","+str(self.rect.height)+") "+str(self.position))

piece_1 = pieces("car",780,770,80,60,0)
piece_2 = pieces("dog",810,830,80,60,0)

class Players:

    def __init__(player,name,pieces,position, money,properties,jail):
        player.name=name
        player.pieces=pieces
        player.position = position
        player.money = money
        player.properties=properties
        player.jail=jail

    def __strposition__(player): #Giving the position to the players as a number is useless
         return list_cases[player.position].name


    def __str__(player):#Print the information about the player
        print("Name: "+player.name,end="\n")
        player.pieces.__str__()
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
            if(case.colour=="brown" or case.colour=="dark blue"):
                if(player.check_colors(case)==2):
                    print('You can build a house for 100')
                    x=int(input("How many houses do you want ? "))
                    if(100*x>player.money):
                        print("Not enough money for this number of houses, you have ", player.money)
                        x=int(input("How many houses do you want ? "))
                        case.house+=x
                        case.price+=100*x
                        player.money-=100*x
                else:
                    print("Impossible to build a house on this case, you need all the properties of the same colour")
                return
            else:
                if(player.check_colors(case)==3):
                    print('You can build a house for 100')
                    x=int(input("How many houses do you want ? "))
                    if(100*x>player.money):
                        print("Not enough money for this number of houses, you have ", player.money)
                        x=int(input("How many houses do you want ? "))
                        case.house+=x
                        case.price+=100*x
                        player.money-=100*x
                else:
                    print("Impossible to build a house on this case, you need all the properties of the same colour")
                return



    def buy_hotel(player,case):
        if(isinstance(case,Street)):
            if(case.house==4):
                print("You can build hotel")
                x=int(input("Do you want to build a hotel ? "))
                print("1.Yes","2.No",sep="\n")
                if(x==1):
                    if(300<=player.money):
                        case.house=0
                        case.price+=500
                        player.money-=300
                    else:
                        print("Not enough money to buy a hotel")
                else:
                    return
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




playt=Players("john",piece_1,0,2500,[],0)

playt.properties.append(case_1)

playt.properties.append(case_3)

playt2=Players("bob",piece_2,0,2500,[],0)
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
        if(case.house==4):
            player.buy_hotels(case)
        if(b==3):
            print("You can buy accomodations on the case","You have",player.money,"of money")
            player.buy_house(case)
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
    if(player.position<0):
        a = random.randint(1,6)
        b = random.randint(1,6)
        x = a+b
        if(a==b):
            print("You made a double, you're free to go",end=" ")
            print("Value of the dice: ",x)
            player.position = player.position+x
            print(f'{player.shape} moves to {list_cases[repeat_the_index(player)].name}')
            return (a,b)
        else:
            print("Not a double you stay in the musée for ",player.jail,"rounds")
            return (0,0)
    else:
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

def trad_index_to_case(index):
    for i in list_cases:
        if(i.index==index):
            return i

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

def save():
    fic=open("data.txt","w")
    for i in list_players:
        fic.write(i.name+" "+str(i.position)+" "+str(i.money)+" "+str(i.jail)+" ")
        fic.write(i.pieces.name+" "+str(i.pieces.rect.x)+" "+str(i.pieces.rect.y)+" "+str(i.pieces.rect.width)+" "+str(i.pieces.rect.height)+" "+str(i.pieces.position)+" ")
        for j in i.properties:
            fic.write(str(j.index)+" ")
        fic.write("\n")
    fic.close()
save()

def load():
    M=[]
    list_players=[]
    fic=open("data.txt","r")
    lignes=fic.readlines()
    for i in lignes:
        M.append(i.split()) #We then create the players
    for j in range(len(M)):
        properties=[]
        piece=pieces(M[j][4],int(M[j][5]),int(M[j][6]),int(M[j][7]),int(M[j][8]),int(M[j][9]))
        h=10
        while (h<len(M[j])):
            case=trad_index_to_case(int(M[j][h]))
            properties.append(case)
            h+=1
        player=Players(M[j][0],piece,int(M[j][1]),int(M[j][2]),properties,int(M[j][3]))
        list_players.append(player)
    return list_players
load()

a=load()