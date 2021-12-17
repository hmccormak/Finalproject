from pygame import mixer

from time import sleep

from random import randint

import csv

import pandas as pd

def main():
    """Main function for the Codémon game,
    please don't sue us, nintendo"""
    
    codédex = Codédex("codélist.csv")
    item = ItemCatalog("itemlist.csv")
    player = (input("What is your name?: "))

    player = Trainer(player)
    player.add_codé(codédex.get_codé("Squittle"))    
    player.add_codé(codédex.get_codé("Magisaur"))
    player.add_codé(codédex.get_codé("Charmancer"))
    player.add_item(item.get_item("stamp-fil-a"))
    player.add_item(item.get_item("cold pizza"))
    player.add_item(item.get_item("gallon of coffee"))
    player.add_item(item.get_item("the best offense"))
    cira = Trainer("Cira")
    cira.add_codé(codédex.get_codé("Gradescope"))
    sleep(1)
    print(f"{player.name} steps into the Hornblake dungeons, ready to break the curse of CIRA once and for all!")
    sleep(2)
    battle(player, cira)


class Trainer():
    """Trainer object for both human and CPU players.
    
    Attributes:
        name (str): trainer name
        codé_list (list): list of codé objects
        item_list (list): list of item objects (computer player will likely not use this)
        sel (int): index of codé list for selection
        blurb (str): empty string
    """
    def __init__(self, name, blurb=""):
        self.name = name
        self.codé_list = []
        self.item_list = []
        self.sel = 0
        
    def __repr__(self):
        return (f"{self.item_list}")
    
    def add_codé(self, codé_obj):
        self.codé_list.append(codé_obj)
        
    def add_item(self, item_obj):
        self.item_list.append(item_obj)

class Codédex():
    """Codédex object. Will be used to make a dictionary of codé.
        
    Attributes:
        codédex: Dictionary catalog of codé info
    """
    def __init__(self, fpath):
        with open(fpath, "r", encoding="UTF-8") as f:
            self.codédex = {}
            reader = csv.reader(f)
            for line in reader:
                name = line[0]
                type = line[1]
                atk = line[2]
                hp = line[3]
                defense = line[4]
                speed = line[5]
                move1 = line[6]
                move2 = line[7]

                self.codédex[name] = (type, atk, hp, int(defense), speed, move1, move2)
            
    def get_codé(self, req_name):
        """Codé object creator
        
        Args:
            req_name (str): name of desired codé to create
            
        Returns:
            created codé object if req_name has a match
            (str) "No such Codémon" if req_name does not match
        """
    
        if req_name in self.codédex:
            req_name = Codé(req_name, 
                            self.codédex[req_name][0], 
                            self.codédex[req_name][1], 
                            self.codédex[req_name][2], 
                            self.codédex[req_name][3], 
                            self.codédex[req_name][4],
                            self.codédex[req_name][5],
                            self.codédex[req_name][6])
            return req_name
        else:
            return "No such Codémon!"


class Codé():
    """Codé object
    
    Attributes:
        name (str): the codé's name
        type (str): the codé's type (water, fire, magic). decides effectiveness of attacks.
        atk (int): the codé's attack stat, used to calculate damage
        hp (int): the codé's hit points, impacted by damage or item
        defense (int): the codé's defense stat, used to calculate damage
        speed (int): the codé's speed stat
        move1 (str): first move
        move2 (str): second move
        atk_list: list of attack names
    
    Returns:
        f-string of the codé's name
    """
    def __init__(self, name, type, atk, hp, defense, speed, move1, move2):
        self.name = name
        self.type = type
        self.atk = int(atk)
        self.hp = int(hp)
        self.defense = int(defense)
        self.speed = int(speed) #do we need this? not in pandas display
        self.move1 = move1
        self.move2 = move2
        self.atk_list = [self.move1, self.move2]
        
    def __repr__(self):
        return (f"{self.name}")

        
