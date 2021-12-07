from pygame import mixer

from time import sleep

from random import randint

import csv

import pandas as pd

def main():
    """Main function for the pokemon game,
    please don't sue us, nintendo"""
    pokedex = Pokedex("pokelist.csv")
    item_catalog = ItemCatalog("itemlist.csv")
    player = (input("What is your name?: "))
    player = Trainer(player)
    player.add_poke(pokedex.get_poke("Squittle"))    
    player.add_poke(pokedex.get_poke("Magisaur"))
    player.add_poke(pokedex.get_poke("Charmancer"))
    player.add_item(item_catalog.get_item("stamp-fil-a"))
    player.add_item(item_catalog.get_item("gallon of coffee"))
    player.add_item(item_catalog.get_item("the best deffense"))
    cira = Trainer("Cira")
    cira.add_poke(pokedex.get_poke("Gradescope"))
    sleep(1)
    print(f"{player.name} steps into the Hornblake dungeons, ready to break the curse of CIRA once and for all!")
    sleep(2)
    battle(player, cira, item_catalog)


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
        self.df = pd.DataFrame()
        
        self.sel = 0
        
    def __repr__(self):
        return (f"{self.item_list}")
    
    def add_poke(self, poke_obj):
        self.poke_list.append(poke_obj)
        
        
    def add_item(self, item_obj):
        self.item_list.append(item_obj)
    def add_df(self, poke_obj):
        self.df.append(poke_obj)


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
                self.pokedex[name] = (type, atk, hp, int(defense), speed, move1, move2)
        
            
                
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
        self.atk = int(atk)
        self.hp = int(hp)
        self.defense = int(defense)
        self.speed = int(speed)
        self.move1 = move1
        self.move2 = move2
        self.atk_list = [self.move1, self.move2]
        
    def __repr__(self):
        return (f"{self.name}")

        
class ItemCatalog():
    """Creates dictionary of items from csv file, items can either heal
    or boost attack/defense. Item name will be the key, its value and it's
    a/d/h label will be in a tuple
    
    Attributes:
        itemcat: dictionary of items  
    """
    def __init__(self, fpath):
        """Method that opens a csv file and catergorizes the items by its name,
        stat and type of item

        Args:
            fpath (string): the path to the csv file
            
        Side effects:
            self.item is populated with items in csv file
        """
        with open(fpath, "w", encoding="utf-8") as wf:
            empty_csv = {}
            csv_writer = csv.writer(wf)
            csv_writer.writerows(empty_csv)
        with open(fpath, "r", encoding="utf-8") as f:
            self.itemcat = {}
            reader = csv.reader(f)
            for line in reader:
               self.name = line[0]
               self.points = line[1]
               self.type = line[2]
               self.itemcat[self.name] = (self.points, self.type)
            
               

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
            return (f"{item_name}")
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
        
    def __repr__(self):
        return (f"{self.name}")
  
    def use_item(self, poke):
        """Adds values to poke stats based off type
        
        Args:
            poke: poke object using item
        
        Side effects:
            adds values to specified poke stats"""
        
        if self.type == "h":
            poke.hp += int(self.stat)
            print(f"Health has increased by {self.stat} to {poke.hp}")
        elif self.type == "a":
            poke.atk + int(self.stat)
            print(f"Attack has increased by {self.stat} to {poke.atk}")     
        elif self.type == "d":
            poke.defense + int(self.stat)
            print(f"Defense has increased by {self.stat} to {poke.defense}")
           
        else:
            print('something here') #just for testing
            

