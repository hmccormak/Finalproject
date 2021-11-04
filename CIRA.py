# BATTLE FUNCTION DRAFT

from pygame import mixer

mixer.init()
mixer.music.load("MEGALOVANIA.mp3")
mixer.music.play()

atk_list = ["punch", "kick"]
item_list = ["brain food lunch", "rare candy"]

choice1_flag = False
while choice1_flag == False:
    choice1 = input("Attack or Item?: ")
    if choice1.lower() == "attack":
        atk_flag = False
        while atk_flag == False:
            a_choice = input(f"select attack: {atk_list}: ")
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
            i_choice = input(f"select item: {item_list}: ")
            if i_choice in item_list:
                # use_item(i_choice)
                print("used item")
                item_flag = True
            else:
                print("pick an option, pingas")
        choice1_flag = True
    else:
        print("pick an option, dingus")