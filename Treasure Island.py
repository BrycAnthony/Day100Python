print('''
*******************************************************************************
|                                                                             |
|   |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||   |
|   ||                                                                     ||   |
|   ||                .     .      .      .      .     .                  ||   |
|   ||                   .       .     .       .                         ||   |
|   ||                       .         ^^^^                              ||   |
|   ||                              .  ^^^^^^                            ||   |
|   ||                         .      ^^^^^^^^^                          ||   |
|   ||                               ^^^^^^^^^^^                          ||   |
|   ||                            .   ^^^^^^^^^^^^                        ||   |
|   ||                                 ||  ||  ||                         ||   |
|   ||                                 ||  ||  ||                         ||   |
|   ||                          _______________________                   ||   |
|   ||                       __/_______________________\__                ||   |
|   ||                    __/_____/_____/_____/_____/____\__              ||   |
|   ||                 __/_____/_____/_____/_____/_____/____\__           ||   |
|   ||              __/_____/_____/_____/_____/_____/_____/____\__        ||   |
|   ||           __/_____/_____/_____/_____/_____/_____/_____/____\__     ||   |
|   ||                                                                     ||   |
|   |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||   |
|                                                                             |
*******************************************************************************

''')
print("Welcome To Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direction = input("Type \"left\" or \"right\" ")
print(" ")

if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_Or_Swim = input("Type \"wait\" to wait for the boat, or \"swim\" to swim across. ")
    if wait_Or_Swim == "wait":
        print("You are discoverd by pirates, captured, and drowend.")
    elif wait_Or_Swim == "swim":
        print("You successful swim to the island, but pirate ships are on there way over.")
        print("There is a house with three doors, one red, one yellow, and one blue")
        color_Door = input("Which color door do you choose? \"red\", \"yellow\", or \"blue\". ")
        print(" ")
        if color_Door == "red":
            print("Inside the room you are dropped to the floor and fall in a pit of spikes.")
        elif color_Door == "blue":
            print("Inside the room a trigger goes off the floods the room with water and you drown.")
        elif color_Door == "yellow":
            print("You have found the treasure chest! However, the pirates enter the room shortly after you.")
            print("\"ARRGHH!!! Have you got the treasure chest there lad!?\"")
            print("Will you lie to them, or tell the truth?")
            lie_Or_Truth = input("Type \"lie\" to lie, or \"truth\" to tell the truth. ")

            if lie_Or_Truth == "lie":
                print("You tell the pirates you have the treasure, but it is in the red room.")
                print("\"And how do we know you aren't telling me fib's?")
                print("You can kill me if I am.")
                print("The pirates believe you but falls into the pit of spikes once entering the red room.")
                print("Now the choice is yours. Open the chest for the loot, or leave the island.")
                print(" ")

                open_Or_Leave = input("Type \"open\" to open the chest, or \"leave\" to leave.")
                if open_Or_Leave == "open":
                    print("You win! You opened the treasure chest with excitment... BOOM! The chest was rigged and you blew up. Game Over.")
                elif open_Or_Leave == "leave":
                    print("You neither win nor lose. Unknowingly to you, the chest was rigged and would've exploded. You live to see another day.")
                else:
                    print("You lose for misclicking. Sorry :)")
            elif lie_Or_Truth == "truth":
                print("You point to the treasure chest and tell the pirates it's right there.")
                print("They push you aside and eagerly open it, then... BOOM! The chest was rigged and the pirates blow up.")
                print("However, the explosion revealed the actual treasure hidden under the floor.")
                print("Congragulations! You have lived, and earned the treasure!")
            else:
                print("You lose for misclicking. Sorry :)")
        else:
            print("You lose for misclicking. Sorry :)")
    else:
        print("You lose for misclicking. Sorry :)")
elif direction == "right":
    print("You get shot with a musket by a pirate. Game over.")
else:
    print("You lose for misclicking. Sorry :)")