def battle(player, opponent, item_catalog):
    '''Allows poke to choose an attack or an item.
    
    Side effects:
        prints "THE FIGHT BEGINS"
        prints opponent's poke name
        prints player's poke name
        prints prompt to choose attack or item or asks the user to choose attack/item
    '''
        
    # mixer.init()
    # mixer.music.load("MEGALOVANIA.mp3")
    # mixer.music.play(loops=-1)
    
    print("\n\n--++==## THE FIGHT BEGINS ##==++--\n")
    opponent_poke = opponent.poke_list[opponent.sel]
    
    print(f"Your opponent, {opponent.name} sent out {opponent_poke}!\n")
    choice_flag = False 
    while choice_flag == False:
        choice = (input(f"<Choose your Pokemon!>: {player.poke_list}:"))
        if choice.lower() == "squittle":
            print()
            sleep(1)
            print(f"{player.name} sent out Squittle!")
            print()
            sleep(1)
            choice = player.poke_list[0]
            choice.atk_list = [choice.move1, choice.move2]
            moves = choice.atk_list
            player_poke = player.poke_list[0]
            break
        elif choice.lower() == "magisaur":
            print()
            sleep(1)
            print(f"{player.name} sent out Magisaur!")
            print()
            sleep(1)
            choice = player.poke_list[1]
            choice.atk_list = [choice.move1, choice.move2]
            moves = choice.atk_list
            player_poke = player.poke_list[1]
            break
        elif choice.lower() == "charmancer":
            print()
            sleep(1)
            print(f"{player.name} sent out Charmancer!")
            print()
            sleep(1)
            choice = player.poke_list[2]
            choice.atk_list = [choice.move1, choice.move2]
            moves = choice.atk_list
            player_poke = player.poke_list[2]
            break
        else:
            print()
            sleep(1)
            print("~~> You picked a wrong pokemon, dingus.")
            print()
            sleep(1)             
           
    df = pd.read_csv("pokelist.csv", names = ['Name', 'Type', 'Attack', 'HP', 'Defense', 'Speed', 'Move1', 'Move2'])
    #need to update CSV file when stats change 
    #https://www.geeksforgeeks.org/how-to-read-csv-file-with-pandas-without-header/
    df = df.iloc[:, 2:5]    
    while opponent.poke_list[opponent.sel].hp > 0 and player.poke_list[player.sel].hp > 0:
        if choice == player.poke_list[0]:
            poke_stats = df.loc[[0]]
            poke_stats = poke_stats.to_string(index = False)
            #https://stackoverflow.com/questions/24644656/how-to-print-pandas-dataframe-without-index
        elif choice == player.poke_list[1]:
            poke_stats = df.loc[[1]]
            poke_stats = poke_stats.to_string(index = False)
        elif choice == player.poke_list[2]:
            poke_stats = df.loc[[2]]
            poke_stats = poke_stats.to_string(index = False)
        else:
            poke_stats = df.loc[[3]]
            poke_stats = poke_stats.to_string(index = False)
        print(poke_stats) #replace with return function?
        
        a_choice = input("<Attack or Item or Change?>: ")
        if a_choice.lower() == "attack":
            a_choice = input(f"<Select attack>: {choice.atk_list}: ")
            if a_choice.lower() in moves[0] or a_choice in moves[1]:
                print()
                print(f"!!      {choice} attacks {opponent_poke}      !!")
                print(f"!!      {choice} used {a_choice}!       !!")
                attack(player_poke, opponent_poke, a_choice)
                sleep(2)              
        elif a_choice.lower() == "item":
            print()
            sleep(1)
            i_choice = input(f"<Select item>: {player.item_list}: ")
            if i_choice.lower() in player.item_list:
                print()
                sleep(1)
                print(f"!!      {player.name} uses {i_choice}!      !!")
                print()
                sleep(1)
                if i_choice.lower() in item_catalog.itemcat:
                    
                    print()
                    result = item_catalog.itemcat.get(i_choice)
                   
                    if result[1] == "h":
                        Item(i_choice, result[0], result[1]).use_item(player_poke)
                    if result[1] == "a":
                        Item(i_choice, result[0], result[1]).use_item(player_poke)
                    if result[1] == "d":
                        Item(i_choice, result[0], result[1]).use_item(player_poke)

            else:
                print()
                sleep(1)
                print("~~>  You picked a wrong choice, dingus.")
                print()
                sleep(1)                
        elif a_choice.lower() == "change":
            print()
            sleep(1)
            print(f"        {player.name} decides its enough for {choice}!      ")
            print()
            c_choice = input(f"<Choose your Pokemon!>: {player.poke_list}:")
            while c_choice:
                if c_choice.lower() == "squittle":
                    print()
                    sleep(1)
                    print(f"!!      {player.name} sent out Squittle!        !!")
                    print()
                    sleep(1)
                    choice = player.poke_list[0]
                    choice.atk_list = [choice.move1, choice.move2]
                    moves = choice.atk_list
                    player_poke = player.poke_list[0]
                    break
                elif c_choice.lower() == "magisaur":
                    print()
                    sleep(1)
                    print(f"!!      {player.name} sent out Magisaur!        !!")
                    print()
                    sleep(1)
                    choice = player.poke_list[1]
                    choice.atk_list = [choice.move1, choice.move2]
                    moves = choice.atk_list
                    player_poke = player.poke_list[1]
                    break
                elif c_choice.lower() == "charmancer":
                    print()
                    sleep(1)
                    print(f"!!      {player.name} sent out Charmancer!      !!")
                    print()
                    sleep(1)
                    choice = player.poke_list[2]
                    choice.atk_list = [choice.move1, choice.move2]
                    moves = choice.atk_list
                    player_poke = player.poke_list[2]
                    break
                else:
                    print()
                    sleep(1)
                    print("~~>  You picked a wrong pokemon, dingus.")
                    print()
                    sleep(1)
                    break      
        print(f"{opponent_poke} attacks {player_poke}.") #CPU turn
        CPU_attack = opponent_select(opponent_poke.atk_list)
        attack(opponent_poke, player_poke, CPU_attack)    
            
    if opponent.poke_list[opponent.sel].hp < 0:
        print(f"{opponent_poke}'s HP is {opponent.poke_list[opponent.sel].hp}.")
        print(f"{player_poke}'s HP is {player.poke_list[player.sel].hp}.")
        print(f"{player.name} wins!")
    elif player.poke_list[player.sel].hp < 0:
            #something here to switch out pokemon and continue battle
        print(f"{opponent_poke}'s HP is {opponent.poke_list[opponent.sel].hp}.")
        print(f"{player_poke}'s HP is {player.poke_list[player.sel].hp}.")
        print(f"{player_poke} was knocked out... ")
        print()
        sleep(1)
        choice_flag = False 
        while choice_flag == False:
            choice = (input(f"<Choose your Pokemon!>: {player.poke_list}:"))
            if choice.lower() == "squittle":
                print()
                sleep(1)
                print(f"{player.name} sent out Squittle!")
                print()
                sleep(1)
                choice = player.poke_list[0]
                choice.atk_list = [choice.move1, choice.move2]
                moves = choice.atk_list
                player_poke = player.poke_list[0]
                break
            elif choice.lower() == "magisaur":
                print()
                sleep(1)
                print(f"{player.name} sent out Magisaur!")
                print()
                sleep(1)
                choice = player.poke_list[1]
                choice.atk_list = [choice.move1, choice.move2]
                moves = choice.atk_list
                player_poke = player.poke_list[1]
                break
            elif choice.lower() == "charmancer":
                print()
                sleep(1)
                print(f"{player.name} sent out Charmancer!")
                print()
                sleep(1)
                choice = player.poke_list[2]
                choice.atk_list = [choice.move1, choice.move2]
                moves = choice.atk_list
                player_poke = player.poke_list[2]
                break
            else:
                print()
                sleep(1)
                print("~~> You picked a wrong pokemon, dingus.")
                print()
                sleep(1)             
    else:
        print(f"{opponent_poke}'s HP is {opponent.poke_list[opponent.sel].hp}.")
        print(f"{player_poke}'s HP is {player.poke_list[player.sel].hp}.")
        print(f"DRAW") #just here for testing
    

def opponent_select(list):
    '''Attack selection function for CPU player,
    attack is selected at random
    
    Args:
        list: list of attacks
    
    Returns:
        Randomly selected attack'''
    attack_selection = randint(0,1)
    if attack_selection == 0:
        print()
        sleep(1)
        print(f"{list}~~> used {list[0]}!")
        print()
        sleep(1)
        return list[0]
    if attack_selection == 1:
        print()
        sleep(1)
        print(f"~~> used {list[1]}!")
        print()
        sleep(1)
        return list[1]     
            
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
    elif selected_attack == p_poke.atk_list[1]:
        starting_power = 20
    damage = 0
    
    if p_poke.type == "water" and o_poke.type == "fire":
        
        damage = 1.6 * starting_power
        damage_type = "It's super effective!"
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

    print(f"{damage_type}")
    print()
    sleep(1)
    print(f"{o_poke} takes {damage} damage! {o_poke}'s HP is now {o_poke.hp}.")
    print()
    sleep(1)
    return o_poke.hp

        
if __name__ == '__main__':
    main()
