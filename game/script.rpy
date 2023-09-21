# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    # Check for file content to go to secret ending
    # need to enter A in key generated file to trigger secret
    $ keyCheck = CheckTextInFile("key.txt", "A")
    if persistent.bond == True and keyCheck:
        jump secret
    else:
        call chapter1
    # need clue 0 & 1 to unlock secret
    if clue1 == True:
        jump goodEnd
    elif clue0 == True and clue1 == False:
        jump badEnd
    else:
        jump defaultEnd



label secretUnlock:
    e "This is a secret unlock."
    e "Secret path unlocked."
    # set unlock condition for secret path
    $ persistent.bond = True
    python:
        MakeTextFile("key.txt", "")
    return

label secret:
    scene bg room
    show eileen happy
    e "This is a secret scene."
    e "gg."
    #end the game here
    return

label defaultEnd:
    scene bg room
    show eileen sad
    e "Default End"
    # This ends the game.
    return

label goodEnd:
    scene bg room
    show eileen love
    e "Good End"
    if clue0 == True:
        call secretUnlock
    # This ends the game.
    return

label badEnd:
    scene bg room
    show eileen sad
    e "bad End"
    # This ends the game.
    return