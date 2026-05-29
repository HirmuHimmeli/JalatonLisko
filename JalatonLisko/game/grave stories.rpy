### GRAVE STORIES AND PLOT PROGRESSION ###
##########################################

label Maija_Petri_grave:
    r "Ilvessalo... Maija and Petri."
    r "Are these my grandparents?"
    v "..."
    "Valac reaches out his hand, and twists his fingers in an odd gesture. The leather of his gloves crackles."
    v "Yes, they are."
    v "This Maija, she's part of my bloodline."

    if Riitta_found == True:
        r "So is this Riitta's sister?"
        v "I presume so."
        v "I think we can infer her life wasn't a happy one."

    else:
        pass


    if first_grave == False:
        v "Want to find out what happened?"
        r "Yes. Do your... thing."
        v "Very well. Listen well, and learn."
        v "Have you ever wished to speak with the dead?"
        r "Oh, well I—{nw}"
        v "Dont answer, the dead don't either. They are gone. But even if we don't remember them, the stone does."
        "Valac does something again, hissing strange sounds under his breath and twisting his hand like he's pulling something."
        "Is this...? This is magic! Without a sigil?"
        "I've... I never thought I'd get to see something like this."
        $ first_grave = True
    else:
        pass

    v "Maija Anneli Ilvessalo, neé Wuorenheimo. Born 10th of October 1942, died on the 14th of March 1971."
    v "Her life was unremarkable in many ways, as was she. Despite her odd eyes and the uncanny bumps on her forehead, she lived as she was expected to."
    v "Her parents were loving, as much as they were required to be."
    v "But her small, happy life was not meant to be."
    v "On one fateful day, just as she was beginning to spread her wings and become her own person, discovering who she was,"
    v "she saw her beloved grandfather shoot himself. In front of the whole family."
    v "And the status quo began to quake."
    v "She began pushing. Against others, against society, against herself."
    v "Alcohol soothed and fanned the flames. It became her most long-lasting companion."
    v "Her nights spent in dark parks, alleyways and strangers' homes muffled the sound of her thoughts."
    v "But with time and the incessant, unwanted but unwavering aid of her sister, she began to heal."
    v "She found hope somewhere else other than at the bottom of a bottle. Found a lover and husband, had a child. Tiny, beloved Tapani."
    v "Life was on rails once more."
    v "But then her mother died. And on her deathbed, told her the truth: her father was not her real father. Her sister and her were only half-siblings."
    v "And in a horrible twist of fate, before she could confide in her beloved Riitta about this, she died as well."
    v "And the status quo became irreparable."
    v "Left to mourn two loved ones but months apart, she was sent into a spiral, which swiftly and unfortunately killed her."
    v "Her oldest friend became her undoing."
    v "On an unexpectedly cold winter eve, Maija died at the bottom of a snowy ditch, unconscious, with a bottle still clutched in one frost-bitten hand."
    #CG END + small pause in dialogue
    v "... {p}How undignified.{p=1.0} For a young mother as well."
    $ Maija_found = True
    v "How far they've fallen."

    menu:
        "I don't know how someone could do something like that.":
            $ p_emp += 0
            r "That's awful. Poor dad…"
            r "He can't have been that old when she ended up doing that. I…"
            r "I don't think that's something that can be excused, no matter who you are. And to start doing that, so young…"
            r "What a degrading way to go."
            v "Well, her life was hers to ruin. Who are we to fifty years later condemn her for how badly she fumbled her own existence?"
            r "But you just—!"

        "I won't judge her.":
            $ p_emp += 1
            r "... I don't know. I mean, that's awful."
            r "But I can't imagine what she'd gone through to fall that hard."
            r "Maybe life wasn't as kind to her as you make it seem."
            v "Oh? You think I'm not telling you everything?"
            r "No, it's that —"
            r "There's a lot that happens in life, you know? A million tiny things."
            r "Those tragedies might have been just the tip of the iceberg."
    #label after_menu / en tiedä tarviiko tätä labelii:

    v "Well, no matter. Unto the next one."
    r "Wait, what about her husband?"
    v "He's not part of my bloodline, he's inconsequential. The only thing of import is that he gave you your surname."
    v "Neé Wuorenheimo, was it?"
    if Riitta_found == False:
        r "Might be worth looking for her sister as well, if she's also here."
        v "Do whatever you want. I'm patient if nothing else."
    else:
        pass
    
    call screen graveyard_section2


