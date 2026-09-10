####This is for all the point and click sections###
###################################################

label valac_convo:
    if valac_convo == 1:
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
        r "Just… wasn't expecting you to be so…"
        v "Extraordinary? One-of-a-kind? Exotic? Unique?"
        r "Sure, let's go with that."
        $ valac_convo +=1
    elif valac_convo == 2:
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
    elif valac_convo == 3:
        r "So… You're an archdemon."
        v "I thought that was already established."
        r "Well, yeah. But it's still difficult to believe. It's like being told your ancestor was a dragon, or something."
        v "You'd know if your family had a dragon in it somewhere. They're traits are quite noticeable. Be glad yours are only so minor."
        r "Doesn't make them any less out of the ordinary."
        r "Wait, you mean there ARE people related to dragons?!"
        $ valac_convo += 1
    elif valac_convo == 4:
        r "Hey, so, how can you turn into a snake?"
        v "I thought me being an archdemon was a needlessly well-established fact."
        r "So you can just do it? On command, by nature?"
        v "Magic comes to me as comfortably as breathing, so yes, by nature."
        r "..."
        r "Where does your cane go when you become a snake?"
        #Valac uncomfortable smile
        v "It transforms with me."
        r "... How? Like, how your clothes do?"
        v "No. This cane was my tail at one point in time."
        v "I made use of it after it was forcibly severed without my consent."
        r "..."
        r "Okay. Right"
        r "So now it's your, what's it called… white cane?"
        v "...?"
        r "Like, you use it to get around obstacles and stuff, find your way around if you can't see."
        v "Does this look like some silly plastic pole? Those are pointless. I can walk perfectly fine even without it."
        "..."
        "I've seen him tapping it at the edges of the walkways and stairs."
        $ valac_convo += 1
    elif valac_convo == 5:
        "Lol fifth convo"
        $ valac_convo += 1
    elif valac_convo <= 6:
        r "Tää on keskustelu kuus."
        v "Siisti juttu make."
        $ valac_convo += 1
    elif valac_convo <= 7:
        "Ahyuk, tää on seittemäs keskustelu."
        $ valac_convo += 1
    else:
        r "I can't think of anything to say to him."
#Checks where player interacted with valac and puts them back where they were, hopefully
    if player_pos  ==1:
        jump graveyard_1

    elif player_pos ==2:
        jump graveyard_2

    elif player_pos ==3:
        jump graveyard_3

    elif player_pos ==4:
        jump graveyard_4

    else:
        return





        
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



  


