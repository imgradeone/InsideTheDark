label yurieye:
    menu:

        "What do you want to do with her realistic eyes?"

        "EXPERIENCE (Original ver)":
            jump yurieye_original

        "EXPERIENCE (without turning off light)":
            jump yurieye_alt

        "Back":
            jump yuri

return

label yurieye_original:

    "OK, let's go."

    scene bg closet
    show yuri 2t at t11 zorder 2
    with wipeleft
    y "[player]..."
    play sound closet_close
    show dark zorder 100
    with wipeleft
    y "My heart..."
    y 2y6 "My heart won't stop pounding, [player]..."
    y "I can't calm down."
    y "I can't focus on anything anymore...!"
    y "Can you feel it, [player]?"
    "Yuri suddenly presses my hand against her chest."
    play music hb
    show layer master at heartbeat
    y 3t "Why is this happening to me?"
    y "I feel like I'm losing my mind..."
    y 3y4 "I can't make it stop."
    y 3y6 "It even makes me not want to read..."
    y "I just want..."
    y 3s "...to look..."
    y "...at you."
    hide yuri
    show yuri eyes
    pause 3.0
    y "...Haah..."
    pause 3.0
    y "...Haah..."
    pause 3.0
    y "...Haah..."
    pause 3.0
    play sound closet_open
    stop music
    show layer master
    hide yuripupils
    show yuri 1n at face
    with None
    show yuri 3n at t32 with None
    hide dark
    show monika 3l at f31 zorder 3
    with wipeleft
    m "U-Um..."
    m "It's...time to share poems..."

    scene black
    show monika at thide zorder 4
    show yuri at thide zorder 2
    hide monika
    hide yuri
    $ persistent.yurieye_seen = True
    jump yurieye

return

label yurieye_alt:

    "Well..."
    "I think you're serious."
    "So, let's go."

    scene bg closet
    show yuri 2t at t11 zorder 2
    with wipeleft
    y "[player]..."
    play sound closet_close
    y "My heart..."
    y 2y6 "My heart won't stop pounding, [player]..."
    y "I can't calm down."
    y "I can't focus on anything anymore...!"
    y "Can you feel it, [player]?"
    "Yuri suddenly presses my hand against her chest."
    play music hb
    show layer master at heartbeat
    y 3t "Why is this happening to me?"
    y "I feel like I'm losing my mind..."
    y 3y4 "I can't make it stop."
    y 3y6 "It even makes me not want to read..."
    y "I just want..."
    y 3s "...to look..."
    y "...at you."
    hide yuri
    show yuri eyes
    pause 3.0
    y "...Haah..."
    pause 3.0
    y "...Haah..."
    pause 3.0
    y "...Haah..."
    pause 3.0
    play sound closet_open
    stop music
    show layer master
    hide yuripupils
    show yuri 1n at face
    with None
    show yuri 3n at t32 with None
    show monika 3l at f31 zorder 3
    with wipeleft
    m "U-Um..."
    m "It's...time to share poems..."

    scene black
    show monika at thide zorder 4
    show yuri at thide zorder 2
    hide monika
    hide yuri

    $ persistent.yurieye_seen = True

    jump yurieye

return