class ItemCatalog():
    """Creates dictionary of items from csv file, items can either heal
    or boost attack/defense. Item name will be the key, its value and it's
    a/d/h label will be in a tuple.
    
    Attributes:
        itemcat: dictionary of items  
    """
    
    def __init__(self, fpath):
        """Method that opens a csv file and catergorizes the items by its name,
        stat and type of item.

        Args:
            fpath (string): the path to the csv file
            
        Side effects:
            self.item is populated with items in csv file
        """
        with open(fpath, "r", encoding="utf-8") as f:
            self.itemcat = {}
            reader = csv.reader(f)
            for line in reader:
               self.name = line[0]
               self.points = line[1]
               self.type = line[2]
               self.itemcat[self.name] = (self.points, self.type)
            
    def get_item(self, item_name):
        """Gets item info from catalog and creates Item object
        
        Args:
            item_name (str): name of item
        
        Returns:
            item (str): the item   
        """
        if item_name in self.itemcat:
            item = Item(item_name, self.itemcat[item_name][0],
                             self.itemcat[item_name][1])
            return (item)


class Item():
    """Item object for items in the players inventory.
    
    Attributes:
        name (str): name of item
        stat (int): points assigned to item
        type (str): str of a/d/h to denote type
    """
    def __init__(self, name, stat, type):
        self.name = name
        self.stat = int(stat)
        self.type = type
        
    def __repr__(self):
        return (f"{self.name}")
  
    def use_item(self, codé):
        """Adds values to codé stats based off type
        
        Args:
            codé: codé object using item
        
        Side effects:
            Alters values to specified codé stat attribute
            Prints empty spaces
            Prints f-string with stat updates
        """
        
        if self.type == "h":
            print()
            sleep(1)
            codé.hp = codé.hp + int(self.stat)
            print(f"Health has increased by {self.stat} to {codé.hp}")
            print()
            sleep(1)
        elif self.type == "a":
            print()
            sleep(1)
            codé.atk = codé.atk + int(self.stat)
            print(f"Attack has increased by {self.stat} to {codé.atk}") 
            print()
            sleep(1)    
        elif self.type == "d":
            print()
            sleep(1)
            codé.defense = codé.defense + int(self.stat)
            print(f"Defense has increased by {self.stat} to {codé.defense}")
            print()
            sleep(1)


