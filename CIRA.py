from pygame import mixer
from time import sleep
import csv
def main():
    name = input("What is your name?: ")
    sleep(1)
    print(f"{name} steps into the Hornblake dungeons, ready to break the curse of CIRA once and for all!")
    sleep(2)
    battle()

def attack(p_poke, o_poke):
    """Deals damages based off of poke stats,
    uses strength() to determine advantage between poke types
    
    Args:
        p_poke: player poke
        o_poke: opponent poke
        
    Returns:
        string reporting attack and (int?/float?) damage value
    """
    starting_power = 1
    p_poke = starting_power
    o_poke = starting_power
    
    

class Poke():        
    """poke object, will be used to make a list of them,
    attacks and its power will be added into a dictionary, eg (attack: power)
    three types: fire, water, magic
    water crits fire, fire crits magic, magic crits water
    
    Attributes: name, type, atk, hp, def, speed
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
                speed = line[5] #might needed to be changed, unawere of speed in poke csv file
                self.pokemon[line[0]] = atk, hp
    
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
               type = line[2]
               self.item[line[0]] = type, name
    def get_item(self, item_name):
        """Gets item info from catalog and creates item object
        
        Args:
            item_name (str): name of item
        
        Returns:
            Item object    
        """
        for item_name in self.item:
            if item_name[2] == "a":
                return self.item #unaweare exaclty how we wanted to use the items, so this commit is where to change return statements
            if item_name[2] == "d":
                return self.item
            if item_name[2] == "h":
                return self.item
                
        
        
class Item(ItemCatalog):
    """item object
    
    Attributes:
        name (str): name of item
        stat (int): points assigned to item
        type (char): char of a/d/h to denote type
    """
    def __init__(self, name, stat, type):
        self.name = name
        self.stat = stat
        self.type = type
    def advantage(self, item):
        self.item = item
        
        
    
        
    
          
class Player():
    """create player object, given preset poke and item list,
    CPU players will not have items
    """
    def __init__(self, player):
        self.player = player
        
        

def battle():
    # music for final fight
    # may implement switching mechanic
    # party stats resets and hp restores at end of round
    # might level up at end of round
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
    if str(choice) in list:
        print(f"~~> used {choice}!")
        choice_flag = True
        return (choice_flag)
    else:
        print("~~> Pick an option, dingus.")
# def attack(choice, list):
#     if check_select(choice, list, choice_flag=True) is "punch":
        
main()