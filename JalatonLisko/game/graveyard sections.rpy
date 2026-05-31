####This is for all the point and click sections###
###################################################

label graveyard_1:
    scene section1
    call screen graveyard_section1

    label placeholder_grave:
    "This is a placeholder."
    #Jos halutaan paljon feikkihautoja eikä haluta koodata jokaista hautaa erikseen
    #Niin pitää tehdä joku player location funktio. Mut honestly whos gonna check
    jump graveyard_1

    label TapaniKaarina_grave:
    "Not yet."
    jump graveyard_1

    
label graveyard_2:
    scene section2
    "This is a graveyard 2"
    "There are some placeholders to click."
    call screen graveyard_section2

label graveyard_3:
    scene section3
    "This is section 3."
    "There are some more placeholders to click."
    call screen graveyard_section3



label graveyard_4:
    "This is a graveyard 4"
    return
label graveyard_5:
    "This is a graveyard 5"
    return
label graveyard_7:
    "This is a graveyard 7"
    return
label graveyard_8:
    "This is a graveyard 8"
    return
label graveyard_9:
    "This is a graveyard 9"
    return
label graveyard_10:
    "This is a graveyard 10"
    return
