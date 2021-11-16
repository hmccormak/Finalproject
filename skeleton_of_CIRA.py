from pygame import mixer
from time import sleep
import csv
def main():
    """Main function for the pokemon game"""
    name = input("What is your name?: ")
    sleep(1)
    print(f"{name} steps into the Hornblake dungeons, ready to break the curse of CIRA once and for all!")
    sleep(2)
    battle()

class Poke():        
    """Poke object. Will be used to make a dictionary of poke.
        
    Attributes: 
        name (str): the poke's name
        type (str): the poke's type (water, fire, magic). decides effectiveness of attacks.
        atk (float): the poke's attack stat, used to calculate damage
        hp (float): the poke's hit points, impacted by damage or item
        defense (float): the poke's defense stat, used to calculate damage
        speed (float): the poke's speed stat
    """
    def __init__(self, fpath):
        with open(fpath, "r", encoding="utf-8")as f:
            self.pokemon = {}
            line = csv.reader(f)
            for line in f:
                name = line[0]
                type = line[1]
                atk = line[2]
                hp = line[3]
                deffense = line[4]
                speed = line[5] #might needed to be changed, unaware of speed in poke csv file
                self.pokemon[name] = type, atk, hp, deffense, speed
    
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
            self.item = {}
            line = csv.reader(f)
            for line in f:
               name = line[0]
               points = line[1]
               type = line[2]
               self.item[name] = points, type
    
    def get_item(self, item_name):
        """Gets item info from catalog and creates item object
        
        Args:
            item_name (str): name of item
        
        Returns:
            self.item is populated with item    
        """
        for item_name in self.item:
            if item_name[2] == "a":
                return self.item
            if item_name[2] == "d":
                return self.item
            if item_name[2] == "h":
                return self.item
                
        
        
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
    def inventory(self, item):
        """Method that determines how the items help the player"""
        inventory = ItemCatalog(item)    
            
        for item in inventory:
            if item[2] == "a":
                Poke.atk + item[1] 
            if item[2] == "d":
                Poke.defense + item[1]
            if item[2] == "h":
                Poke.hp + item[1]
def battle():
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

    atk_list = ["punch", "kick"]
    item_list = ["brain food lunch", "rare candy"]
    
    print("\n\n--++==## THE FIGHT BEGINS ##==++--\n")
    
    print(f"opponent sends out op_poke_name!\n")
    print(f"Player sends out poke_name!\n")

    choice_flag = False
    while choice_flag == False:
        choice = input("<Attack or Item?>: ")
        if choice.lower() == "attack":
            a_choice = input(f"<Select item>: {atk_list}: ")
            
                
            choice_flag = bool(check_select(a_choice, atk_list, choice_flag))
        elif choice.lower() == "item":
            i_choice = input(f"<Select item>: {item_list}: ")
            choice_flag = bool(check_select(i_choice, item_list, choice_flag))
        else:
            print("~~> Pick an option, dingus.")

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
        
def attack(p_poke, o_poke):
    """Deals damages based off of poke types and poke stats.
    
    Args:
        p_poke: player poke
        o_poke: opponent poke
    
    Returns:
        o_poke.hp = the opponent poke's modified hp
        
    Side effects:
        prints strings reporting attack and float of damage value
    """
    starting_power = 10
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
