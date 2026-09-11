# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define r = Character("Rene")
define a = Character("Anni")
define t = Character("Tapani")

##Tracking values

#Default Story values + tracker values
default p_emp = 0
default p_rep = 0
default first_grave = False


#Grave found values
default Riitta_found = False
default Maija_found = False
default Signe_found = False
default Toivo_found = False
default Aarne_found = False
default Signe_I_found = False
default Lennart_found = False

default visited_ukko = False
default gave_coin = False

#Tracks Valac's optional dialogue and crosses out previous conversations because the number has grown
default valac_convo = 1
#Tracks player position with valac convos
default player_pos = 1
# The game starts here.

label start:
    scene graveyard_gates
    show garmes happy
    define r = Character("Rene", who_color="#357897ff")
    define v = Character("Valac", who_color="#fdfcfc")
    #Intro CGs: Rene arrives at the graveyard gates, Valac slithers out from his sleeve in snake form
    r "There. I don't think anyone saw you."
    v "Of course they didn't. I'm not some fumbling idiot, I know how to keep myself hidden."
    v "How do you think I've survived this long, hmm?"
    r "Well—! A white snake in someone's jacket sleeve isn't a normal sight!"
    v "And that snake turning into an archdemon is? Calm down, boy. You're making a scene."
    "The gates loom ahead, with not a person in sight."
    "This wasn't what I thought this day would be like."
    #Small no-detail CG of Valac showing up on Rene's doorstep?
    "He showed up on my doorstep, unannounced. All four horns, weird eyes and white hair —"
    "I'd never met too many demons, but I knew he wasn't the average kind."
    "Proclaimed that he'd been looking for me — For family. That he'd been asleep for so long, he didn't know where his children had gone. He was happy he'd found me."
    "Demanded that I take him to the graveyard. Find out which of his — our relatives were alive, if any. Since I didn't know."
    "I'd never met them."
    "..."
    "Valac looks wholly unbothered. If a little impatient."
    r "... Well, there's the graveyard."
    r "I'm going back home."
    v "What?! This isn't what we agreed on."
    r "You wanted to look for family graves, there's the graveyard. You don't need me there."
    v "What, you don't want to bond with your long-lost great-great-great-grandfather? Come on now."
    v "...I knew where the graveyard was. But I can't find the graves on my own."
    r "What? Why?"
    v "My sight is not what it used to be." 
    v "You'll help me look, won't you?"
    "..."
    v "If you do, I could tell you about them. You never met them, you said? This could be your chance."
    "... This is so out of the blue, it's difficult to really think of reasons why I shouldn't."
    "And, I mean… If he really isn't lying, and we truly are related…"
    "..."
    "...Fuck it."
    r "Why not."
    r "... Not like I have anything better to do, anyway."
    "And on the other hand, perhaps it is best not to upset an archdemon. If he truly is one… Though with that many horns he must be, right?"
    "... Didn't think there were any around anymore."
    v "Wonderful! You could have been a bit more enthusiastic about it, but I'll take it."
    r "..."
    r "Wait, how are we supposed to find them? I don't even know who's buried here."
    v "They all are, that I do know."
    v "And surely you know your own surname? Why not start with your closest relatives, and work backwards?"
    r "..."
    r "... I don't remember where mom and dad are."
    v "Won't be hard to find. I might have a faint memory where they might be… {color=#FFBF00}section 4{/color}, if memory serves."
    v "I'd recommend taking a look at that {color=#FFBF00}map{/color} over there. No need to waste time wandering around."
    r "Alright? I'll… I'll take a look."
    jump graveyard_gates
    return

label graveyard_gates:
    scene graveyard_gates
    call screen graveyard_gates

