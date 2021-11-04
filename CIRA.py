from pygame import mixer

#def main():
    # controls whole game, ask for players name,
    # goes through battles, (player stats reset and end of match?)

#def attack():
    # use attack from list, determine strength from poke stats
    # and opponent stats
    
#def use_item():
    # use item from list, restore hp or boost stat
    # stat boost resets at end of round

#class poke():
    # poke object, will be used to make a list of them
    # Attributes: name, type, atk, hp, def, (guts?)
    # three types: fire, water, magic
    # water crits fire, fire crits magic, magic crits water

#class Player():
    # create player object, given preset poke list
    
# class humanPlayer(Player):
    # inherits player

#class cpuPlayer(Player):
    # inherits player
    # creates opponents, the final boss is called Cira
    # not sure if they should have one or many poke

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

    choice1_flag = False
    while choice1_flag == False:
        choice1 = input("<Attack or Item?>: ")
        if choice1.lower() == "attack":
            atk_flag = False
            while atk_flag == False:
                a_choice = input(f"<Select attack>: {atk_list}: ")
                if a_choice in atk_list:
                    # use_atk(a_choice)
                    print("used attack")
                    atk_flag = True
                else:
                    print("pick an option, weenus")
            choice1_flag = True
        elif choice1.lower() == "item":
            item_flag = False
            while item_flag == False:
                i_choice = input(f"<Select item>: {item_list}: ")
                if i_choice in item_list:
                    # use_item(i_choice)
                    print("used item")
                    item_flag = True
                else:
                    print("pick an option, pingas")
            choice1_flag = True
        else:
            print("pick an option, dingus")

battle()