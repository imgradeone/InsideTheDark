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

label natcrush:

    menu:

        "你想选择哪个项目？"

        "体验！":
            jump natcrush_act
#        "EXPERIENCE (Peace ver.)":
#            jump natcrush
#        "Inside the Code (TODO)":
#            jump natcrush
        "返回上一级":
            jump natsuki
return

label natcrush_act:

    "好的，演出开始。"

    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "...你确定那样不会无聊吗？"
    n "不会！"
    mc "即使你只是看我读着？"
    n "额...！"
    n "我认为...这样很好。"
    mc "如果你这样说..."
    mc "...我想与他人分享你喜欢的东西很有趣。"
    mc "当我说服任何一个朋友挑选我喜欢的系列时，我总是会感到兴奋。"
    mc "你明白我的意思吧？"
    n "...？"
    mc "嗯？"
    mc "你不明白？"
    show n_cg1_exp2 at cgfade
    n "嗯..."
    n "那样不是..."
    n "好吧，我不会真正地明白。"
    mc "...你这是什么意思？"
    mc "难道你没有把漫画分享给你的朋友过吗？" # Don't you share your manga with your friends?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "你不能忘记那件事吗？"
    n "真是的..."
    mc "啊... 对不起..."
    n "哼。"
    n "说的像是我说服了我的朋友们读那一篇一样..."
    n "他们只觉得漫画是给小孩子看的。"
    n "如果他们都不喜欢的话，我甚至无法提开主题。"
    n "”额？你还没脱离那个想法吗？“"
    n "说得让我想一拳凹进他们的脸皮里..."
    mc "呃，我认识那种人。"
    mc "老实说，要找到不做判断的朋友，要花很多心血..."
    mc "我已经是一个失败者，所以我想，随着时间的流逝，我已然倾向于其他的失败者了。"
    mc "但是对像你这样的人来说可能更难..."
    hide n_cg1_exp3
    n "嗯。"
    n "是的，这很准确。"
    "{i}...等等，是哪一部分？{/i}"
    $ style.say_dialogue = style.normal
    n "我是说，我觉得我甚至不能把它放在自己的房间里。"

    $ style.say_dialogue = style.edited
    n "如果我爸发现了这个，他会打{i}屎{/i}我。"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "我甚至不知道，如果我爸发现了那个，会做什么。"
    n "至少在俱乐部房间里是安全的。"
    show n_cg1_exp3 at cgfade
    n "除了 Monika，对将那个寄放在房间里的态度有点古怪..."
    n "啊！我就是赢不了，————难道我赢得了吗？"
    mc "好吧，最终因那件事得到了代价，不是吗？"
    mc "我的意思是，我在这里，读着它。"
    n "好吧，这并不能解决我的任何问题。"
    mc "也许吧..."
    mc "但是至少你玩的开心，对吧？"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "————"
    n "..."
    n "...所以呢？"
    mc "啊哈哈。"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "真是的，够了！"
    n "你到底是要读那本书，还是有别的目的？"
    mc "是啊..."
    "我翻了一页又一页。"
    show black with dissolve_cg
    "..."
    "..."
    "....."
    "......."
    "........."
    "时间在消逝。"
    hide n_cg1_exp3
    show n_cg1_exp4 at cgfade behind black
    "Natsuki 现在古怪地安静下来了。" # is strangely quiet now."
    "我瞥了她一眼。"
    hide black with dissolve_cg
    "看来她开始入睡了。"
    mc "嘿，Natsuki..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "...有？"
    "突然，Natsuki 径直陷入了我。" # 或是崩溃？
    play sound fall
    $ style.say_dialogue = style.normal
    mc "嘿！嘿————"
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base

    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r at t11 zorder 2
    m "哦，天..."
    m 1d "Natsuki，你还好吗？"
    show monika at t21 zorder 2
    show natsuki 12b at f22 zorder 3
    n "..."
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m 1a "来..."
    show monika at t21 zorder 2
    "Monika 伸进她的包里，掏出某种蛋白质棒。"
    "她把它扔向 Natsuki 的方向。"
    "Natsuki 的眼睛突然又发亮起来了。"
    "她从地板上抓住那条棒，并立即撕下了包装纸。"
    show natsuki at f22 zorder 3
    n 1s "我告诉过你不要给我————"
    show natsuki at t22 zorder 2
    "在收回那个句子之前，她甚至还没有说完它。"
    show natsuki at thide zorder 1
    hide natsuki
    show monika 3b at t11 zorder 2
    m "不用担心她，[player]。"
    m "她还好。"
    m "发生那种事情只是偶然的。"
    m 1a "这就是为什么我总是为她在我的包里准备零食。"
    m 5a "不管了...！"
    m "我们现在为何不来分享诗呢？"
    scene black
    show monika at thide zorder 2
    hide monika
    jump natcrush

return