label vaivaisukko:
    if visited_ukko == False:
        "An odd, old-looking wooden statue stands by the entrance, clutching a crutch in one hand, the other outstretched, begging. There's a small slit in its chest, big enough for a coin."
        "A plastic-covered paper on top of it says:"
        "The funds gained through the pauper statue will be used for charity work in the parish. Thank you for your donation."
        v "Well? Are you going to give alms to the poor, for the weary and the weak?"
        menu:
            "Give a coin to the pauper statue?"

            "Give.":
                $ gave_coin = True
                "I dig a 2 euro coin from the bottom of my pocket. It slides into the statue with a hollow tink."
                "I hear Valac chuckle derisively."
                v "How incredibly noble of you."
                v "Did that make you feel better about yourself?"
                "..."
            "Don't give.":
                "I stuff my hands into my pockets, and leave the statue to beg in vain."
                "There's a smug grin on Valac's face."
                v "My, how selfish of you."
                v "Then again, why help without gaining anything in return?"
                v "Well… Assuming you'll never need the help you didn't give."
                "..."

        "If this is how he treats his relatives, no wonder he doesn't know if any of them are alive. Besides me."
        $ visited_ukko = True
    elif gave_coin == False:
        v "Having second thoughts, are we?"
        r "..."

        menu:
            "Give coin to the pauper statue?"

            "Give.":
                $ gave_coin = True
                "I manage to dig a coin from the bottom of my pocket. It slides into the statue with a hollow tink."
                "... I don't feel any different."
                v "Well, how noble of you."
                v "Needed a bit to think on it, did you?"
                r "Why don't {i}you{/i} give something then?"
                v "Why should I?"
                "..."
                "Despite his words, I think I did a good thing."
            "Don't give.":
                "..."
                "Valac scoffs."
                v "What a waste."
                "He starts to walk off, like I'd offended him somehow."
                "..."
                "Why do I feel like he's disappointed in me?"
    else:
        "I dig around in my pockets for another coin, but sadly don't find any."
        r "..."
        r "Why don't you give a coin?"
        v "Why should I?"
        r "Well, I did. Because I wanted to."
        r "It's voluntary, of course. You don't have to help."
        v "Eugh."
        "To my surprise, he rummages around his coat pockets and digs out a coin."
        "It looks ancient, it's not even a euro. Maybe a markka?"
        "He slides it in and it hits the other coins with a tink."
        v "Well? Are we going?"

    jump graveyard_gates

label intro_map:
    "An old, weathered map of the graveyard."
    "I'll take a picture of it. Don't need to come back here constantly to check where we're going."
    #Phone camera sound .mp3 :D
    $ map_on = True
    v "Ah, wonders of modern technology."
    v "Shall we go?"
   
    jump TapaniKaarina_grave_intro

label TapaniKaarina_grave_intro:
    scene tapanikaarina_grave
    r "... Here it is."
    r "I told you they were dead. Why did we need to come here?"
    v "Out of principle, I suppose."
    r "..."
    r "... Why are we here?"
    r "You said you could tell me about my family if we came here. But you never said why you wanted to do that."
    v "... Well…"
    r "Were you lying? Are we even related?"
    "For a moment he looks so utterly, genuinely aghast that I felt like I'd said something far worse."
    v "Really? You're pulling that card on me?"
    v "Boy, have you looked in the mirror? You don't have those eyes for no reason."
    v "And do correct me if I'm wrong,"
    "He steps closer. Before I can react, he brushes a brusque hand over my forehead."
    #CG closeup of Rene's forehead with the horns poking out
    v "those tiny horns aren't common for non-demons, are they?"
    v "There aren't too many reasons for you to be a freak of nature, being an heir to my bloodline one possibility among them."
    v "My eyesight may be poor, so poor that I have to beg for your help. But my nose — why, it never lies. I know it is my blood coursing through your veins."
    "I stumble back."
    r "But—! Alright, fine!"
    r "But if you can smell your blood, whatever that means, then why are we here looking for your children?"
    r "Can't you go looking for them by smell, then?"
    v "Well, that's a lot of ground to cover!"
    v "And it will be easier for my weary heart if I know my search would be pointless. If they're already here."
    v "And when you find our relatives' graves, I can tell you more about them. Your grandparents, great grandparents — people you were ripped away from."
    v "And your parents… You'd like to know why they weren't there to raise you, wouldn't you?"
    "!"
    r "You'd…? Yes, please!"
    r "What happened to them? How do you know?"
    v "Patience, patience! I promise I'll tell you, after we find my other descendants. Then, we'll return here."
    v "It could be a fruitful bonding moment for us!"
    "I can't force a lie out of my mouth, to say that I'm not curious."
    "I've lived with my aunt my entire life. I don't even remember my parents."
    "And auntie didn't know about dad's side of the family. They never contacted me."
    "So Valac could be right — they might all be here."
    r "But, wait. If you were — what, asleep? — for a couple hundred years or so, doesn't that mean you don't even know those people? How would you tell me anything about them?"
    v "Not that long, no. And you'll see."
    v "I have my ways. Ways that I could show you, if you come along."
    r "... Fine. Can't say it's too often an archdemon offers to teach you something."
    r "But where do we start?"
    v "Well, you can just search blindly, take in the scenery. Maybe find some other names you recognise."
    v "Or you can search by surnames. Likely your father shares his surname with his parents. And the next one with their parents, so on and so forth."
    r "But, don't people sometimes change their surnames?"
    v "We can cross that bridge when we get to it."
    v "And as I said, you might just get lucky. I'll know if my blood is buried under the stones you find."
    r "... But if that's the case, then —"
    v "What? I'm not checking every grave in the vain hope that I'll find the right ones, the names of whom I cannot even make out."
    v "If you expect an old, old man like myself to toil himself to death looking for his lost family, then your aunt raised you quite poorly."
    "..."
    "An old receipt that'd been left in my pocket is crumpled into a tiny, sharp shard of paper in my hand."
    scene section1
    r "Well… I best start looking."
    jump graveyard_1

