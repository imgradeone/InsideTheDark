label yurikill:

    menu:

        "Which section do you want?"

        "EXPERIENCE":
            jump yurikill_act
#        "Inside the Code (TODO)":
#           jump yurikill
        "Back to select menu":
            jump yuri
    return

label yurikill_act:

    "OK, go for it."
    "Known issue: It won't be able to get the kill time shorter by saving and loading."
    scene bg club_day2

    play music t10y
    show yuri 2m at t11 zorder 2
    y "Finally."
    y 2y1 "Finally!"
    y 2s "This is really all I wanted."
    y 1y6 "[player], there's no need to spend the weekend with Monika."
    y "Don't listen to her."
    y 1y5 "Just come to my house instead."
    y 3y5 "The whole day, with just the two of us..."
    y "Doesn't that sound wonderful?"
    y 3y1 "Ahahaha!"
    y 3y4 "Wow... There's really something wrong with me, isn't there?"
    y "But you know what?"
    y 1y3 "I don't care anymore."
    y "I've never felt this good my whole life."
    y 1y4 "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    y 3y4 "It feels like I'm going to die if I'm not breathing the same air as you."
    y 4a "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their entire life around you?"
    y 2y6 "But if it feels so good..."
    y 2y4 "Then why does it feel more and more like something horrible is going to happen?"
    y 2y6 "Maybe that's why I tried stopping myself at first..."
    y "But the feeling is too strong now."
    y 3y1 "I don't care anymore, [player]!"
    y "I have to tell you!"
    y 3y4 "I'm...I'm madly in love with you!"
    y "It feels like every inch of my body...every drop of blood in me...is screaming your name."
    y 3y3 "I don't care what the consequences are anymore!"
    y "I don't care if Monika is listening!"
    y 3w "Please, [player], just know how much I love you."
    y 3m "I love you so much that I even touch myself with the pen I stole from you."
    y 3y4 "I just want to pull your skin open and crawl inside of you."
    y 3y6 "I want you all to myself."
    y "And I will be only yours."
    y "Doesn't that sound perfect?"
    y 3s "Tell me, [player]."
    y "Tell me you want to be my lover."
    y "Do you accept my confession?"

    menu:
        
        "Yes.":
            jump yuriinkill
        "No.":
            jump yuriinkill

    label yuriinkill:
        window hide(None)
        stop music
        pause 1.0
        # Goodbye
        # Instead of deleting saves, we'll use after_load label to return to Yuri whenever a save is loaded
        window auto
        $ persistent.yurikillround = 1

    label yurikill1:
        window auto
        stop music
        scene bg club_day
        show yuri 3d at i11
        y "...Ahahaha."
        y "Ahahahahahaha!"
        $ style.say_dialogue = style.normal
        y 3y5 "Ahahahahahahahaha!"
        $ style.say_dialogue = style.edited
        y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
        window hide(None)
        window auto
        $ style.say_dialogue = style.normal

        play sound "sfx/yuri-kill.ogg"
        pause 1.43
        show yuri stab_1
        pause 0.75
        show yuri stab_2
        show blood:
            pos (610,485)
        pause 1.25
        show yuri stab_3
        pause 0.75
        show yuri stab_2
        show blood:
            pos (610,485)
        show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
        pause 1.25
        show yuri stab_5
        pause 0.70
        show yuri stab_6:
            2.55
            easeout_cubic 0.5 yoffset 300
        show blood as blood2:
            pos (635,335)
        pause 2.55
        hide blood
        hide blood2
        pause 0.25
        play sound fall
        pause 0.25
        scene black
        pause 2.0

        scene black
        show ykilling
        with dissolve_cg
    label yurikill2:
        $ quick_menu = True
        python:
            _history_list = []
            m.add_history(None, "", """Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!Every day is full of chit-chat and fun activities with all of my adorable and unique club members:Sayori, the youthful bundle of sunshine who values happiness the most;Natsuki, the deceivingly cute girl who packs an assertive punch;Yuri, the timid and mysterious one who finds comfort in the world of books;...And, of course, Monika, the leader of the club! That's me!I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you're a sweetheart—will you promise to spend the most time with me?Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!Every day is full of chit-chat and fun activities with all of my adorable and unique club members:Sayori, the youthful bundle of sunshine who values happiness the most;Natsuki, the deceivingly cute girl who packs an assertive punch;Yuri, the timid and mysterious one who finds comfort in the world of books;...And, of course, Monika, the leader of the club! That's me!I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you're a sweetheart—will you promise to spend the most time with me?Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!Every day is full of chit-chat and fun activities with all of my adorable and unique club members:Sayori, the youthful bundle of sunshine who values happiness the most;Natsuki, the deceivingly cute girl who packs an assertive punch;Yuri, the timid and mysterious one who finds comfort in the world of books;...And, of course, Monika, the leader of the club! That's me!I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you're a sweetheart—will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with""")

        $ style.say_dialogue = style.edited
        scene black
        window show(None)
        if not renpy.music.get_playing(channel='music') == audio.t6s:
            $ audiostart = str(renpy.random.random() * 360)
            $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
            play music t6s
        show ykilling
        label yurikillloop:
            $ persistent.yurikillround += 1
            if persistent.yurikillround < 1440:
                $ gtext = glitchtext(renpy.random.randint(8, 80))
                y "current round: [persistent.yurikillround]/1440, [gtext]"
                $ _history_list.pop()
                jump yurikillloop
            else:
                jump yurikill3

    label yurikill3:
        $ style.say_dialogue = style.normal
        $ gtext = glitchtext(renpy.random.randint(8, 80))
        if not renpy.music.get_playing(channel='music') == audio.t6s:
            $ audiostart = str(renpy.random.random() * 360)
            $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
            play music t6s
        scene bg club_day
        "[gtext]"
        window auto
        n "Alright, it's festival time!"
        show natsuki 4k at t11 zorder 2
        n "Wow, you got here before me?"
        n "I thought I was pretty ea--{nw}"
        show natsuki scream at h11
        n "EYAH!"
        n "AAAAAAAAAAAAAAAHHHH!!!"
        pause 1.0
        show natsuki scream at h11
        pause 0.75
        show natsuki vomit at h11
        pause 2.0
        show natsuki at lhide
        hide natsuki
        "Natsuki runs away."
        m "..."
        show monika 2b at t11 zorder 2
        m "I'm here!"
        m 2d "[player], did something happen?"
        m "Natsuki just ran past me..."
        m 2i "...Oh..."
        m "...Oh."
        m 2r "..."
        m 2l "Ahahaha!"
        m "Well, that's a shame."
        m 2d "Wait, were you here the entire weekend, [player]?"
        m "Oh, jeez..."
        m 2g "I didn't realize the script was broken that badly."
        m "I'm super sorry!"
        m "It must have been pretty boring..."
        m 2e "I'll make it up to you, okay?"
        m "Just gimme a sec..."
        $ consolehistory = []
        call updateconsole("os.remove(\"characters/yuri.chr\")", "You cannot delete any character.") from _call_updateconsole_18
        pause 1.0
        call updateconsole("os.remove(\"characters/natsuki.chr\")", "You cannot delete any character.") from _call_updateconsole_19
        pause 1.0
        m 2a "I'm almost done."
        m 2j "I just want to have a cupcake real quick!"
        $ gtext = glitchtext(10)
        "Monika lifts the foil from [gtext]'s tray and takes a cupcake."
        m 2b "Seriously, these are the best!"
        m "I really just had to have one, since it's the last time I'll ever get the chance to."
        m 2a "You know, before they stop existing and everything."
        m "...But anyway, I really shouldn't be making you wait any longer."
        m 2j "Just bear with me, okay?"
        m 2a "This should only take a second."

        $ persistent.yuri_kill = 0
        scene black
        show monika at thide zorder 4
        hide monika

    jump yurikill

return