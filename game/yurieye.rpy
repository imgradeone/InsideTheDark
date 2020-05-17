label yurieye:
    menu:

        "你想怎么感受 Yuri 的三次元之眼？"

        "体验！（原版）":
            jump yurieye_original

        "体验！（开灯版）":
            jump yurieye_alt

        "返回上一级":
            jump yuri

return

label yurieye_original:

    "好的，那么开始吧！"

    scene bg closet
    show yuri 2t at t11 zorder 2
    with wipeleft
    y "[player]..."
    play sound closet_close
    show dark zorder 100
    with wipeleft
    y "我的心..."
    y 2y6 "我的心不会停止跳动的，[player]..."
    y "我冷静不下来。"
    y "我再也没法专注于任何东西了...!"
    y "[player]，你感觉到了吗？"
    "Yuri 突然把我的手按在她的胸前。"
    play music hb
    show layer master at heartbeat
    y 3t "为什么这发生在我身上？"
    y "就像失去自我意识..."
    y 3y4 "我停不下来了。"
    y 3y6 "我甚至不想读书了..."
    y "我只想..."
    y 3s "...看着..."
    y "...你。"
    hide yuri
    show yuri eyes
    pause 3.0
    y "...哈..."
    pause 3.0
    y "...哈..."
    pause 3.0
    y "...哈..."
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
    m "emm..."
    m "是时候...分享写的诗了..."

    scene black
    show monika at thide zorder 4
    show yuri at thide zorder 2
    hide monika
    hide yuri
    $ persistent.yurieye_seen = True
    jump yurieye

return

label yurieye_alt:

    "嗯..."
    "你应该是认真的。"
    "那么，开始吧。"

    scene bg closet
    show yuri 2t at t11 zorder 2
    with wipeleft
    y "[player]..."
    play sound closet_close
    y "我的心..."
    y 2y6 "我的心不会停止跳动的，[player]..."
    y "我冷静不下来."
    y "我再也没法专注于任何东西了...!"
    y "[player]，你感觉到了吗？"
    "Yuri 突然把我的手按在她的胸前。"
    play music hb
    show layer master at heartbeat
    y 3t "为什么这发生在我身上？"
    y "就像失去自我意识..."
    y 3y4 "我停不下来了。"
    y 3y6 "我甚至不想读书了..."
    y "我只想..."
    y 3s "...看着..."
    y "...你。"
    hide yuri
    show yuri eyes
    pause 3.0
    y "...哈..."
    pause 3.0
    y "...哈..."
    pause 3.0
    y "...哈..."
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
    m "emm..."
    m "是时候...分享写的诗了..."

    scene black
    show monika at thide zorder 4
    show yuri at thide zorder 2
    hide monika
    hide yuri

    $ persistent.yurieye_seen = True

    jump yurieye

return