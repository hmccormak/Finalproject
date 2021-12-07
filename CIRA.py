from pygame import mixer

from time import sleep

from random import randint

import csv

import pandas as pd

def main():
    """Main function for the codémon game,
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
    ## will move the long text to a file
    cira_blurb = "\nAHAHAAAHAAAHA, DO YOU REALLY THINK YOU CAN DEFEAT ME WITH YOUR SPAGHETTI CODE?\n\nI CAN DESTROY YOUR GRADES IN THE BLINK OF AN EYE!\n\nYOUR PARENTS ARE GONNA FIND A PILE OF ONES AND ZEROS WHEN IM DONE WITH YOU!\n\nTL;DR:\nEAT EXCREMENT BUNDLES OF STICKS"
    cira = Trainer("Cira", cira_blurb)
    cira.add_codé(codédex.get_codé("Gradescope"))
    cira = Trainer("Cira")
    cira.add_codé(codédex.get_codé("Gradescope"))
    sleep(1)
    print(f"{player.name} steps into the Hornblake dungeons, ready to break the curse of CIRA once and for all!")
    sleep(2)
    battle(player, cira, item)


class Trainer():
    """Trainer object for both human and CPU players
    
    Attributes:
        name (string): trainer name
        codé_list (list): list of codé objects
        item_list (list): list of item objects (computer player will likely not use this)
        sel (int): index of codé list for selection
    """
    def __init__(self, name, blurb=""):
        self.name = name
        self.codé_list = []
        self.item_list = []
        self.df = pd.DataFrame()
        self.sel = 0
        self.blurb = blurb
        
    def __repr__(self):
        return (f"{self.item_list}")
    
    def add_codé(self, codé_obj):
        self.codé_list.append(codé_obj)
        
        
    def add_item(self, item_obj):
        self.item_list.append(item_obj)
    def add_df(self, codé_obj):
        self.df.append(codé_obj)


class Codédex():
    """codédex object. Will be used to make a dictionary of codé.
        
    Attributes:
        codédex: Catalog of codé info
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
        """codé object creator
        
        Args:
            req_name: name of desired codé to create
            
        Returns:
            created codé object if req_name has a match"""
    
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
            return "no such Codémon!"


