print("welcome to my first game!")
name = (input("what is your name?"))
age = int(input("how old are you?"))
option = 2
if age >= 18:
    print("you are qualify to play the game!")

    wants_to_play = input("Do you want to play?")
    if wants_to_play == "yes":
        print("you are standing with", option, "option")
        print("lets play!")
        left_or_right = input("first choice...left or right (left/right)?")
        if left_or_right == "left":
            ans = input("nice you followed a path and  you have reached the lake...Do you swim across or go around (across/round)?")
        else:
            print("you have failed")
            lake_or_house = input("second choice...standing or moving (standing/moving)?")
        if standing_or_moving == "moving":
            #  ans = input("you are lost go back...Do you prefer standing or moving (standing/moving)?")
            # elif standing_or_moving == "moving":
         ans = input("you are in the right track...Do you want to continue (yes/no)?")
        print("you have found your place")
    else:
             print("you are confused")

                    


