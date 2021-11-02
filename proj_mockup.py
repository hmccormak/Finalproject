def main(player_name, opponents_file):
    ## Create a player object, with a dictionary of pokes.
    ## Create a list of opponents, not sure how many.
    ## Battle will start, and the game will end or continue depending on
    ## what it returns.
    
def attack(attack_name):
    ## returns attack values based off of poke stats and types
    
def useItem(item_name):
    ## regains health or boosts stats based off of specificed item
    ## returns item value and code (to differentiate between hp and stat boost)
    
def switch(poke_name):
    ## switch out current poke for another
    
def take(poke_take, poke_drop):
    ## take poke from losing opponent, drops selected player poke
    
def battle(self, opponent):
    # maybe move this to main
    # print(f"Challenger {opponent.name} approaches!")
    # op_poke = opponent.pokelist[0]
    # print(f"{opponent.name} sent out {op_poke}")
    # p_poke = self.pokelist[0]
    # print(f"Go, sent out {p_poke}!")
    
    end_flag = 0
    while end_flag == 0:
        if p_poke.speed > op_poke:
            print("attack | item")
            input("make a selection")
            ## etc, make attack or use item
            if op_poke.hp <= 0:
                end_flag = 1
        else:
            op_poke.attack(atk)
            print(f"opponent used {atk}!")
            if poke.hp > 0:
                print("attack | item")
                input("make a selection")
                ## etc, make attack or use item
                if op_poke.hp <= 0:
                    end_flag = 1
            else:
                end_flag == 2
    if end_flag == 1:
        print("you win")
        op_list.pop()
        opponent == op_list[0]
    if end_flag == 0:
        print("you lose")
        sys.exit()