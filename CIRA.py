from pygame import mixer

from time import sleep

import csv

def main():
    """Main function for the pokemon game,
    please don't sue us, nintendo"""
    pokedex = Pokedex("pokelist.csv")
    item_catalog = ItemCatalog("itemlist.csv")
    player = input("What is your name?: ")
    player = Trainer(player)
    player.add_poke(pokedex.get_poke("Squittle"))
    player.add_poke(pokedex.get_poke("Magisaur"))
    player.add_poke(pokedex.get_poke("Charmancer"))
    player.add_item(item_catalog.get_item("stamp-fil-a"))
    cira = Trainer("Cira")
    cira.add_poke(pokedex.get_poke("Gradescope"))
    sleep(1)
    print(f"{player.name} steps into the Hornblake dungeons, ready to break the curse of CIRA once and for all!")
    sleep(2)
    battle(player, cira)


class Trainer():
    """Trainer object for both human and CPU players
    
    Attributes:
        name (string): trainer name
        poke_list (list): list of poke objects
        item_list (list): list of item objects (computer player will likely not use this)
        sel (int): index of poke list for selection
    """
    def __init__(self, name):
        self.name = name
        self.poke_list = []
        self.item_list = []
        self.sel = 0
        
    def add_poke(self, poke_obj):
        self.poke_list.append(poke_obj)
        
    def add_item(self, item_obj):
        self.item_list.append(item_obj)


class Pokedex():
    """Pokedex object. Will be used to make a dictionary of poke.
        
    Attributes:
        pokedex: Catalog of poke info
    """
    def __init__(self, fpath):
        with open(fpath, "r", encoding="UTF-8") as f:
            self.pokedex = {}
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
                self.pokedex[name] = (type, atk, hp, defense, speed, move1, move2)
                
    def get_poke(self, req_name):
        """Poke object creator
        
        Args:
            req_name: name of desired poke to create
            
        Returns:
            created poke object if req_name has a match"""
        if req_name in self.pokedex:
            req_name = Poke(req_name, 
                            self.pokedex[req_name][0], 
                            self.pokedex[req_name][1], 
                            self.pokedex[req_name][2], 
                            self.pokedex[req_name][3], 
                            self.pokedex[req_name][4],
                            self.pokedex[req_name][5],
                            self.pokedex[req_name][6])
            return req_name
        else:
            return "no such poke!"


class Poke():
    """Poke object
    
    Attributes:
        name (str): the poke's name
        type (str): the poke's type (water, fire, magic). decides effectiveness of attacks.
        atk (int): the poke's attack stat, used to calculate damage
        hp (int): the poke's hit points, impacted by damage or item
        defense (int): the poke's defense stat, used to calculate damage
        speed (int): the poke's speed stat
        atk_list: list of attack names
    """
    def __init__(self, name, type, atk, hp, defense, speed, move1, move2):
        self.name = name
        self.type = type
        self. atk = int(atk)
        self.hp = int(hp)
        self.defense = int(defense)
        self.speed = int(speed)
        self.atk_list = [move1, move2]


class ItemCatalog():
    """Creates dictionary of items from csv file, items can either heal
    or boost attack/defense. Item name will be the key, its value and it's
    a/d/h label will be in a tuple
    
    Attributes:
        item: dictionary of items  
    """
    def __init__(self, fpath):
        """Method that opens a csv file and catergorizes the items by its name,
        stat and type of item

        Args:
            fpath (string): the path to the csv file
            
        Side effects:
            self.item is populated with items in csv file
        """
        with open(fpath, "r", encoding="utf-8") as f:
            self.itemcat = {}
            reader = csv.reader(f)
            for line in reader:
               name = line[0]
               points = line[1]
               type = line[2]
               self.itemcat[name] = (points, type)

    def get_item(self, item_name):
        """Gets item info from catalog and creates item object
        
        Args:
            item_name (str): name of item
        
        Returns:
            self.item is populated with item    
        """
        if item_name in self.itemcat:
            item_name = Item(item_name, self.itemcat[item_name][0],
                             self.itemcat[item_name][1])
            return item_name
        else:
            return "no such item!"


