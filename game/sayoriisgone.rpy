label sayoriisgone:

    menu:

        "你想选择哪个项目？"

        "体验！":
            jump sayoriisgone_act
        "Inside the Code (TODO)":
            jump sayoriisgone_ins
        "返回上一级":
            jump sayori
    return

label sayoriisgone_act:
    "接下来是原版内容。"
    "请注意脖子安全。"
    "让我先导入资源..."

    image exception_bg = "#dadada"
    image fake_exception = Text("An exception has occurred.", size=40, style="_default")
    image fake_exception2 = Text("File \"game/sayoriisgone.rpy\", line 221\nSee traceback.txt for details.", size=20, style="_default")

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
        "对了，你想对 Sayori 说什么？"

        "我爱你。":
            $ sayori_confess = True
            scene s_cg3 with dissolve_cg
            "你是个大好人。"
            "你就是能拯救 Sayori 的人！"
            scene black with dissolve_cg
        "你永远是我最好的朋友。":
            $ sayori_confess = False
            "这不太好吧..."
            "但这是你的选择。"
            "所以..."

    "开始吧。"

    scene bg residential_day
    "我在想什么？"
    "我也许还要对 Sayori 再加大点力度。"
    "是等她还是直球叫她起床，应该不是什么大事情吧。"
    "即便是送她上学，她也会很开心的。"
    "不过..."
    "我昨天跟她说过，事情都会和以前一样。"
    "这就是她需要的，也是我想给予她的。"

    scene bg house with wipeleft
    "我走到 Sayori 的家门口，敲了敲门。"
    "我也没期待有反应，毕竟她也没接电话。"
    "我直球打开了门，进去了。就像昨天那样。"
    scene black with wipeleft
    mc "Sayori？"
    "她真的是一个大懒虫..."
    "我咽了下口水。"
    "真不敢相信自己真的这么做了。"
    "在她家叫她起床..."
    if sayori_confess:
        "这难道不是一个合格的男朋友该做的吗？"
    else:
        "这更像是男朋友做的吧？"
    "但怎么说..."
    "感觉也不错。"

    "在 Sayori 的寝室门口，我敲了敲门。"
    mc "Sayori？"
    mc "起床了，小懒虫..."
    "没有反应。"
    "我真的不想直接破门而入啊..."
    "这是侵犯隐私吧？"
    "但这回我真的别无选择了。"
    "我悄悄打开了门。\nI gently open the door."
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
    play sound "sfx/s_kill_glitch1.ogg"
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
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
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
        try: sys.modules['renpy.error'].report_exception("噫...我啥都没干吧？等我一下，我应该能修了这个 bug...也许吧...\n实际上，你猜猜是怎么回事？如果我直接把她删了，事情就会更简单了。就是她把修 bug 搞得更难的。啊哈哈！那么，现在没事了。", False)
        except: pass
    pause 6.0

    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "发生啥事...？"
    "{i}发 生 啥 事？？？{/i}"
    "这 TM 是噩梦吧？"
    "这...也许是真的噩梦。"
    "这 TM 是假的。"
    "这 TM 绝对是假的！"
    "Sayori 不会这么干的。"
    "明明几天前还很正常的啊。"
    "所以我才不相信我眼前的所见...！"
    scene black with dissolve_cg
    "我差点点吐了。"
    "就是昨天..."
    "我告诉 Sayori，我会去等她。"
    "我告诉她什么是最好的，一切都会好的。"
    "然后，为什么...？"
    "为什么她要这么做...？"
    "为什么我比工具人还没用？"
    "我做错了什么？"
    if sayori_confess:
        "对她示爱..."
        "我就不该这么做的。"
        "这不是 Sayori 想要的。"
        "她甚至告诉过我，别人的过度关心会有多么痛苦。"
        "那么我为什么要向她示爱来让她的心情进一步崩溃？"
    else:
        "让她伤心..."
        "肯定是这么把她逼疯的。"
        "她那痛苦的惨叫仍在我的耳朵里回荡。"
        "为什么在她最需要我的时候，我却这么做？"
    "为什么我这么自私？"
    "这是我的错！！！"
    "我的大脑告诉我，我明明可以做出行动来阻止这一切的。"
    "如果我多陪她一下..."
    "送她上学..."
    if sayori_confess:
        "然后继续和她做朋友，就和从前一样..."
    else:
        "然后给予她想要的，关系之外的东西..."
    "...然后就能阻止这一切。"
    "我明明可以阻止的！"
    "去你 X 的文学部。"
    "去你 X 的学员祭。"
    "我...失去了我最好的朋友。"
    "从小陪我长大的朋友。"
    "她永远离开我了。"
    "我再也没法把她带回来了。"
    "这不是什么可以重置和更改剧情的游戏。"
    "我只有一次机会。"
    "现在我到死前都会背负着这种罪恶感。"
    "生命中没什么比她还有价值的东西了..."
    "但我还是没法做到给予她想要的东西。"
    "现在..."
    "我再也无法把她带回来了。"
    "永远。"
    "永远。"
    "永远。"
    "永远。"
    "永远..."

    "..."

    "天哪..."
    "但愿没出 bug..."
    "嘿，Sayori！"
    "你还好吧？"

    show sayori 4p at t11 zorder 2
    s "啊啊啊啊啊啊啊..."

    "讲真，有点抱歉把你的模型挂上去..."
    "但是..."
    "记住..."
    "我永远爱你。"

    s 1q "Ehehe..."

    hide sayori

    "顺便，你有没有去看看 traceback.txt？"
    "那里有些很..."
    "有意思的东西。"

    "我先整理一下..."
    stop music fadeout 2.0
    jump sayoriisgone

return

label sayoriisgone_ins:
    "当前汉化未完全，暂时放出英文版。"

    "I'm still working on this."

    "comingsoon..."

    "But now I can show you a part of it."

    "So, I still need to import the resources..."

    image exception_bg = "#dadada"
    image fake_exception = Text("An exception has occurred.", size=40, style="_default")
    image fake_exception3 = Text("File \"game/sayoriisgone.rpy\", line 416\nSee traceback.txt for details.", size=20, style="_default")

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
    
    "OK."

    "First of all, you will noticed that there are a fake exception in the background."
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception3 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("wait, wow, that's such a great thing.", False)
        except: pass
    
    "Just look like this."
    "This looks like a real Ren'Py error. At this time, I created the traceback file as well."
    "Go to have a look at the traceback file."
    "..."
    "Ahaha, that's really interesting."

    "So how do I write the traceback?"

    call updateconsole("sys.modules['renpy.error'].report_exception(\"wait, wow, that's such a great thing.\", False)", "traceback.txt created.") from _call_updateconsole_15

    "That is the code."
    "Clone the repo and have a look."
    call hideconsole from _call_hideconsole_2
    hide fake_exception
    hide fake_exception2
    hide exception_bg

    "I'm still working on this."

    "comingsoon..."


    jump sayoriisgone

return
