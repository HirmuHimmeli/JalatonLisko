# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
default value = 0

# The game starts here.

label start:
    "How much value would you like to have?"

    menu:
        "1":
            $ value += 1
            "Now there's one value."

        "2":
            $ value += 2
            "Now there's two."

        "3":
            $ value += 3
            "Now there's three."

    jump matching_test

label matching_test:
    "How much value did I have again?"
    python:
        match value:
            case 1:
                return "One!"
            
            case 2:
                return "Two"
            case 3:
                return "THree"

            case _:
                "No clue."
label One:
    "ONE!"

label Two:
    "TWO!"

label Three:
    "THREE!"
return