def battle(player, opponent):
    '''Allows player to choose an attack, item, or new codé.

    Args:
        player: the player trainer object
        opponent: the opponent trainer object
    
    Side effects:
        prints "THE FIGHT BEGINS"
        prints opponent's codé name
        prints player's codé name
        prints prompt to choose attack or item or asks the user to choose attack/item
        prints player selections
        prints empty lines
        print a result if the player has won, lost, or came to a draw
    '''

    
    print("\n\n--==++## THE FIGHT BEGINS ##++==--\n")
    opponent_codé = opponent.codé_list[opponent.sel]
    
    print(f"Your opponent, {opponent.name} sent out {opponent_codé}!\n")
   
    choice = (input(f"<Choose your Codémon!>: {player.codé_list}:"))
    choice_flag = False
    new = [codé.name.lower() for codé in player.codé_list]
   
    while choice_flag == False:
        if choice.lower() in new:
            choice_flag = True
            for i in range(len(new)):
                if choice.lower() == new[i]:
                    player.sel = i
            player_codé = player.codé_list[player.sel] 
            temp_name = repr(player.codé_list[player.sel]) 
            print()
            sleep(1)
            print(f"{player.name} sent out {temp_name}!")
        else:
            print()
            sleep(1)
            print("~~>  You picked a wrong Codémon, dingus.")
            print()                
            sleep(1)
            choice = (input(f"<Choose your Codémon!>: {player.codé_list}:"))                   
           
    while opponent.codé_list[opponent.sel].hp > 0 and player.codé_list[player.sel].hp > 0:
        choice_flag = False
        pandas_table(choice, player_codé) 
        print()
        
        a_choice = input("<Attack or Item or Change?>: ")
        if a_choice.lower() == "attack":
            attack_flag = False
            choice_flag = True
            while attack_flag == False:
                print()
                sleep(1)
                a_choice = input(f"<Select attack>: {player.codé_list[player.sel].atk_list}: ")
                if a_choice.lower() in player.codé_list[player.sel].atk_list:
                    attack_flag = True
                    print()
                    print(f"{player_codé} attacks {opponent_codé}!")
                    print()
                    sleep(1)
                    print(f"~~>  {player_codé} used {a_choice}!")
                    attack(player_codé, opponent_codé, a_choice)
                    sleep(2)
                else:
                    print()
                    print("Wrong choice")
                    sleep(1)
            
        elif a_choice.lower() == "item":
            item_choice = False
            while item_choice == False:
                i_choice = input(f"<Select item>: {player.item_list}: ")
                i_choice = str(i_choice)
                temp_list = []
                for j in range(len(player.item_list)):
                    temp_list.append(player.item_list[j].name.lower())
                choice_flag = bool(check_select(i_choice, temp_list, choice_flag))
                if choice_flag == True:
                    for i in range(len(temp_list)):
                        if i_choice.lower() == player.item_list[i].name:
                            player.item_list[i].use_item(player_codé)
                            del player.item_list[i]
                            item_choice = True
                            break
                sleep(1)
                if choice_flag == False:
                    print()
                    sleep(1)
                      
                            
        elif a_choice.lower() == "change":
            change_flag = False
            choice_flag = True
            while change_flag == False:
                print()
                sleep(1)
                print(f"{player.name} decides its enough for {player.codé_list[player.sel]}!")
                print()
                c_choice = input(f"<Choose your Codémon!>: {player.codé_list}:")
                temp_list = []
                for i in range(len(player.codé_list)):
                    temp_list.append(player.codé_list[i].name.lower())
                if c_choice.lower() in temp_list:
                    for j in range(len(player.codé_list)):
                        if c_choice.lower() == repr(player.codé_list[j]).lower() and player.codé_list[j].hp > 0:
                            change_flag = True
                            player.sel = j
                            player_codé = player.codé_list[player.sel]
                            print(f"{player.name} sent out {player_codé.name}!\n")
                            break
                        else:
                            print("That codé is out cold!")
                            break
                else:
                    print()
                    sleep(1)
                    print("~~>  You picked a wrong Codémon, dingus.")
                    print()
                    sleep(1) 
        else: 
            print()
            sleep(1)
            print("~~>  You picked a wrong choice, dingus.")
            print()
            sleep(1)

        if opponent_codé.hp > 0 and choice_flag == True:
            print(f"{opponent_codé} attacks {player_codé}.") #CPU turn
            CPU_attack = opponent_select(opponent_codé.atk_list)
            attack(opponent_codé, player_codé, CPU_attack)
            
        
        if player.codé_list[player.sel].hp <= 0:
            fainted_codé = player_codé
            for i in range(len(player.codé_list)):
                if player.codé_list[i].hp > 0:
                    player_codé = player.codé_list[i]
                    player.sel = i
                    print(f"{fainted_codé} was knocked out...")
                    print()
                    sleep(1)
                    print(f"{player.name} sent out {player.codé_list[i]}!")
                    break     

            
    if opponent_codé.hp <= 0:
        print(f"{opponent_codé}'s HP is {opponent_codé.hp}.")
        print(f"{player_codé}'s HP is {player_codé.hp}.")
        print(f"{player.name} wins!")
    elif player.codé.hp <= 0:
        print(f"{opponent_codé}'s HP is {opponent_codé.hp}.")
        print(f"{player_codé}'s HP is {player_codé.hp}.")
        print(f"{player_codé} was knocked out... ")
        print()
        sleep(1)
        print(f"{player.name} lost!")
    

