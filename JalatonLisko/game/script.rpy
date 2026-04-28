# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    scene bg graveyard_2
    show garmes happy
    define r = Character("Rene", who_color="#357897ff")
    define v = Character("Valac", who_color="#fdfcfc")
    #Intro CGs: Rene arrives at the graveyard gates, Valac slithers out from his sleeve in snake form
    r "There. I don't think anyone saw you."
    v "Of course they didn't. I'm not some fumbling idiot, I know how to keep myself hidden."
    v "How do you think I've survived this long, hmm?"
    r "Well—! A white snake in someone's jacket sleeve isn't a normal sight!"
    v "And that snake turning into an archdemon is? Calm down, boy."
    v "You're making a scene. Who else would come to a graveyard this time of day?"
    "The gates loom ahead, with not a person in sight."
    "Valac looks wholly unbothered. If a little impatient."
    r "... Well, there's the graveyard."
    r "I'm going back home."
    v "Wait, you're leaving?! That's not what you agreed to."
    r "You wanted to look for family graves, there's the graveyard where they are. You don't need me there."
    v "What, you don't want to bond with your long-lost great-great-great-grandfather? Come on now."
    v "...I knew where the graveyard was. But I can't find the graves on my own."
    r "What? Why?"
    v "My sight is not what it used to be." 
    v "You'll help me look, won't you?"

    return
