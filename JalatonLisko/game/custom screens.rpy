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
        action Jump ("TapaniKaarina_grave_ph")
    
    imagebutton auto "valac_sec1_%s":
        focus_mask True
        action [SetVariable("player_pos", 1), Jump ("valac_convo")]

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

    imagebutton auto "valac_sec2_%s":
        focus_mask True
        action [SetVariable("player_pos", 2), Jump ("valac_convo")]


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
    
    imagebutton auto "valac_sec3_%s":
        focus_mask True
        action [SetVariable("player_pos", 3), Jump ("valac_convo")]


screen graveyard_section4():
    tag gravmenu
    add "section4"
    modal True

   
    imagebutton auto "graveyard_4_grave_1_%s":
        focus_mask True
        action Jump ("Aarne_grave")

    imagebutton auto "graveyard_4_grave_2_%s":
        focus_mask True
        action Jump ("Signe_I_grave")

    imagebutton auto "graveyard_4_grave_3_%s":
        focus_mask True
        action Jump ("Lennart_grave")

    imagebutton auto "graveyard_4_grave_4_%s":
        focus_mask True
        action Jump ("ph34")

    imagebutton auto "graveyard_4_grave_5_%s":
        focus_mask True
        action Jump ("ph35")

    imagebutton auto "valac_sec4_%s":
        focus_mask True
        action [SetVariable("player_pos", 4), Jump ("valac_convo")]

