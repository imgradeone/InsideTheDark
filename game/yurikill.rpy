label yurikill:

    menu:

        "imgradeone" "你想选择哪个项目？"

        "体验！":
            jump yurikill_act
#        "Inside the Code (TODO)":
#           jump yurikill
        "返回上一级":
            jump yuri
    return

label yurikill_act:

    "imgradeone" "已知问题：凝视尸体的时长不能通过存档读档来加速。"
    "imgradeone" "好的，那么开始吧。"
    scene bg club_day2  
    #您有 1/6 的几率触发死不瞑目的 Sayori 彩蛋，如果你看到了这行注释，请加油触发（
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
    y "我这辈子都没有感到这么爽过。"
    y 1y4 "和你在一起就已经是超乎我想象的极致快乐了。"
    y "我对你“上瘾”了。"
    y 3y4 "我感觉如果不和你在一起，我就要死了。"
    y 4a "如果有那么关心你的人，那感觉是不是很爽？"
    y "还是那种一辈子都想围着你转的那种。"
    y 2y6 "不过如果这种感觉很好..."
    y 2y4 "那么为什么可怕的事情还是要发生？"
    y 2y6 "也许这就是我最初尝试阻止自己的原因..."
    y "但是现在这个感觉特别强烈了。"
    y 3y1 "[player]，即便这样，我也不在乎了！"
    y "我一定要告诉你！"
    y 3y4 "我...我彻彻底底地爱上你了！"
    y "我感觉我身体的每一块地方...还有每一滴血...都在喊着你的名字。"
    y 3y3 "我也不在乎后果了！"
    y "我也不在乎 Monika 有没有在那里偷听了！"
    y 3w "[player]，请一定要明白我有多爱你啊。"
    y 3m "我特别爱你，甚至一度偷你的笔去自///慰。"
    y 3y4 "我只想拉开你的表//皮，在你的身体里游走。"
    y 3y6 "我想让你永远属于我。"
    y "我也将永远属于你。"
    y "听上去是不是很棒呢？"
    y 3s "[player]，告诉我。"
    y "告诉我你想成为我的爱人。"
    y "你接受我的感情吗？"

    menu:

#       "imgradeone" "凉凉预警"

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
        y 3y3 "啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈{nw}"
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
                "imgradeone" "{fast}当前进度：[persistent.yurikillround]/1440{fast}"
                y "[gtext]"
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

        $ persistent.yurikillround = 0
        scene black
        show monika at thide zorder 4
        hide monika

    jump yurikill

return