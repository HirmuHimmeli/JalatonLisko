####This is for all the point and click sections###
###################################################

label graveyard_1:
    if Maija_found == True:
        r "I think that's all my relatives in this section."
        v "Onto the next one, then?"
        jump graveyard_2
        
    else:
        pass    
    scene section1
    call screen graveyard_section1


    label placeholder_grave:
    "This is a placeholder."
    #Jos halutaan paljon feikkihautoja eikä haluta koodata jokaista hautaa erikseen
    #Niin pitää tehdä joku player location funktio. Mut honestly whos gonna check might as well write individual labels
    jump graveyard_1

    label TapaniKaarina_grave:
    "Not yet."
    "I need to find the rest of them first."
    jump graveyard_1

    label Maija_Petri_grave:
        if Maija_found == False:
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
                r "Oh, {w}well I—{w=1.0}{nw}"
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
            v "...How undignified. For a young mother as well."
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

            v "Well, no matter. Unto the next one."
            r "Wait, what about her husband?"
            v "He's not part of my bloodline, he's inconsequential. The only thing of import he gave you is your surname."
            v "Neé Wuorenheimo, was it?"
            if Riitta_found == False:
                r "Might be worth looking for her sister as well, if she's also here."
                v "Do whatever you want. I'm patient if nothing else."  
            else:
                pass

            $ Maija_found = True

        else:
            r "Found her already."
        jump graveyard_1

    label valac_sec1:
        if valac_convo ==1:
            r "..."
            v "What? Spit it out."
            r "This is just…"
            r "Well, it's a little weird, isn't it? Someone just knocks on your front door and they happen to be your great-great-something-grandfather."
            r "And a fucking archdemon of all things."
            v "Language, young man."
            r "Sorry…"
            r "But, still. It's uh. A change of pace, to say the least."
            r "Wasn't expecting my Wednesday to look like this."
            r "Or… you, to be honest."
            v "What's that supposed to mean?"
            r "When I opened the door I wasn't expecting scales and four horns and weird eyes —"
            v "Don't insult me."
            r "I'm not, I —"
            "I stop talking before I manage to stuff my foot any further up my mouth."
            r "Just… wasn't expecting you to be so…"
            v "Extraordinary? One-of-a-kind? Exotic? Unique?"
            r "Sure, let's go with that."
            $ valac_convo +=1

        elif valac_convo ==2:
            r "You know, I've wondered. Why I look like this, and why no one else does."
            v "You never had any demons in your class? And some corvid demi-humans have darker sclera."
            r "But no one tends to have both. Or have them passed down, when neither mom nor dad were either."
            v "Hmm."
            r "Do you know why that is?"
            v "Not really, no. We're special in that way, I suppose."
            r "'We', meaning us, or —"
            v "Me and my siblings. We're an odd bunch, I have to admit."
            v "..."
            v "I wonder how many of them are still around."
            r "I thought you guys were immortal?"
            v "Oh, and that's why most of us have seemingly vanished from the face of the Earth?"
            v "But… yes. Death typically isn't the end for us."
            r "That's… certainly a choice of words. What the hell does that mean?"
            v "All in due time, boy. I'd hate to lose all sense of mystery so quickly."
            $ valac_convo +=1


        else:
            v "..."
            v "What? Don't just stand there, get to work boy."
        
        jump graveyard_1

        



label graveyard_2:
    if Riitta_found  == True:
        r "Well that's it for this one."
        v "Let's move on. I'm getting cold just standing around here."
        jump graveyard_3
    else:
        pass

    scene section2
    "This is a graveyard 2"
    "There are some placeholders to click."
    call screen graveyard_section2

    label Riitta_grave:
        if Riitta_found == False:
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
                r "Oh, {w}well I—{w=1.0}{nw}"
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
            $ Riitta_found = True
        else:
            r "Already found her."
            v "Oh, you want to hear the tale of her tragic death again?"
            r "No thanks."
        jump graveyard_2

    label placeholder_grave_2:
        "This is a placeholder."
        jump graveyard_2

    label placeholder_grave_3:
        "This is a placeholder."
        jump graveyard_2
    


    