label graveyard_4:
    #if Signe_I_found and Aarne_found and Lennart_found == True:
        #Initiate endgame branching
    #else:
        #pass
    
    scene section4
    "There are some more placeholders to click."
    "This is a graveyard 4"
    call screen graveyard_section4

    label Aarne_grave:
        r "Aarne Vennamo..."
        r "I think this must be Signe's father."
        v "... Yes, he's one of ours."
        "Valac looks deep in thought..."
        r "looking at the dates, I think this might be one of the last graves we can feasibly still find."
        r "I think the really old ones are removed aren't they? If no one comes to remember them."
        v "..."
        v "And no one born that long ago would still live, most likely."
        v "..."
        r "... What? What is it?"
        v "You best be prepared. His story is a long one."
        v "... Aarne Valentin."
        v "Born 20th of February 1884. Younger brother of Lennart Valdemar."
        v "..."
        v "Aarne and his brother were raised by their mother, and neither brother remembered much of their father."
        v "Despite his best attempts to reconnect, he failed to find him."
        v "His mother, on the other hand, was a constant pressure on his life."
        v "She'd devoted most of her waking moments in seances, trying to perfect her art of spiritism. Even as her reputation and relationships began to decline."
        v "Her lack of love and attention, her separating him from his father, her incessant, delusional ramblings..."
        v "When he came of age, Aarne had her committed to an asylum."
        v "This sparked animosity between him and his brother. To further distance hismelf from his family, he changed his last name. To Vennamo."
        v "Despite his off-putting appearance, Aarne was a succesful author."
        v "Unfortunately for him, his talents shone the brightest when he was suffering."
        v "When the civil war broke out, Aarne fully lost contact with his once close brother. Separated by politics and ideology, Lennart joined the reds, while Aarne joined the whites."
        v "They never faced each other during the bloody affair, but Aarne always feared the day he might have to shoot his own brother."
        v "But the war ended, the white side claiming victory. The bloody aftermath continued beyond warfare."
        v "After realising what conditions his brother was being subjected to, Aarne rushed to get his brother out from the prison camp."
        v "He succeeded, and with his newly engaged wife Aune, tried to nurse Lennart back to health."
        v "An olive branch for years of animosity."
        v "Lennart died only months after."
        v "And fate would not let Aarne escape."
        v "His beloved Aune, and tiny infant daughter Signe Impi, both succumbed to the Spanish Flu only weeks apart. Aarne was spared."
        v "He remarried. With one Tyyne Maria. They had twins, Signe Amanda and Toivo Armas."
        v "The wards proved to be a fruitful time for Aarne's career."
        v "Due to his age, he narrowly avoided being drafter into the wards of the 20th century. Fate wasn't as kind ot his son, Toivo, who persihed on the frontlines."
        v "None, not his wife, his daughter, or any of his artist friends, were wiser to the gaping hole where his heart was supposed to be."
        v "During a large family gathering, to remember and forget the past when necessary, he stepped into the middle of the dining room."
        v "And announced that he would be shooting himself, then and there."
        v "The family did not believe him."
        v "His wife rolled her eyes. Simo and Signe bid him to stop fooling around and to sit back down. He was scaring Riitta."
        v "But he'd known where Simo, Signe's husband, had hid his gun after the war."
        v "..."
        v "Aarne lived a long, miserable life. He died on the 2nd of February, 1958."
        "..."
        r "That's... awful."
        v "..."
        v "One of the most selfish things a person can do, really."
        r "What? Killing themselves?"
        v "Yes."
        v "A father, a husband and a grandfather — To break the entire family, just to... what? Make a point?"
        v "He ruined their lives. Sent them all to an early grave."

        menu:
            "Yes, it was selfish.":
                r "Yeah... You're right."
                r "They all died so young. Even if he didn't mean to, he took their futures with him."
                r "... Why would he do something like that?"
                r "I mean, he was wealthy, succesful, had a family even after all he'd been through. Didn't even serve in the wards."
                # Valac shit eating grin because he thinkgs this is funny
                v "Well. We can never truly know what's going on inside other peoples' heads, can we?"
            
            "No, it wasn't selfish.":
                r "... More sad than selfish, I think."
                v "Oh?"
                r "I... I mean I can't know, but I think he was desperate for someone to understand him. No one did, so he took things into his own hands."
                r "He was probably tried, and maybe no one realised how tired he was."
                r "Maybe he thought he didn't deserve to exist. Survivor guilt and all."
                r "And... I mean... It's not like I know that much about it, but..."
                r "Maybe he thought he was doing them a kindness. They wouldn't have to suffer him anymore. They'd be free. He wouldn't burden them anymore, with his grief that never healed."
                v "It wasn't selfish of him to pull them down with him?"
                r "I know it's awful. And not kind, at all. Least of all to himself."
                v "..."
                v "... An interesting point of view."

        r "..."
        r "... wait. He changed his surname?"
        v "Some did."
        r "And his brother — Lennart? — didn't?"
        v "If you're keen to find him, despite knowing what happened to him, go ahead."
        $ Aarne_found = True
        jump graveyard_4

    label Signe_I_grave:
        r "Aune neé Matintytär... and Signe Impi Vennamo. Just a few months old."
        v "Why are we here?"

        if Aarne_found == True:
            v "We already know what happened. There's zero reason to listen to the same bleak tale again."
            menu:
                "Yeah, maybe you're right.":
                    r "I don't know if I want to hear that in more detail."
                    r "..."
                    v "... Let's move on."
                    $ Signe_I_found = True
                    jump graveyard_4
                "No, I want to hear it.":
                    r "But what if there is? This Signe is also blood-related to you. To me."
                    r "I think her story is worth telling on its own merits. No matter how short it is."
                    r "As is Aune's."
                    v "This Aune is of no use to me."
                    v "... But fine. I'll dredge the memory of Signe from the stone."
                    v "It's a short one."
                    jump Signe_I_story
        else:
            r "Well, she's a Vennamo. Probably related to Toivo and Signe."
            r "... Another Signe?"
            v "Alright, fine."
            v "It's a short one."
            jump Signe_I_story
    
    
    label Signe_I_story:
        v "Signe Impi Vennamo, born 24th of June 1918. Daughter of Aune Matintytär and Aarne Vennamo."
        v "Her birth was a spark of light in her father's dim life."
        v "She'd been long-awaited, beloved, even before ever opening her eyes."
        v "Her mother used to sing to her. Songs her own mother had sung. Songs of birds, the lakes and the hereafter."
        v "She sang, she sang and sang, until she no longer could."
        v "Her father tried to do the same after her mother was no longer there to sing little Signe to sleep."
        v "But she could only cry."
        v "Signe Impi died on the 16th of April 1919."

        r "..."
        v "..."
        v "Regrettable."
        r "... So they both died because—"
        v "The Great Influenza epidemic. The Spanish flu."
        r "I thought that was only a thing elsewhere. You know, big population centres and so on."
        v "Oh, it was a 'thing' everywhere."
        r "Were you... active, then?"
        v "Oh, no. I slept through most of it."
        v "..."
        r "So... wait."
        r "There's Signe Amanda, and then there's Signe Impi..."
        if Aarne_found == True:
            r "Aarne gave the same name to both daughters?"
        else:
            r "Were they sisters? Why did they have the same first name?"
        v "Common practice. If one child died very young, the next one would be given the same name."

        menu:
            "That's... kind of sweet?":
                r "I... don't really know if I'd do that."
                r "But I guess times were different."
                v "Indeed they were."
                r "Maybe it was like... a way to rememeber them. To keep a part of them with them."
                r "My cousin was named after his grandfather..."
                r "So I guess it's kind of like that."
                v "That's one way to look at it."
                v "Or perhaps it was just easier, not having to come up with a new name. And less things to grieve if you pretend the dead child doesn't exist."
                r "That's pretty bleak."
                r "I guess some people could have thought of it that way. But I guess it's a complex thing to parse."
                if Aarne_found or Lennart_found == True:
                    r"..."
                    v "..."
                    v "What?"
                    r "Nothing."
                else:
                    pass

            "That's really weird.":
                r "That's weird. What, did they run out of names?"
                v "Maybe it was a kindness. To give them a chance to live through their sibling."
                r "Still, kind of macabre. Name a child after their dead sibling, like they're a replacement."
                v "Isn't it a fairly common practice to name your child after their relatives, dead or alive?"
                r "Well, yeah, it's not rare. But it's weird when it's dead children."
                v "Why? Isn't that precisely why they would choose to do that? To honour someone?"
                v "Isn't it just telling of how much she was loved? That she was the namesake for her younger sister?"
                r "I... I just don't see it."
                v "I wouldn't expect anything more."
                
        v "... Well. Let's continue."
        r "Yeah. Sure..."
        r "{size=-20}... I hope you and your mom are together now."
        v "Did you say something?"
        r "Nothing."
        $ Signe_I_found = True
        jump graveyard_4
    
    
    
    label Lennart_grave:
        if Aarne_found == False:
            r "..."
            r "I don't recognise that name at all."
            r "Probably not related."

        else:
            r "... Wait."
            r "Lennart... Fennander?"
            r "Is this Aarne's brother?"
            v "Seems to be."
            v "Well, I think we already know what happened to him."
            r "..."
            r "I want to hear his perspective."
            v "Fine... If you insist."
            
            v "Lennart Valdemar Fennander. Born 7th of July, 1892."
            v "The first born son of a distinguished spirit medium and her elusive husband."
            v "Lennart didn't remember much of his father, and never looked for him once his mother spirited him and his brother away from him."
            v "Despite his mother's ever worsening mental state, Lennart lover her with all his heart. Looked after her, and made sure she was as comfortable as she could."
            v "And was understandably incensed after Aarne had her committed to an asylum, without telling him."
            v "The once close borthers grew apart. The last threads that kept them talking to each other snapped as the civil war ignited."
            v "Despite his wealthy background and established family line, LEnnart fought as part of the reds."
            v "For his efforts he was rewarded a long, grueling stay in a prison camp where he languished for months. Underfed, starving, ravaged by disease."
            v "He was one of the lucky ones."
            v "As a final olive branch, after years apart, Aarne got his brother out."
            v "Hoping to nurse his brother back to health, Aarne stayed quietly by his bedside."
            v "But Lennart had suffered too greatly in the flifth and famine."
            v "His health continued declining, and he died mere months later. Never able to marrt, have children, or reconcile with his brother."

            r "..."
            r "Man. I... What a terrible end."
            v "Well, what can you do?"
            v "Maybe he should have done the right thing and not have joined the weaker side, just beacuse of his ideals."

            menu:
                "It was a stupid thing to do":
                    $ p_emp -= 1
                    r "I mean, the whole civil war thing seemed pretty pointless. Were things realaly so bad it was worth killing your own countrymen for?"
                    r "And... yeah. Weren't the reds all poor farmers and something? Why would Lennart join them?"
                    r "Kind of a bad move to join the obvious losing side."
                    v "I bet many historians wish it were that simple. Easy, clean answers that the investors and financers understnad, no ifs, buts or thoughs."
                    v "People famously always do the logical thing, after all. It's all very easy to understand and clear-cut, isn't it?"
                    v "\"The weak, evil bolsheviks\" versus \"the valiant, civilised whites\". Simple, isn't it?"
                    r "I mean — That's kind of the gist I got —"
                    v "From your history teacher who had to dumb it down so that you had even the slightest chance of retaining any information what so ever."
                    v "I thought you got yourself an upper secondary education. History and social studies weren't your fortes, were they?"
                    r "I—! Let's drop this."
                    r "I knew this was going to be like kicking an ant's nest."
                    v "If so, hos incredibly foolish of you to bring it up."
                    r "I didn't, it was you who—!"
                    r "Argh, forget it."
                "That's easy to say after the fact.":
                    $ p_emp += 1
                    r "I mean, the whole civil war was a big tragedy all around."
                    r "How would they have known that they'd lose?"
                    v "How would the poor farmers and industrial workers have known that they wouldn't stand a chance against the well-trained middle- and upperclass aided by Imperial Germany?"
                    r "Well, it wasn't that simple, was it? I thought the Soviets were backing the reds, so it wasn't like..."
                    v "Like what?"
                    r "Like... I don't know. It makes it messier."
                    r "Lennart was quite well off, wasn't he?"
                    r "And he still fought with them. Against his brother's side."
                    r "..."
                    v "People make foolish, idiotic choices all the time. Typically because they follow their hearts instead of their brains."
                    r "But that's pretty human, isn't it?"
                    r "Can't really fault the guy if he was doing what he thought was right, and got to suffer for it."
                    v "He most likely ended a life or two during that war."
                    r "..."
                    r "... Feels weird to shame someone from a hundred years ago because history happened to them."
                    v "Hmm. A fun way to put it."
            $ Lennart_found = True
        jump graveyard_4
    
    label valac_sec4:


