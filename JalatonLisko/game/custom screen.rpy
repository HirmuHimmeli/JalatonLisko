### GAME SCREENS ###
####################

screen mapUI():
    add "mapbg"
    tag menu
    modal True

    
    imagebutton auto "mapssection10_%s":
        focus_mask True
        action Call ("graveyard_10")
    
    imagebutton auto "mapssection2_%s":
        focus_mask True
        action Call ("graveyard_2")
    
    imagebutton auto "mapssection3_%s":
        focus_mask True
        action Call ("graveyard_3")

    imagebutton auto "mapssection4_%s":
        focus_mask True
        action Call ("graveyard_4")

    imagebutton auto "mapssection5_%s":
        focus_mask True
        action Call ("graveyard_5")

    imagebutton auto "mapssection7_%s":
        focus_mask True
        action Call ("graveyard_7")

    imagebutton auto "mapssection8_%s":
        focus_mask True
        action Call ("graveyard_8")

    imagebutton auto "mapssection9_%s":
        focus_mask True
        action Call ("graveyard_9")



screen graveyard_gates():
    add "graveyard_gates"
    modal True

    imagebutton auto "mapstand_%s":
        focus_mask True
        action Jump ("intro_map")

    imagebutton auto "vaivaisukko_%s":
        focus_mask True
        action Jump ("vaivaisukko")

screen graveyard_section1():
    add "section1"
    modal True

    imagebutton auto "map_icon_%s":
        focus_mask True
        action ShowMenu("mapUI")

    imagebutton auto "graveyard_1_grave1_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "hautayksi_%s":
        focus_mask True
        action Jump ("TapaniKaarina_grave")

screen graveyard_section2():
    add "section2"
    modal True
  
    imagebutton auto "map_icon_%s":
        focus_mask True
        action ShowMenu("mapUI")
   
    imagebutton auto "graveyard_2_grave1_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "graveyard_2_grave2_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "graveyard_2_grave3_%s":
        focus_mask True
        action Jump ("placeholder_grave")
