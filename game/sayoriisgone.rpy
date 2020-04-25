label sayoriisgone:

    menu:

        "Which section do you want?"

        "EXPERIENCE":
            jump sayoriisgone_act
        "Back to select menu":
            jump horrormenu
    return

label sayoriisgone_act:

    "Now there is the original content."
    "Be careful of your neck."
    "Let me import the resources..."

    image exception_bg = "#dadada"
    image fake_exception = Text("An exception has occurred.", size=40, style="_default")
    image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 214\nSee traceback.txt for details.", size=20, style="_default")

    image splash_glitch:
        subpixel True
        "images/bg/splash-glitch.png"
        alpha 0.0
        pause 0.5
        linear 0.5 alpha 1.0
        pause 2.5
        linear 0.5 alpha 0.0
        "gui/menu_bg.png"
        topleft
        alpha 0.0
        parallel:
            xoffset 0 yoffset 0
            linear 0.25 xoffset -100 yoffset -100
            repeat
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            ypos 0
            pause 1.0
            easeout 1.0 ypos -500
    image splash_glitch2:
        subpixel True
        "gui/menu_bg.png"
        topleft
        block:
            xoffset 0 yoffset 0
            linear 0.05 xoffset -100 yoffset -100
            repeat

    image splash_glitch_m:
        subpixel True
        "gui/menu_art_m.png"
        zoom 0.5
        xpos 0.5 ypos 0.5
        pause 0.1
        parallel:
            xpos 0.3 ypos 1.2
            linear 0.08 ypos 0.1
            repeat
        parallel:
            pause 0.5
            alpha 0.0

    image splash_glitch_n:
        subpixel True
        "gui/menu_art_n.png"
        zoom 0.5
        pause 0.2
        xpos 0.8 ypos 0.8
        pause 0.05
        xpos 0.2 ypos 0.7
        pause 0.05
        xpos 0.4 ypos 0.2
        pause 0.05
        xpos 0.7 ypos 1.2
        pause 0.05
        xpos 0.1 ypos 1.0
        pause 0.05
        xpos 0.2 ypos 0.6
        pause 0.05
        xpos 0.9 ypos 0.4
        pause 0.05
        alpha 0.0

    image splash_glitch_y:
        subpixel True
        "gui/menu_art_y.png"
        zoom 0.5
        ypos 1.3
        block:
            xpos 0.85
            pause 0.02
            xpos 0.81
            pause 0.02
            repeat



    menu:
        "So, What do you want to say to Sayori?"

        "I love you.":
            $ sayori_confess = True
            scene s_cg3 with dissolve_cg
            "You are so nice."
            scene black with dissolve_cg
        "You'll always be my dearest friend.":
            $ sayori_confess = False

    "Here we go."

    scene bg residential_day
    "What was I thinking?"
    "I should have tried a little bit harder for Sayori."
    "It's not a big deal to at least wait for her, or help her wake up."
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs, and what I want to give her."

    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    if sayori_confess:
        "That really is something that a boyfriend would do, isn't it?"
    else:
        "Isn't that more like something a boyfriend would do?"
    "In any case..."
    "It just feels right."

    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here's goes nothing.", False)
        except: pass
    pause 6.0


    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "What the hell...?"
    "{i}What the hell??{/i}"
    "Is this a nightmare?"
    "It...has to be."
    "This isn't real."
    "There's no way this can be real."
    "Sayori wouldn't do this."
    "Everything was normal up until a few days ago."
    "That's why I can't believe what my eyes are showing me...!"
    scene black with dissolve_cg
    "I suppress the urge to vomit."
    "Just yesterday..."
    "I told Sayori I would be there for her."
    "I told her I know what's best, and that everything will be okay."
    "Then why...?"
    "Why would she do this...?"
    "How could I be so helpless?"
    "What did I do wrong?"
    if sayori_confess:
        "Confessing to her..."
        "I shouldn't have confessed to her."
        "That's not what Sayori needed at all."
        "She even told me how painful it is for others to care about her."
        "Then why did I confess to her, and make her feel even worse?"
    else:
        "Turning down her confession..."
        "That has to have been what pushed her over the edge."
        "Her agonized scream still echoes in my ears."
        "Why did I do that to her when she needed me the most?"
    "Why was I so selfish?"
    "This is my fault--!"
    "My swarming thoughts keep telling me everything I could have done to prevent this."
    "If I just spent more time with her."
    "Walked her to school."
    if sayori_confess:
        "And remained friends with her, like it always has been..."
    else:
        "And gave her what I know she wanted out of our relationship..."
    "...Then I could have prevented this."
    "I know I could have prevented this!"
    "Screw the Literature Club."
    "Screw the festival."
    "I just...lost my best friend."
    "Someone I grew up with."
    "She's gone forever now."
    "Nothing I do can bring her back."
    "This isn't some game where I can reset and try something different."
    "I had only one chance, and I wasn't careful enough."
    "And now I'll carry this guilt with me until I die."
    "Nothing in my life is worth more than hers..."
    "But I still couldn't do what she needed from me."
    "And now..."
    "I can never take it back."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never..."

    "..."

    "Oh gosh..."
    "I hope that there won't be a bug..."
    "Hey, Sayori!"
    "Are you still OK?"

    show sayori 4p at t11 zorder 2
    s "Aaaaaah..."

    "I'm sorry for this..."
    "But..."
    "Remember..."
    "I'll always love you."

    s 1q "Ehehe..."

    hide sayori

    "By the way, did you notice the traceback.txt?"
    "There are something..."
    "Interesting."

    jump sayoriisgone

return
