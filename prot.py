import random as rn
class Fighter():
    def __init__(self, name, health=100, dmg_per_attack=rn.randint(1,30)):
        self.name = name
        self.health = health
        self.dmg = dmg_per_attack
    def __str__(self):
        return "Fighter({},{},{})".format(self.name, self.health, self.dmg)

player1 = Fighter("Rasul")
player2 = Fighter("Aibika")
print(player1.__str__())
print(player2.__str__())

player1 = {
    "name": 'Zero',
    "health": 100,
    "damage": 27
}

player2 = {
    "name": 'Scorpion',
    "health": 120,
    "damage": 25.5
}

player3 = {
    "name": 'Dominator',
    "health": 500,
    "damage": 1.5
}

def who_win(players):
    players = players.copy() # Создаем копию листа чтоб не изменять оригинал
    
    i = 0                     # |
    while len(players) > 1:   # |
        if i >= len(players): # | 
            i = 0             # | -> бесконечно пробегаемся по всем игрокам пока они есть
        
        player = players[i]

        for player2beat in players: # Пробегаемся по всем игрокам
            if player2beat != player: # Если игрок которого не мы сами
                print(f"{player['name']} is attacking a {player2beat['name']}")
                player2beat["health"] -= player["damage"] # Условно атакуем
                print(f"{player2beat['name']} has a {player2beat['health']}HP")
                
                if player2beat["health"] <= 0: # Проверяем на хп жив ли он
                    print(f"{player2beat['name']} is died")
                    players.remove(player2beat) # Убираем его если он сдох
                    i -= 1 # Если игрок сдох то список сдвигается назад ( и это абордажный 
                           #                                                крюк от этого )
        print()
        
        i += 1                # |

    print(f"{players[0]['name']} is win!")

who_win([player1, player2, player3])
