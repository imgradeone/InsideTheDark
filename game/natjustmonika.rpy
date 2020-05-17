label natjustmonika:

    menu:

        "Which section do you want?"

        "EXPERIENCE":
            jump natjustmonika_act
#        "EXPERIENCE (Peace ver.)":
#            jump natjustmonika
#        "Inside the Code (TODO)":
#            jump natjustmonika
        "Back to select menu":
            jump natsuki

    return

label natjustmonika_act:

    scene bg club_day2
    show natsuki 42c at t11 zorder 2
    with wipeleft_scene
    n "This is clearly Yuri's influence..."
    n "I didn't realize you were so impressionable."
    n "Spending all this time with her in the club..."
    n "Now trying to write like her..."
    n 1s "This is stupid."
    n "At least Monika appreciates my writing..."
    n 1r "...Ugh."
    n 1q "Okay...I guess I'm going to share my poem with you now."
    n "I really hate that I have to do this."
    n "But unfortunately I don't have much of a choice."
    n 1h "Just...read it carefully, okay?"
    n "Then you can go away."
    $ style.say_dialogue = style.normal
    call showpoem(poem_n23, revert_music=False) from _call_showpoem_4
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    stop music
    hide screen tear
    show natsuki ghost_base
    n "I changed my mind."
    n "Ignore everything you just read."
    n "There's no point in trying to do anything."
    n "It's Yuri's own fault that she's so unlikable."
    n "Can you hear me, [player]?"
    n "If you would just spend more time with Monika, all these problems would go away."
    n "Yuri and I are too messed up for someone as wonderful as you."
    n "Just think of Monika from now on."
    n "Just Monika."
    hide natsuki
    $ style.say_dialogue = style.edited
    "Just Monika."
    menu:
        "Just Monika."
        "Just Monika.":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "Just Monika.", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "Just Monika." with Dissolve(0.5, alpha=True)
    pause 1.0
    stop music
    hide splash_warning
    scene black
    with wipeleft_scene
    $ skip_transition = True

    jump natjustmonika

return