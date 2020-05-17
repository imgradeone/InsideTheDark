label natjustmonika:

    menu:

        "你想选择哪个项目？"

        "体验！":
            jump natjustmonika_act
#        "EXPERIENCE (Peace ver.)":
#            jump natjustmonika
#        "Inside the Code (TODO)":
#            jump natjustmonika
        "返回上一级":
            jump natsuki

    return

label natjustmonika_act:

    scene bg club_day2
    show natsuki 42c at t11 zorder 2
    with wipeleft_scene
    n "这明显是出于 Yuri 的影响..."
    n "我没意识到你有这么深刻的印象力。"
    n "一直陪伴她在俱乐部..."
    n "现在想像她一样写..."
    n 1s "这样太愚蠢了。"
    n "至少还有 Monika 支持我的作品..."
    n 1r "...啊。"
    n 1q "好吧...我想我现在要和你分享我的诗了。"
    n "我真的很讨厌我必须这样做。"
    n "但不幸的是，我没有太多选择。"
    n 1h "只要...仔细阅读，好吗？"
    n "那你就可以走了。"
    call showpoem(poem_n23, revert_music=False) from _call_showpoem_4
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    stop music
    hide screen tear
    show natsuki ghost_base
    n "我改变了主意。"
    n "请忘记你刚才读的一切。"
    n "尝试做任何事情都是没有意义的。"
    n "Yuri 如此讨人喜欢是她的错。"
    n "你听得到吗，[player]？"
    n "如果你只在 Monika 上花更多的时间，所有这些问题都将消失。"
    n "Yuri 和我都为让像你这样出色的人感到困惑。"
    n "从现在开始，只要想着 Monika 就好了。"
    n "只要 Monika。"
    hide natsuki
    "只要 Monika。"
    menu:
        "只要 Monika。"
        "只要 Monika。":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "只要 Monika。", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "只要 Monika。" with Dissolve(0.5, alpha=True)
    pause 1.0
    stop music
    hide splash_warning
    scene black
    with wipeleft_scene
    $ skip_transition = True

    jump natjustmonika

return