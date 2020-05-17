label horrorintro:
    $ config.allow_skipping = True
    stop music fadeout 2.0

    scene bg residential_day
    with dissolve_scene_full
    play music t2
    pause 2.0

    "imgradeone" "那么..."
    "imgradeone" "欢迎来到 Inside The Dark mod。"
    "imgradeone" "我是 mod 作者，imgradeone。"
    "imgradeone" "你应该蛮享受 DDLC 吧，尽管它有那么{i}亿点点{/i}...恐怖？"
    "imgradeone" "呃呵呵..."
    "imgradeone" "所以这个 mod 可能会伤害到你。"
    "imgradeone" "但这一次，我们会深入代码。"
    "imgradeone" "所以，确保自己已经从 https://github.com/imgradeone/InsideTheDark 克隆代码以便学习。"
    "imgradeone" "不过，如果你只是想来体验一下恐怖的 DDLC 的话..."
    "imgradeone" "那么..."
    menu:
        "imgradeone" "您打出真结局来了吗？"
        "是":
            "imgradeone" "..."
            pass
        "否":
            "imgradeone" "..."
            "imgradeone" "XD"
            pass
    "imgradeone" "那么准备进入 mod 吧！"
    "imgradeone" "等等..."
    "imgradeone" "口意..."
    "imgradeone" "我忘记说我是个 mod 菜鸡了..."
    "imgradeone" "这个 mod 可能完成度极低，并且充满 BUG。"
    "imgradeone" "抱歉..."
    "imgradeone" "不过，四个阔爱的妹子也会加入这个 mod。"
    "imgradeone" "我会好好照顾她们的。"
    "imgradeone" "那么，有请 DDLC 天团出场！"
    "imgradeone" "你好！"

    $ t45 = t11

    show monika 1a at t45 zorder 4
    m "嗨，mod 作者！你好，[player]！"
    m 1b "我会一直爱你的呐！"
    m 5a "祝你好运！"
    show monika at thide zorder 4
    hide monika

    show natsuki 1a at t45 zorder 4
    $ style.say_dialogue = style.edited
    n 4x "WDNMD，嘿，mod 作者，听说你喜欢写 BUUUUUUUUUUUUUG？"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "我的天啊，imgradeone，你这个愚蠢的土拨鼠又在写 bug 了..."
    n 1b "..."
    n 1c "..."
    n "刚刚发生了什么..."
    show natsuki at thide zorder 4
    hide natsuki

    show yuri 1a at t45 zorder 4
    $ style.say_dialogue = style.edited
    y 3y3 "啊哈↓↓↓↓↓↓↓哈↓↓↓↓↓哈↓↓↓↓↓哈↓↓↓↓哈↓↓↓哈↓↓哈↓"
    $ style.say_dialogue = style.normal
    y "..."
    y 1c "..."
    y "啥啊...？"
    y "我咋变成..."
    $ style.say_dialogue = style.edited
    y 3y3 "疯nggggggggggggggggg子iiiiiiiiiiii了eeeeeeeeeee？！"
    show yuri at thide zorder 4
    hide yuri

    show sayori 1a at t45 zorder 4
    $ style.say_dialogue = style.normal
    s "..."
    s 4p "噫啊啊啊啊啊啊啊啊啊！"
    show sayori at thide zorder 4
    hide sayori

    show natsuki vomit at t45 zorder 4
    n "哇啊啊啊啊啊啊啊啊啊啊啊啊啊！"
    n "Yuri 你咋了？？？"
    show natsuki at thide zorder 4
    hide natsuki

    "imgradeone" "是的，我又犯传统艺能了..."
    "imgradeone" "这也许是你游最烂的 mod..."
    "imgradeone" "吧..."

    mc "嘿，发生啥事？？"
    show monika 1a at t45 zorder 4
    m "..."
    show monika at thide zorder 4
    hide monika

    "imgradeone" "让我修一下 bug..."
    "imgradeone" "现在就和没事一样了。"
    "imgradeone" "现在可以进入最糟糕的部分了..."

    "imgradeone" "顺便重申一下，所有角色的文件都会安全地保存。"
    "imgradeone" "那么..."
    "imgradeone" "爱你们喵！"

    $ persistent.example_seen = True

    jump horrormenu

    return

label horrormenu:
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0

    menu:
        "imgradeone" "请选择你今天想要迫害的角色。"

        "Sayori":
            jump sayori
        "Yuri":
            jump yuri
        "Natsuki":
            jump natsuki
        "重播首次启动的故事":
            jump horrorintro
#       "Credits (in dev)":
#           jump creditofitd
        "返回主菜单":
            return
    return