class Codé():
    """Codé object
    
    Attributes:
        name (str): the codé's name
        type (str): the codé's type (water, fire, magic). decides effectiveness of attacks.
        atk (int): the codé's attack stat, used to calculate damage
        hp (int): the codé's hit points, impacted by damage or item
        defense (int): the codé's defense stat, used to calculate damage
        speed (int): the codé's speed stat
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
        # with open(fpath, "w", encoding="utf-8") as wf:
        #     empty_csv = {}
        #     csv_writer = csv.writer(wf)
        #     csv_writer.writerows(empty_csv)
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
            item = Item(item_name, self.itemcat[item_name][0],
                             self.itemcat[item_name][1])
            return (item)


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
        self.stat = int(stat)
        self.type = type
        
    def __repr__(self):
        return (f"{self.name}")
  
    def use_item(self, codé):
        """Adds values to codé stats based off type
        
        Args:
            codé: codé object using item
        
        Side effects:
            adds values to specified codé stats"""
        
        if self.type == "h":
            print()
            sleep(1)
            codé.hp += int(self.stat)
            print(f"Health has increased by {self.stat} to {codé.hp}")
            print()
            sleep(1)
        elif self.type == "a":
            print()
            sleep(1)
            codé.atk + int(self.stat)
            print(f"Attack has increased by {self.stat} to {codé.atk}") 
            print()
            sleep(1)    
        elif self.type == "d":
            print()
            sleep(1)
            codé.defense + int(self.stat)
            print(f"Defense has increased by {self.stat} to {codé.defense}")
            print()
            sleep(1)
           
        else:
            print('something here') #just for testing
            

       
def music_and_blurb(opponent):
    mixer.init()
    mixer.music.load("meg_intro.mp3")
    mixer.music.play()
    print(opponent.blurb)
    sleep(13.5)
    mixer.music.load("meg_loop.mp3")
    mixer.music.play(loops=-1)


def battle(player, opponent, item):
    '''Allows codé to choose an attack or an item.
def battle(player, opponent, item_catalog):
    Allows codé to choose an attack or an item.
    
    Side effects:
        prints "THE FIGHT BEGINS"
        prints opponent's codé name
        prints player's codé name
        prints prompt to choose attack or item or asks the user to choose attack/item
    '''

    #music_and_blurb(opponent)
    
    print("\n\n--++==## THE FIGHT BEGINS ##==++--\n")
    opponent_codé = opponent.codé_list[opponent.sel]
    
    print(f"Your opponent, {opponent.name} sent out {opponent_codé}!\n")
   
    choice = (input(f"<Choose your Codémon!>: {player.codé_list}:"))
    choice_flag = False
    new = [codé.name.lower() for codé in player.codé_list]
    while choice_flag == False:
        if choice.lower() in new:
        
            choice_flag = True
            player_codé = player.codé_list[player.sel] 
            temp_name = repr(player.codé_list[player.sel]) 
            print()
            sleep(1)
            print(f"{player.name} sent out {temp_name}!")
            
            
        else:
            print()
            sleep(1)
            print("~~> You picked a wrong Codémon, dingus.")
            print()                
            sleep(1)
            choice = (input(f"<Choose your Codémon!>: {player.codé_list}:"))
            print(choice)
                             
           
    while opponent.codé_list[opponent.sel].hp > 0 and player.codé_list[player.sel].hp > 0:
        update_stats("codélist.csv", player)
        pandas_table(choice, player)
        print()
        sleep(1)
        a_choice = input("<Attack or Item or Change?>: ")
        if a_choice.lower() == "attack":
            print()
            sleep(1)
            a_choice = input(f"<Select attack>: {player.codé_list[player.sel].atk_list}: ")
            if a_choice.lower() in player.codé_list[player.sel].atk_list:
                print()
                print(f"!!      {choice} attacks {opponent_codé}      !!")
                print(f"!!      {choice} used {a_choice}!       !!")

                attack(player_codé, opponent_codé, a_choice)
                mixer.Channel(1).play(mixer.Sound("Slash.wav"))

                attack(player_codé, opponent_codé, a_choice)

                sleep(2)              
        elif a_choice.lower() == "item":
            i_choice = input(f"<Select item>: {player.item_list}: ")
            i_choice = str(i_choice)
            temp_list = []
            for j in range(len(player.item_list)):
                temp_list.append(player.item_list[j].name)
            choice_flag = bool(check_select(i_choice, temp_list, choice_flag))
            if choice_flag == True:
                for i in range(len(temp_list)):
                    if i_choice == player.item_list[i].name:
                        player.item_list[i].use_item(player_codé)
                        del player.item_list[i]
                        break
                print()
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
            c_choice = input(f"<Choose your Codémon!>: {player.codé_list}:")
            while c_choice:
                if c_choice.lower() == "squittle":
                    print()
                    sleep(1)
                    print(f"!!      {player.name} sent out Squittle!        !!")
                    print()
                    sleep(1)
                    choice = player.codé_list[0]
                    choice.atk_list = [choice.move1, choice.move2]
                    moves = choice.atk_list
                    player_codé = player.codé_list[0]
                    break
                elif c_choice.lower() == "magisaur":
                    print()
                    sleep(1)
                    print(f"!!      {player.name} sent out Magisaur!        !!")
                    print()
                    sleep(1)
                    choice = player.codé_list[1]
                    choice.atk_list = [choice.move1, choice.move2]
                    moves = choice.atk_list
                    player_codé = player.codé_list[1]
                    break
                elif c_choice.lower() == "charmancer":
                    print()
                    sleep(1)
                    print(f"!!      {player.name} sent out Charmancer!      !!")
                    print()
                    sleep(1)
                    choice = player.codé_list[2]
                    choice.atk_list = [choice.move1, choice.move2]
                    moves = choice.atk_list
                    player_codé = player.codé_list[2]
                    break
                else:
                    print()
                    sleep(1)
                    print("~~>  You picked a wrong Codémon, dingus.")
                    print()
                    sleep(1)
                    break 
        else: 
            print()
            sleep(1)
            print("~~>  You picked a wrong choice, dingus.")
            print()
            sleep(1)    

        print(f"{opponent_codé} attacks {player_codé}.") #CPU turn
        CPU_attack = opponent_select(opponent_codé.atk_list)
        attack(opponent_codé, player_codé, CPU_attack)     

            
    if opponent.codé_list[opponent.sel].hp <= 0:
        print(f"{opponent_codé}'s HP is {opponent.codé_list[opponent.sel].hp}.")
        print(f"{player_codé}'s HP is {player.codé_list[player.sel].hp}.")
        print(f"{player.name} wins!")
    elif player.codé_list[player.sel].hp <= 0:
        print(f"{opponent_codé}'s HP is {opponent.codé_list[opponent.sel].hp}.")
        print(f"{player_codé}'s HP is {player.codé_list[player.sel].hp}.")
        print(f"{player_codé} was knocked out... ")
        print()
        sleep(1)
        choice_flag = False 
        while choice_flag == False:
            choice = (input(f"<Choose your Codémon!>: {player.codé_list}:"))
            if choice.lower() == "squittle":
                print()
                sleep(1)
                print(f"{player.name} sent out Squittle!")
                print()
                sleep(1)
                choice = player.codé_list[0]
                choice.atk_list = [choice.move1, choice.move2]
                moves = choice.atk_list
                player_codé = player.codé_list[0]
                break
            elif choice.lower() == "magisaur":
                print()
                sleep(1)
                print(f"{player.name} sent out Magisaur!")
                print()
                sleep(1)
                choice = player.codé_list[1]
                choice.atk_list = [choice.move1, choice.move2]
                moves = choice.atk_list
                player_codé = player.codé_list[1]
                break
            elif choice.lower() == "charmancer":
                print()
                sleep(1)
                print(f"{player.name} sent out Charmancer!")
                print()
                sleep(1)
                choice = player.codé_list[2]
                choice.atk_list = [choice.move1, choice.move2]
                moves = choice.atk_list
                player_codé = player.codé_list[2]
                break
            else:
                print()
                sleep(1)
                print("~~> You picked a wrong codémon, dingus.")
                print()
                sleep(1)             
    else:
        print(f"{opponent_codé}'s HP is {opponent.codé_list[opponent.sel].hp}.")
        print(f"{player_codé}'s HP is {player.codé_list[player.sel].hp}.")
        print(f"DRAW") #just here for testing
    

def update_stats(file, player):
    ''''''
    with open(file, 'r+') as f:
        for line in f:
            if line[0] == player.name:
                line[2] = f.write(player.atk)
                line[3] = f.write(player.hp)
                line[4] = f.write(player.defense)
                line[5] = f.write(player.speed)
def pandas_table(choice, player):
    
    df = pd.read_csv("codélist.csv", names = ['Name', 'Type', 'Attack', 'HP', 'Defense', 'Speed', 'Move1', 'Move2'])
    #need to update CSV file when stats change 
    #https://www.geeksforgeeks.org/how-to-read-csv-file-with-pandas-without-header/
    df = df.iloc[:, 2:5]
        
    if choice == player.codé_list[0]:
        codé_stats = df.loc[[0]]
        codé_stats = codé_stats.to_string(index = False)
        #https://stackoverflow.com/questions/24644656/how-to-print-pandas-dataframe-without-index
    elif choice == player.codé_list[1]:
        codé_stats = df.loc[[1]]
        codé_stats = codé_stats.to_string(index = False)
    elif choice == player.codé_list[2]:
        codé_stats = df.loc[[2]]
        codé_stats = codé_stats.to_string(index = False)
    else:
        codé_stats = df.loc[[3]]
        codé_stats = codé_stats.to_string(index = False)
    print(codé_stats) #replace with return function?

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
        mixer.Channel(1).play(mixer.Sound("Slash.wav"))
        print()
        sleep(1)
        return list[0]
    if attack_selection == 1:
        print()
        sleep(1)
        print(f"~~> used {list[1]}!")
        mixer.Channel(1).play(mixer.Sound("Slash.wav"))
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
        
def attack(p_codé, o_codé, selected_attack):
    """Deals damages based off of codé types and codé stats.
    
    Args:
        p_codé (obj): attacking codé
        o_codé (obj): opposing codé
        selected_attack (string): name of selected attack, determines base strength
    
    Returns:
        o_codé.hp = the opponent codé's modified hp
        
    Side effects:
        prints strings reporting attack and float of damage value
    """
    if selected_attack == p_codé.atk_list[0]:
        starting_power = 10

    elif selected_attack == p_codé.atk_list[1]:
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