import random

class Die(object):
    def __init__(self, init_sides=6):
        self.face = random.randint(1,init_sides)
        self.sides = init_sides

    def roll(self):
        self.face = random.randint(1,self.sides)
        return self

    def get_face(self):
        return self.face

class Dice(object):
    def __init__(self, number=5):
        self.dice = []

        for i in range( number ):
            self.dice.append( Die() )

    def reroll(self, die_num):
        self.dice[die_num] = self.dice[die_num].roll()

    def show(self):
        die_num = 0
        for die in self.dice:
            print(str(die_num)+"  ",end="")
            die_num += 1
        print ("")

        for die in self.dice:
            print (str(die.get_face())+"  ",end="")
        print ("")
        print ("")

###########

# Roll all the dice

num_die = 5

valid_dice = range(num_die)

hand = Dice(num_die)

print ("Initial roll is:")
hand.show()

still_roll = True
num_roll = 1

while still_roll:
    all_reroll=""
    not_valid_reroll = True
    while not_valid_reroll:
        reroll_list = input( "Which die/dice do you want to reroll? ")
        if reroll_list == "":
            still_roll = False
            break

        for reroll_die in reroll_list:
            if int(reroll_die) not in valid_dice:
                print("Invalid die "+reroll_die+" - needs to be in "
                        +str(list(valid_dice)))
                break
        else:
            not_valid_reroll = False

    for reroll_die in reroll_list:
        #reroll_int = int(reroll)
        #print("reroll is "+str(reroll)+ " type "+str(type(reroll)))
        hand.reroll(int(reroll_die))

    print ("After re-rolling: " + reroll_list)
    hand.show()

    # Show the hand
    # Roll the requested dice

    num_roll += 1

    if num_roll > 2:
        still_roll = False