label graveyard_3:
    if Signe_found and Toivo_found == True:
        r "I think that's all for section 3."
        jump graveyard_4

    else:
        pass
    
    scene section3
    "This is section 3."
    "There are some more placeholders to click."
    call screen graveyard_section3
   
    label Signe_grave:
        if Signe_found == False:

            r "Signe Wuorenheimo and Simo Wuorenheimo..."
            r "These must be Maija and Riitta's parents."
            v "..."
            v "Oh, yes. This Signe is of my flock."

            v "Signe Amanda Vennamo, later Wuorenheimo. Twin sister of the accomplished young photographer, Toivo Vennamo."
            v "Born on the 10th of February, 1921, died 2nd of October 1970."
            v "the twins were raised sheltered and far away from their deluded but influental grandparents, instead spending their summers with their humble mother's family in the countryside."
            v "Signe proved to be a character of some eccentric qualities. While her brother pursued photography, Signe took up the pen, and in her spare time wrote poetry to soothe her racing mind."
            v "She married one Simo Väinö Wuorenheimo in 1940, only months after the Winter War."
            v "Sadly, the peace was temporary. As Europe continued to languish in the tides of war, Simo was drafted as a new war began only a year later."
            v "While her husband spent years driving a truck, delivering the bodies of fallen soldiers back home, Signe stayed with her cousins." 
            v "Despite the outlaw of dancing during wartime, she and her cousins would sneak off to secret dances that were held in barns and other unseen places."
            v "And it so happened that many Germans stationed in the same area would occasionally join in the revelry, sneaking off to acquaint themselves with the local women and exchange rare goods brought with them."
            v "During one such evening, she met a handsome young man."
            v "He spoke little Finnish, and she even less German, but they found comfort in each other. True silence in the surrounding cacophony."
            v "One day he disappeared, never to be seen again. Leaving Signe with child."
            v "The child, Maija Anneli, was born in the midst of a world at war."
            v "Simo eventually returned to Signe, begrudgingly accepting the child and her missteps."
            v "The couple concealed Maija's true parentage from the rest of the family. She did have her mother's eyes, after all."
            v "After the war, Simo and Signe had a child together, Riitta Eeva."
            v "What little happiness had returned after the birth of their children, Simo's return from the war and returning normalcy, lasted only for a decade or so."
            v "One fateful day, during a family reunion in their house, Signe's father stood up, and made an announcement. Not a single person believed him."
            v "She could only watch as her father pulled out a gun, and shot himself in the head. In front of her and her children."
            v "Her mind, spirit and wellbeing shattered. She was admitted to a hospital, and later a mental institution."
            v "After twelve years of anguish, after finally telling Maija that Simo was not her father, she passed away, never knowing the name of the man she'd danced with that January night."
            "..."
            v "What a sordid story."
            r "An outlaw of dancing? Was that really a thing?"
            v "I recommend opening a book once in a while. Maybe you'd have heard of it already."
            v "Yes, it was felt to be inappropriate to dance while men were dying in the war effort."
            v "..."
            v "Not that it bothered her. What an uncouth girl."

            menu:
                "I don't think we understand her.":
                    # p_emp += 1
                    r "I mean, yeah. That's a terrible thing to do, to her husband."
                    r "But... I don't know. There was a war going on. She didn't know if he was coming back, did she?"
                    v "So that makes it okay to—?"
                    r "No, of course not. But—"
                    r "I, I don't know. It's difficult. Feels icky to judge someone's decisions from that long ago."
                    r "I don't think it was right, but it feel sbad to say that it was 'wrong' either, you know?"
                    v "Oh, trying to become an academic, are you?"
                    r "I'm just trying to give her a fighting chance."
                    r "And it's not like we know for a fact that Simo wasn't unfaithful. Not like that's even improbable."
                    v "Depends on where he was stationed. He might have met an 'exotic' Karelian or two."
                    r "... Plenty of people around regardless."
                    v "My, how progressive of you. Were they also in an open relationship, hm?"
                    r "That's not what I'm saying and you know it."
                    r "It wasn't right, but... I'm trying to think about what I would have done. If tomorrow wasn't a certainty anymore. And it doesn't feel that clear-cut anymore."
                    r "And maybe, if she'd been a man instead, we wouldn't have the instinct to judge her so harhsly."

                "I don't understand how she could do that.":
                    r "I mean, yeah. That's a terrible thing to do to her husband."
                    r "And... didn't women help with the war effort at all? There were some, weren't there?"
                    v "Lotta Svärd, yes."
                    v "With over two hundred thousnad volunteering women."
                    r "..."
                    r "And she wasn't one of them?"
                    v "Even if she was, would that have stopped her? They're not mutually exclusive."
                    r "Well, I mean—"
                    v "Chances were she was ordered to help with the war effort somewhere else, in a factory or as a builder..."
                    v "Oh, were you insinuating that joining would have prevented her immoral acts? Absolved her? Made her repent? Had \"fixed\" her?"
                    r "No, of course not?! Where'd you get that?"
                    v "You know,"
                    v "it isn't too unlikely that Simo had his own missteps while away."
                    v "You could have some more long-lost relatives you don't know about."

            "..."
            r "... But I don't think anything would make you deserving of seeing your own father shoot himself in front of you."
            r "That's the same incident Maija and Riitta saw as children, wasn't it?"
            v "I can't imagine it to have been helpful to their psyches."

            if Toivo_found == False:
                r "You said she had a twin brother, right?"
                r "Where did he go?"
                v "Well, might be worth looking for him."
                
            else:
                r "What an awful end for the twins."
                r "Neither had the chance to become the artists they hoped to be."
            
            r "... I wonder if auntie had some of her poems saved, somewhere..."
            "..."
            v "... neé Vennamo, was it?"
            v "..."
            "Unexpectedly, Valac lets out a mirthless chuckle."
            v "Let us continue, shall we?"
            $ Signe_found = True
      
        else:
            r "Found her already."
        jump graveyard_3

    label Toivo_grave:
        if Toivo_found == False:
            r "Toivo Armas Vennamo... died in 1941."
            v "..."
            v "Toivo Armas Vennamo, twin brother of Signe Amanda. Born on the 10th of February 1921, died 19th of November 1941."
            v "Raised sheltered and away from his father's 'deluded' parents, Toivo became close with his maternal grandfather, Eino."
            v "He helped him run his photography studio during the summers, where he similarly took interest in photography."
            v "Turning out to be a quite the prodigy, he earned some awards even before his 18th birthday."
            v "Instead of leading him to stardom, it led him to his death."
            v "He'd been too young for the frontlines in the Winter War, but as the summer of 1941 came around, he was drafted in the newly ignited war efforts."
            v "His talents earned him a spot in the TK-companies, to document the war with his fellow photographers, writers and artists."
            v "Beloved, sigiled camera in hand, he did his job exceptionally."
            v "His photos were well received by the war cabinet, and he was encouraged to further continue his artful documentation. Of action, troops advancing through the invaded Karelian countryside."
            v "Fulfilling this duty meant, however, that he was skirting closer and closer to active cannon fire."
            v "One November day, unlucky cannon fire landed right where he was."
            v "Only his Contax camera was left behind where he'd stood."
            v "The family had nothing else to bury."
            "..."

            r "And just like that, huh?"
            r "He was just, what — 20? Even younger than me..."
            r "... Died on my birthday. The same date, I mean."
            "Valac looks oddly at me for a moment. Or in my general direction, really."
            "He seems lost in thought."
            v "Do you believe in reincarnation?"
            r "What? Like, I'm Toivo reborn?"
            r "I dont' think so."
            r "Or, maybe he just left his photography genius back in the afterlife."
            v "..."
            v "Hmphm."
            r "...Hm? What's so funny?"
            v "Oh, it's nothing."
            v "... This family of mine seems to have a bad tendency to die in embarrasingly young."
            r "That's—"

            #Onko pointless menu og scriptissä? Keksitään jotain mielenkiintoisempaa sanottavaa
            v "Let's move on, shall we?"
            if Signe_found == False:
                r "He had a twin, didn't he? The mother of Riitta and Maija?"
                v "If you really want to find her, go ahead."
            
            else:
                pass

            $ Toivo_found = True
        else:
            "Found him already. I wonder where his twin is."
        jump graveyard_3

    label ph32:
        "This is a placeholder."
        jump graveyard_3

    label ph33:
        "This is a placeholder."
        jump graveyard_3

    label ph34:
        "This is a placeholder."
        jump graveyard_3

    label ph35:
        "This is a placeholder."
        jump graveyard_3

    label ph36:
        "This is a placeholder."
        jump graveyard_3

    label ph38:
        "This is a placeholder."
        jump graveyard_3

    label ph39:
        "This is a placeholder."
        jump graveyard_3

    label valac_sec3:
  


label graveyard_4:
# if Signe_found and Toivo_found == False:
    #    r "I think that's all for section 4."
    #    jump graveyard_5

# else:
#     pass
    
    scene section4
    "There are some more placeholders to click."
    "This is a graveyard 4"
    call screen graveyard_section4




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