label Riitta_grave:
    r "Riitta Wuorenheimo..."

    if Maija_found == True:
        r "I think is Maija's sister. My great-aunt?"
        v "Yes. Well, there she is."
        v "Unto the next one?"
        r "What? Don't you want to know what happened to her?"
        v "..."
        v "Why not."
        r "...?"

    else:
        v "... Yes, she's part of the family."
        r "Was she my...grandmother?"
        v "I doubt it. Doesn't share her surname with you, and wasn't buried with her husband, if she had one."
        r "I wonder what happened. She was only... 25?"
        "Just a couple years older than me..."

    if first_grave == False:
        v "Want to find out what happened?"
        r "Yes. Do your... thing."
        v "Very well. Listen well, and learn."
        v "Have you ever wished to speak with the dead?"
        r "Oh, well I—{nw}"
        v "Dont answer, the dead don't either. They are gone. But even if we don't remember them, the stone does."
        "Valac does something again, hissing strange sounds under his breath and twisting his hand like he's pulling something."
        "Is this...? This is magic! Without a sigil?"
        "I've... I never thought I'd get to see something like this."
        $ first_grave = True
    else:
        pass

    v "Riitta Eeva Wuorenheimo, born on the 31st of July 1946, died on the 7th of March 1971."
    v "The younger sister of Maija. Born to a happy couple after the wars of Europe were finally over."
    v "Despite his experiences during the wars, her father was loving beyond measure."
    #Happy portrait of Riitta
    v "The model girl, sweet and kind. Like a doll. Always kind, always quiet. Even when she was bullied for her odd eyes, even when her big sister pulled her hair."
    #Close up of her eye showing Aarne's body
    v "But her screams were the loudest when she saw her grandfather shoot himself, in front of her and the whole family."
    v "She managed to repress those terrible moments, and while her elder sister spiralled, Riitta managed to claw herself back into civility. Despite never marrying, finding the company of men to be not to her liking, she applied herself elsewhere, whenever she could."
    v "She was there to pull her sister out of the dark, back into the light."
    v "And she was there to see the birth of her nephew, Tapani."
    v "After their mother died, her sister spiralled again. She was gone most days, and her husband had grown tired of searching for her time and time again."
    v  "Riitta was there to replace her sister's presence in the life of young Tapani."
    v "One such sunny March day, in lieu of her sister having neglected her duties, Riitta took Tapani on a stroll. They ventured onto the ice of a frozen lake, to look at animal trails in the snow."
    v "It could have been the ice, thinner in that part than others, maybe the sun had shone just a bit too brightly, but the icy veneer of the lake broke underneath Riitta's feet."
    v "The young boy was left scrambling by the edge of the shattered ice to get his aunt out of the freezing water, to no avail."
    v "She couldn't stay afloat. And no one had heard their shouts for help."
    v "Riitta's frozen body was recovered from the icy waters hours later."
    #CGs over
    "..."
    #Rene looks silently horrified because uintitraumat
    $ Riitta_found = True
    r "..."
    v "... Wasn't there a frightening children's show telling people not to walk on weak ice?"
    v "She should have taken its advice."
    r "...?"

    menu:
        "What a cruel thing to say.":
            $ p_emp += 1
            r "How could she have known?"
            r "It sounded like she thought it was safe, if she took dad with her."
            v "People tend to treat death as an unfortunate side effect, instead of an ever-looming threat."
            r "People also fall in the ice every year, sometimes you just can't know these things."
            v "She might still be alive if she'd had just an inkling of basic survival skills."
            #Valac omahyväinen smirk he thinks its funny
            v "... Land of a thousand lakes, and a thousand people who never learned how to swim."
            r "Maybe it wasn't her fault for not learning, if she was never taught."


        "I thought people were smarter back then.":
            $ p_emp -= 1
            "Without really meaning to, I let out a scoff."
            r "... Haven't these things just been common knowledge? Did she even know how to swim?"
            v "She might not have. She might never have needed to learn."
            v "How many people drown per year now? A few dozen?"
            v "Before swimming lessons, before all the regulations written in blood,"
            v "That number was in the hundreds."
            v "There's nothing special about her death. She was a fool, just like the 463 other fools who drowned that year."
            #Show Rene semi-embarrassed, u know vähän häpeissään et meni sanomaan jotain tyhmää mut ei myöskään myönnä sanoneensa mitään väärin
            r "..."
            r "Do you really just remember these things, or did you pull that number out of your ass?"
            v "Language, boy."

"..."
v "Well, shall we finally move on?"

   