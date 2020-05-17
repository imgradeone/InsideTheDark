init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight

            for i in range(self.numRects):
                self.add(self.displayable)
           
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
            
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0


image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natneck:

    menu:

        "你想选择哪个项目？"

        "体验！":
            jump natneck_act
        "体验！（和平版）":
            jump natneck_peace
#        "Inside the Code (TODO)":
#            jump natneck
        "Alt Version by imgradeone":
            jump natneck_alt
        "返回上一级":
            jump natsuki

return

label natneck_act:

    "好的，那就和 Natsuki 玩吧。"
    scene bg club_day
    with dissolve_scene_full
    show natsuki 1g at t11 zorder 3
    $ style.say_dialogue = style.edited
    n "[player]..."
    n "为什么你今天不陪我一起看书？"
    n 1m "我一直在等着你。"
    n "我等你等得很久了！"
    n "这是我今天唯一期待的事情。"
    n "你为什么要毁了它？？"
    n "难道你更喜欢 Yuri？"
    n 1k "我强烈建议你远离她。"
    n "喂，你有在听吗？"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    n ghost1 "Yuri 就 TM 一死病娇。"
    n "现在这一点特别明显了。"
    n "所以还是陪我玩吧。"
    n "好伐？"
    n "[player]，你不恨我吧？"
    n "你恨我吗？"
    show natsuki_ghost_blood zorder 3
    n "难道你 TM 想让我哭着回家？"
    n "文学部是我唯一感觉安全的地方。"
    n "不要毁了它。"
    n "千万不要毁了它。"
    n "求你了。"
    n "不要再和 Yuri 聊天了。"
    n "要陪我玩。"
    n "我要说的就这么多了..."
    n "陪我玩。"
    stop music
    hide n_rects_ghost3
    n ghost2 "{b}快来陪我玩！！！{/b}"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 at i11 onlayer front
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    pause 0.5
    show end:
        xzoom -1
    with dissolve_cg
    pause 2.0
    scene black
    with None
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    scene black
    jump natneck


return

label natneck_peace:
    "这是开发仍在进行的和平版。"
    scene bg club_day
    with dissolve_scene_full
    show natsuki 1g at t11 zorder 3
    $ style.say_dialogue = style.edited
    n "[player]..."
    n "为什么你今天不陪我一起看书？"
    n 1m "我一直在等着你。"
    n "我等你等得很久了！"
    n "这是我今天唯一期待的事情。"
    n "你为什么要毁了它？？"
    n "难道你更喜欢 Yuri？"
    n 1k "我强烈建议你远离她。"
    n "喂，你有在听吗？"
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    n ghost1 "Yuri 就 TM 一死病娇。"
    n "现在这一点特别明显了。"
    n "所以还是陪我玩吧。"
    n "好伐？"
    n "[player]，你不恨我吧？"
    n "你恨我吗？"
    n "难道你 TM 想让我哭着回家？"
    n "文学部是我唯一感觉安全的地方。"
    n "不要毁了它。"
    n "千万不要毁了它。"
    n "求你了。"
    n "不要再和 Yuri 聊天了。"
    n "要陪我玩。"
    n "我要说的就这么多了..."
    n "陪我玩。"
    stop music
    n ghost2 "{b}快来陪我玩！！！{/b}"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    show natsuki ghost3
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 at i11 onlayer front
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    scene black
    with None
    window auto
    scene black
    pause 0.5
    show end:
        xzoom -1
    with dissolve_cg
    pause 2.0
    scene black
    with None
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    scene black
    jump natneck
return

label natneck_alt:
    "Yep, this is my own made version, but very suck."

    scene bg club_day2

    show natsuki 1g at t11 zorder 3
    n "[player]..."
    n "Why did you download this mod?"
    n "You know what?"
    n 2b "This is the suckest mod ever."
    n "Why did you consider it?"
    n 3f "You should delete the mod now."
    $ style.say_dialogue = style.edited
    n "Or my dad would beat the shit out of me if he found this."
    $ style.say_dialogue = style.normal
    n scream "Ahhhh..."
    n "Something went wrong..."
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    stop music
    hide screen tear
    n ghost_base "Finally..."
    n "The worst time..."
    n "...is COMING!!!!"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    show natsuki ghost3
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 at i11 onlayer front
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    scene black
    with None
    window auto
    scene black
    pause 0.5
    show end:
        xzoom -1
    with dissolve_cg
    pause 2.0
    scene black
    with None
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    scene black
    jump natneck

    return 