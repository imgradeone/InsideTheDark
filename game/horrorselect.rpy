label horrorintro:
    stop music fadeout 2.0

    "Well..."
    "Welcome to the Inside The Dark mod."
    "I am the modder, imgradeone."
    "I think that you are really enjoyed the DDLC original game, although it is a bit...scary?"
    "Ehehe..."
    "So, this mod may be harmful to you."
    "But, we will get inside the code itself."
    "So make sure you clone this mod project from https://github.com/imgradeone/InsideTheDark so that you could learn better."
    "But if you only want to experience the worst part of the DDLC game..."
    "Well..."
    "Did you finished the original game?"
    "..."
    "Bruh. XD"
    "So let's get into the mod."
    "Wait..."
    "Jeeeeeeez..."
    "I forgot to tell you that I am a newbie of modding..."
    "The mod might be VERY INCOMPLATED and FULL OF BUGS."
    "Sorry about this..."
    "BTW, I will bring 4 cute girls to this mod."
    "And I will take good care of them."
    "So, let me show them..."
    "Hello!"
    show monika 1a at t41 zorder 4
    show sayori 1a at t42 zorder 3
    show yuri 1a at t43 zorder 2
    show natsuki 1a at t44 zorder 1
    m "Hi, modder. And hello, [player]!"
    m 1b "I will love you at any time!"
    m 5a "Good luck and have fun!"
    
    $ style.say_dialogue = style.edited
    n 4x "WTF, HEY MODDER, YOU LIKE BUGSSSSSSSSSSSSSSSSSS?"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Oh, gosh, imgradeone, you made a new bug..."

    n 1b "..."
    n 1c "..."

    n "What happened..."

    $ style.say_dialogue = style.edited
    y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"
    $ style.say_dialogue = style.normal
    y "..."
    y 1c "..."
    y "So...?"
    y "Why I became..."
    $ style.say_dialogue = style.edited
    y 3y3 "INSANEEEEEEEEEEEEEE???!!!"
    $ style.say_dialogue = style.normal
    s "..."
    s 4p "Kyaaaaaaaaaa!"
    show natsuki vomit
    n "WHAAAAAAAA!"
    n "What's your problem, Yuri?"

    "Yep, I am making a lot of bugs..."
    "This will be the worst mod..."
    "Ever..."
    mc "Hey, What's happening?"

    m "..."

    "Let me fix it..."

    show monika 1a at t41 zorder 4
    show sayori 1a at t42 zorder 3
    show yuri 1a at t43 zorder 2
    show natsuki 1a at t44 zorder 1

    "Now just like nothing happened."

    "So let me get into the worst part..."

    "BTW, any chatacters' files will be kept safely."
    "So..."

    "I will always love you all."
    show monika at thide zorder 4
    show sayori at thide zorder 3
    show yuri at thide zorder 2
    show natsuki at thide zorder 1

    hide monika
    hide sayori
    hide yuri
    hide natsuki

    $ persistent.example_seen = True

    jump horrormenu

    return

label horrormenu:
    stop music fadeout 2.0

    "Now please select a character."

    menu:
        "Sayori":
            jump sayori
        "Yuri":
            jump yuri
        "Natsuki":
            jump natsuki
        "Intro":
            jump horrorintro
        "Back to main menu":
            return

    return