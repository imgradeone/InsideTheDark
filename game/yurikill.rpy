label yurikill:

    menu:

        "你想选择哪个项目？"

        "体验！":
            jump yurikill_act
#        "Inside the Code (TODO)":
#           jump yurikill
        "返回上一级":
            jump yuri
    return

label yurikill_act:

    "好的，那么开始吧。"
    "已知问题：凝视尸体的时长不能通过存档读档来加速。"
    scene bg club_day2

    play music t10y
    show yuri 2m at t11 zorder 2
    y "终于啊。"
    y 2y1 "终于啊！！！"
    y 2s "这就是我真心想要的！"
    y 1y6 "[player]，没必要和 Monika 度过周末了。"
    y "别听她的。"
    y 1y5 "就来我家吧。"
    y 3y5 "一整天就只有我们两个..."
    y "是不是很完美啊？"
    y 3y1 "啊哈哈哈哈！"
    y 3y4 "哇... 我是不是有毛病...？"
    y "但你知道吗？"
    y 1y3 "老子才不在乎呢！"
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

        "凉凉预警"

        "是的。":
            jump yuriinkill
        "不！":
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
        y "...啊哈哈哈。"
        y "啊哈哈哈哈哈哈哈！"
        $ style.say_dialogue = style.normal
        y 3y5 "啊哈哈哈哈哈哈哈哈！"
        $ style.say_dialogue = style.edited
        y 3y3 "啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈{nw}"
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
                y "当前进度：[persistent.yurikillround]/1440, [gtext]"
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
        n "好哇，是学园祭时间！"
        show natsuki 4k at t11 zorder 2
        n "哇，你比我早到？"
        n "我觉得我真是个吃hu————{nw}"
        show natsuki scream at h11
        n "噫啊！"
        n "啊↑啊↗啊→啊↘啊↓啊↓啊↓啊↓！！！"
        pause 1.0
        show natsuki scream at h11
        pause 0.75
        show natsuki vomit at h11
        pause 2.0
        show natsuki at lhide
        hide natsuki
        "Natsuki 溜了。"
        m "..."
        show monika 2b at t11 zorder 2
        m "我在这呢！"
        m 2d "[player]，刚刚是不是发生了什么？"
        m "Natsuki 刚刚从我身边跑了..."
        m 2i "...哦..."
        m "...口我。"
        m 2r "..."
        m 2l "啊哈哈哈！"
        m "有点遗憾啊。"
        m 2d "等等，[player]，你是不是整个周末都要在这里？"
        m "天哪..."
        m 2g "我都没发现这游戏爆得这么厉害。"
        m "肥肠抱歉！"
        m "这肯定很无聊的说..."
        m 2e "我帮你整理一下，好伐？"
        m "给我一点点时间..."
        $ consolehistory = []
        call updateconsole("os.remove(\"characters/yuri.chr\")", "You cannot delete any character.") from _call_updateconsole_18
        pause 1.0
        call updateconsole("os.remove(\"characters/natsuki.chr\")", "You cannot delete any character.") from _call_updateconsole_19
        pause 1.0
        m 2a "可以了。"
        m 2j "我现在想拿一个纸杯蛋糕了。"
        $ gtext = glitchtext(10)
        "Monika 从 [gtext] 的托盘里拿出箔纸并拿走了一个纸杯蛋糕。"
        m 2b "啊，真香！"
        m "我肯定要拿的呐，毕竟这是最后一次了。"
        m 2a "你懂的，在她们彻底消失之前。"
        m "...但怎么说，我真的不能让你再等下去了。"
        m 2j "就陪我，好吧？"
        m 2a "一下下就好。"

        $ persistent.yuri_kill = 0
        scene black
        show monika at thide zorder 4
        hide monika

    jump yurikill

return