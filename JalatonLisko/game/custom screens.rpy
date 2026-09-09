### GAME SCREENS ###
####################

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

    imagebutton auto "graveyard_1_grave1_%s":
        focus_mask True
        action Jump ("Maija_Petri_grave")

    imagebutton auto "hautayksi_%s":
        focus_mask True
        action Jump ("TapaniKaarina_grave")

screen graveyard_section2():
    tag gravmenu
    add "section2"
    modal True
   
    imagebutton auto "graveyard_2_grave1_%s":
        focus_mask True
        action Jump ("Riitta_grave")

    imagebutton auto "graveyard_2_grave2_%s":
        focus_mask True
        action Jump ("placeholder_grave_2")

    imagebutton auto "graveyard_2_grave3_%s":
        focus_mask True
        action Jump ("placeholder_grave_3")


screen graveyard_section3():
    tag gravmenu
    add "section3"
    modal True

   
    imagebutton auto "graveyard_3_grave1_%s":
        focus_mask True
        action Jump ("Signe_grave")

    imagebutton auto "graveyard_3_grave2_%s":
        focus_mask True
        action Jump ("ph32")

    imagebutton auto "graveyard_3_grave3_%s":
        focus_mask True
        action Jump ("ph33")

    imagebutton auto "graveyard_3_grave4_%s":
        focus_mask True
        action Jump ("ph34")

    imagebutton auto "graveyard_3_grave5_%s":
        focus_mask True
        action Jump ("ph35")

    imagebutton auto "graveyard_3_grave6_%s":
        focus_mask True
        action Jump ("ph36")

    imagebutton auto "graveyard_3_grave7_%s":
        focus_mask True
        action Jump ("Toivo_grave")

    imagebutton auto "graveyard_3_grave8_%s":
        focus_mask True
        action Jump ("ph38")

    imagebutton auto "graveyard_3_grave9_%s":
        focus_mask True
        action Jump ("ph39")