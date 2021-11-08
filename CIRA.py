from pygame import mixer

#def main():
    # controls whole game, ask for players name,
    # goes through battles, (player stats reset and end of match?)

def attack():
    """Deals damages based off of poke stats,
    uses strength() to determine advantage between poke types
    
    Args:
        p_poke: player poke
        o_poke: opponent poke
        
    Returns:
        (int?/float?) of damage value
    """

class poke():        
    """poke object, will be used to make a list of them,
    attacks and its power will be added into a dictionary, eg (attack: power)
    three types: fire, water, magic
    water crits fire, fire crits magic, magic crits water
    
    Attributes: name, type, atk, hp, def, speed
    """
    
class itemCatalog():
    """Creates dictionary of items from csv file, items can either heal
    or boost attack/defense. Item name will be the key, its value and it's
    a/d/h label will be in a tuple
    
    Attributes:
        items: dictionary of items  
    """
    def get_item():
        """Gets item info from catalog and creates item object
        
        Args:
            name (str): name of item
        
        Returns:
            Item object    
        """

class Player():
    """create player object, given preset poke and item list,
    CPU players will not have items
    """

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
    
    print("\n\n\n\n\n\n\n\n\n\n--++==## THE FIGHT BEGINS ##==++--\n")
    
    print(f"opponent_name sends out op_poke_name!\n")
    print(f"player_name sends out poke_name!\n")

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
        
battle()