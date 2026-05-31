### GAME SCREENS ###
####################

screen mapUI():
    add "mapbg"
    tag menu
    modal True

    
    imagebutton auto "mapssection10_%s":
        focus_mask True
        action Jump ("graveyard_10")
    
    imagebutton auto "mapssection2_%s":
        focus_mask True
        action Jump ("graveyard_2")
    
    imagebutton auto "mapssection3_%s":
        focus_mask True
        action Jump ("graveyard_3")

    imagebutton auto "mapssection4_%s":
        focus_mask True
        action Jump ("graveyard_4")

    imagebutton auto "mapssection5_%s":
        focus_mask True
        action Jump ("graveyard_5")

    imagebutton auto "mapssection7_%s":
        focus_mask True
        action Jump ("graveyard_7")

    imagebutton auto "mapssection8_%s":
        focus_mask True
        action Jump ("graveyard_8")

    imagebutton auto "mapssection9_%s":
        focus_mask True
        action Jump ("graveyard_9")



screen graveyard_gates():
    tag gravmenu
    add "graveyard_gates"
    modal True

    imagebutton auto "mapstand_%s":
        focus_mask True
        action Jump ("intro_map")

    imagebutton auto "vaivaisukko_%s":
        focus_mask True
        action Jump ("vaivaisukko")

screen graveyard_section1():
    tag gravmenu
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
    tag gravmenu
    add "section2"
    modal True

  
    imagebutton auto "map_icon_%s":
        focus_mask True
        action ShowMenu("mapUI")
   
    imagebutton auto "graveyard_2_grave1_%s":
        focus_mask True
        action Jump ("Maija_Petri_grave")

    imagebutton auto "graveyard_2_grave2_%s":
        focus_mask True
        action Jump ("Riitta_grave")

    imagebutton auto "graveyard_2_grave3_%s":
        focus_mask True
        action Jump ("placeholder_grave")


screen graveyard_section3():
    tag gravmenu
    add "section3"
    modal True

    imagebutton auto "map_icon_%s":
        focus_mask True
        action ShowMenu("mapUI")
   
    imagebutton auto "graveyard_3_grave1_%s":
        focus_mask True
        action Jump ("Signe_grave")

    imagebutton auto "graveyard_3_grave2_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "graveyard_3_grave3_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "graveyard_3_grave4_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "graveyard_3_grave5_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "graveyard_3_grave6_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "graveyard_3_grave7_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "graveyard_3_grave8_%s":
        focus_mask True
        action Jump ("placeholder_grave")

    imagebutton auto "graveyard_3_grave9_%s":
        focus_mask True
        action Jump ("placeholder_grave")