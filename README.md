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