class Item():
    """item object for items in the players inventory
    
    Attributes:
        name (str): name of item
        stat (int): points assigned to item
        type (char): char of a/d/h to denote type
    """
    def __init__(self, name, stat, type):
        """Method that populates the item attributes.
        Args:
            name(string):the name of the item
            stat(int): the amount of points an item aids the player
            type(string): the type of item (attack/deffense/attack)
        Side effects:
            self.name populates with name of item
            self.stat populates the stat of an item
            self.type populates the type of an item
        """
        self.name = name
        self.stat = stat
        self.type = type
        
    def use_item(self, poke):
        """Adds values to poke stats based off type
        
        Args:
            poke: poke object using item
        
        Side effects:
            adds values to specified poke stats"""
        if self.type == "h":
            poke.hp + self.stat
        if self.type == "a":
            poke.atk + self.stat
        if self.type == "d":
            poke.defense + self.stat


def battle(player, opponent):
    '''Allows poke to choose an attack or an item.
    
    Side effects:
        prints "THE FIGHT BEGINS"
        prints opponent's poke name
        prints player's poke name
        prints prompt to choose attack or item or asks the user to choose attack/item
    '''
        
    mixer.init()
    mixer.music.load("MEGALOVANIA.mp3")
    mixer.music.play(loops=-1)
    
    print("\n\n--++==## THE FIGHT BEGINS ##==++--\n")
    
    print(f"opponent sends out {opponent.poke_list[opponent.sel].name}!\n")
    print(f"Player sends out {player.poke_list[player.sel].name}!\n")

    choice_flag = False ## player turn
    while choice_flag == False:
        choice = input("<Attack or Item?>: ")
        if choice.lower() == "attack":
            a_choice = input(f"<Select attack>: {player.poke_list[player.sel].atk_list}: ")
            choice_flag = bool(check_select(a_choice, player.poke_list[player.sel].atk_list, choice_flag))
            if choice_flag == True:
                attack(player.poke_list[player.sel], opponent.poke_list[opponent.sel], a_choice)
        elif choice.lower() == "item":
            i_choice = input(f"<Select item>: {player.item_list}: ")
            choice_flag = bool(check_select(i_choice, player.item_list, choice_flag))
        else:
            print("~~> Pick an option, dingus.")
    
    if opponent.poke_list[opponent.sel].hp <= 0:
        return(f"you win!")
    
    attack(opponent.poke_list[opponent.sel], player.poke_list[player.sel], "docstring error") ## CPU turn
    
    if player.poke_list[player.sel].hp <= 0:
        return(f"you lose!")

def check_select(choice, list, choice_flag):
    '''Identifies the player and opponent's selections.
    
    Args:
        choice (str): the attack or item selection
        battle_list (list): the list of attacks or items
        choice_flag (bool): True or False
        
    Returns:
        choice_flag (bool): True
        
    Side effects:
        prints which item/attack the player chose
        prints a prompt if the player makes the wrong selection'''
        
    if str(choice) in list:
        print(f"~~> used {choice}!")
        choice_flag = True
        return (choice_flag)
    else:
        print("~~> Pick an option, dingus.")
        
def attack(p_poke, o_poke, selected_attack):
    """Deals damages based off of poke types and poke stats.
    
    Args:
        p_poke (obj): attacking poke
        o_poke (obj): opposing poke
        selected_attack (string): name of selected attack, determines base strength
    
    Returns:
        o_poke.hp = the opponent poke's modified hp
        
    Side effects:
        prints strings reporting attack and float of damage value
    """
    if selected_attack == p_poke.atk_list[0]:
        starting_power = 10
    if selected_attack == p_poke.atk_list[1]:
        starting_power = 20
    damage = 0
    
    if p_poke.type == "water" and o_poke.type == "fire":
        damage_type = "It's super effective!"
        damage = 1.6 * starting_power
    elif p_poke.type == "fire" and o_poke.type == "magic":
         damage_type = "It's super effective!"
         damage = 1.6 * starting_power
    elif p_poke.type == "magic" and o_poke.type == "water":
         damage_type = "It's super effective!"
         damage = 1.6 * starting_power
    elif p_poke.type == "fire" and o_poke.type == "water":
        damage_type = "It's not very effective..."
        damage = .625 * starting_power
    elif p_poke.type == "magic" and o_poke.type == "fire":
        damage_type = "It's not very effective..."
        damage = .625 * starting_power
    elif p_poke.type == "water" and o_poke.type == "magic":
        damage_type = "It's not very effective..."
        damage = .625 * starting_power
    else:
        damage_type = ""
        damage = starting_power
        
    damage = damage * (o_poke.defense / p_poke.atk)
    o_poke.hp = o_poke.hp - damage
    
    print(f"{p_poke.name} attacks {o_poke.name}. {damage_type}")
    print (f"{o_poke.name} takes {damage}!!! {o_poke.name}'s hp is now {o_poke.hp}.")
    
    return o_poke.hp
main()
