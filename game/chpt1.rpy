
label chapter1:
    scene bg room
    show eileen happy
    # These display lines of dialogue.

    e "This is a normal chapter"

    menu: 
        "Choose 1"
        "Clue0":
            call altPath0
        "Clue1":
            call altPath1

    e "ok"

    menu: 
        "Choose 1 again"
        "Clue0":
            call altPath0
        "Clue1":
            call altPath1

    e "okay"
    # back to start
    return

label altPath0:
    e "This is an alternative path."
    e "You have obtained clue 0"
    $ clue0 = True
    return

label altPath1:
    e "This is an alternative path."
    e "You have obtained clue 1"
    $ clue1 = True
    return

