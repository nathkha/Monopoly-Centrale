# Monopoly-Centrale
To launch the Monopoly, we have to run the game function. 
This function need before several list. 
The list of players created by the list_players function
The list of case, created by ourselves.

Now let's the differents classes, methods and functions we have. 

Class Player:
This class creates a player of the Monopoly
Several parameters: Name, Shape, money, position and the list of properties.

__str__() -> function that will print all the players parameters

Buy_case(player,case) -> function that will alow the player to buy a case, if the player has enough money and if the case is of a good type (Street, Company or Crous)

check_colors(player,case) ->In order to buy a house, we need to have 3 properties of the same colour. This function counts the number of same-colour propertiy we have and return this number 

number_companies(player) ->The rent of a company depends of how many companies the player has. Thus, wee need this number.

buy_house(player,case) -> Permits to a player to build houses on  a property if there is the minimum number of properties of the same coulour required.

mortgage(player) -> When a player runs out of money, to get money back, they can put a mortgage on their properties. This function only triggers when players can't pay another player.

Class Case:
This class is divided into several subclasses 
In general, the class case have several parameters: name,index,info.
We decide to create subclasses because all the classes don't have the same purpose, parameters. 
In Street, we added the rent, number of houses, number of hotels, the color and owner.
In Chance, we can keep the same parameters than Class.

Class Cards: 
The cards correspond to the Chance and Community chest card, each of them are stored in a list. 
The method recognize(card,player), recognize which type of card it is then the action (receive, go or pay) and the amount or the location the player due or have to go. 

To pick a card, we created the function pick_a_random_card. To copy the randomness of the real game, we pick our card randomly through a list.






