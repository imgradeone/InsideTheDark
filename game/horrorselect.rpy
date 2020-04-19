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
    "Did you finished the real game?"
    "..."
    "Ahaha..."
    "So let's get into it."
    "Jeeeeeeez..."
    "I forgot to tell you that I am a newbie of modding..."
    "The mod might be VERY INCOMPLATED and FULL OF ISSUES."
    "Sorry about this..."
    "BTW, I will bring 4 girls to this mod."
    "So, let me show them..."
    show monika 1a at t41 zorder 4
    show sayori 1a at t42 zorder 3
    show yuri 1a at t43 zorder 2
    show natsuki 1a at t44 zorder 1
    m "Hi, [player]!"
    m 1b "I am watching your code!"
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
    show natsuki vomit

    "Yep, I am making a lot of bugs..."
    "This will be the worst mod..."
    "Ever..."
    mc "Hey, What's happening?"

    m "..."

    show monika 1a at t41 zorder 4
    show sayori 1a at t42 zorder 3
    show yuri 1a at t43 zorder 2
    show natsuki 1a at t44 zorder 1

    "Just like nothing happened."

    "So let me get into the worst part..."

    "BTW, any chatacters' files will be kept safely."
    "So..."

    "I will always love you all."

    hide monika
    hide sayori
    hide yuri
    hide natsuki

    $ persistent.example_seen = True

    jump horrormenu

    return

label horrormenu:

    "Time to select."

    menu:
        "Sayori Hangout":
            jump sayoriisgone
        "Back to menu":
            return
        "Intro":
            jump horrorintro

    return