def pandas_table(choice, codé):
    '''Updates the player's codé's stats during battle.
    
    Args:
        choice (str): Codé name
        player (obj): Codé object
    
    Side effects:
        Prints codé's stats
    '''
    
    df = pd.read_csv("codélist.csv", names = ['Name', 'Type', 'Attack', 'HP', 'Defense', 'Speed', 'Move1', 'Move2'])
    #https://www.geeksforgeeks.org/how-to-read-csv-file-with-pandas-without-header/
    df = df.iloc[:, 2:5]
   
    if choice == 'Squittle':
        updated_hp = df.loc[0, 'HP'] = str(codé.hp)
        updated_atk = df.loc[0, 'Attack'] = str(codé.atk)
        updated_defense = df.loc[0, 'Defense'] = str(codé.defense)
        #https://stackoverflow.com/questions/24644656/how-to-print-pandas-dataframe-without-index
        codé_stats = df.loc[[0]]
        codé_stats = codé_stats.to_string(index = False)

    elif choice == "Magisaur":
        updated_hp = df.loc[1, 'HP'] = str(codé.hp)
        updated_atk = df.loc[1, 'Attack'] = str(codé.atk)
        updated_defense = df.loc[1, 'Defense'] = str(codé.defense)
        codé_stats = df.loc[[1]]
        codé_stats = codé_stats.to_string(index = False)
        
    elif choice == "Charmancer":
        updated_hp = df.loc[2, 'HP'] = str(codé.hp)
        updated_atk = df.loc[2, 'Attack'] = str(codé.atk)
        updated_defense = df.loc[2, 'Defense'] = str(codé.defense)
        codé_stats = df.loc[[2]]
        codé_stats = codé_stats.to_string(index = False)
    else:
        updated_hp = df.loc[3, 'HP'] = str(codé.hp)
        updated_atk = df.loc[3, 'Attack'] = str(codé.atk)
        updated_defense = df.loc[3, 'Defense'] = str(codé.defense)
        codé_stats = df.loc[[3]]
        codé_stats = codé_stats.to_string(index = False)
        
    print(f"{codé.name}'s stats:")
    print(codé_stats)

def opponent_select(atk_list):
    '''Attack selection function for CPU player. Attack is selected at random.
    
    Args:
        atk_list: list of attacks
    
    Returns:
        Randomly selected attack from atk_list
    '''
        
    attack_selection = randint(0,1)
    print()
    sleep(1)
    print(f"~~> used {atk_list[attack_selection]}!")
    print()
    sleep(1)
    return atk_list[attack_selection]    
            
def check_select(choice, battle_list, choice_flag):
    '''Identifies the player and opponent's selections.
    
    Args:
        choice (str): the attack or item selection
        battle_list (list): the list of attacks or items
        choice_flag (bool): True or False
        
    Returns:
        choice_flag (bool): True
        
    Side effects:
        prints which item/attack the player chose
        prints a prompt if the player makes the wrong selection
    '''
        
    if str(choice).lower() in battle_list:
        print(f"~~> used {choice}!")
        choice_flag = True
        return (choice_flag)
    else:
        print("~~> Pick an option, dingus.")
        
def attack(p_codé, o_codé, selected_attack):
    """Deals damages based off of codé types and codé stats.
    
    Args:
        p_codé (Codé): attacking codé
        o_codé (Codé): opposing codé
        selected_attack (str): name of selected attack, determines base strength
    
    Returns:
        o_codé.hp (str): the opponent codé's modified hp
        
    Side effects:
        Alters hp attribute of Codé object
        Prints strings reporting attack and float of damage value
    """
    if selected_attack.lower() == p_codé.atk_list[0].lower():
        starting_power = 10

    elif selected_attack.lower() == p_codé.atk_list[1].lower(): #should this elif be an else statement
        starting_power = 20
    
    
    if p_codé.type == "water" and o_codé.type == "fire":
        damage = 1.6 * starting_power
        damage_type = "It's super effective!"
    elif p_codé.type == "fire" and o_codé.type == "magic":
        damage_type = "It's super effective!"
        damage = 1.6 * starting_power
    elif p_codé.type == "magic" and o_codé.type == "water":
        damage_type = "It's super effective!"
        damage = 1.6 * starting_power
    elif p_codé.type == "fire" and o_codé.type == "water":
        damage_type = "It's not very effective..."
        damage = .625 * starting_power
    elif p_codé.type == "magic" and o_codé.type == "fire":
        damage_type = "It's not very effective..."
        damage = .625 * starting_power
    elif p_codé.type == "water" and o_codé.type == "magic":
        damage_type = "It's not very effective..."
        damage = .625 * starting_power
    else:
        damage_type = ""
        damage = starting_power
        
    damage = damage * (o_codé.defense / p_codé.atk)
    o_codé.hp = o_codé.hp - damage

    print(f"{damage_type}")
    print()
    sleep(1)
    print(f"{o_codé} takes {damage} damage! {o_codé}'s HP is now {o_codé.hp}.")
    print()
    sleep(1)
    return o_codé.hp

        
if __name__ == '__main__':
    main()