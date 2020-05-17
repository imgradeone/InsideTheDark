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

        "Which section do you want?"

        "EXPERIENCE":
            jump natcrush_act
#        "EXPERIENCE (Peace ver.)":
#            jump natcrush
#        "Inside the Code (TODO)":
#            jump natcrush
        "Back to select menu":
            jump natsuki
return

label natcrush_act:

    "OK, Act Start."

    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "...Are you sure this isn't boring for you?"
    n "It's not!"
    mc "Even though you're just watching me read?"
    n "Well...!"
    n "I'm...fine with that."
    mc "If you say so..."
    mc "...I guess it's fun sharing something you like with someone else."
    mc "I always get excited when I convince any of my friends to pick up a series I enjoy."
    mc "You know what I mean?"
    n "...?"
    mc "Hm?"
    mc "You don't?"
    show n_cg1_exp2 at cgfade
    n "Um..."
    n "That's not..."
    n "Well, I wouldn't really know."
    mc "...What do you mean?"
    mc "Don't you share your manga with your friends?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Could you not rub it in?"
    n "Jeez..."
    mc "Ah... Sorry..."
    n "Hmph."
    n "Like I could ever get my friends to read this..."
    n "They just think manga is for kids."
    n "I can't even bring it up without them being all like..."
    n "'Eh? You still haven't grown out of that yet?'"
    n "Makes me want to punch them in the face..."
    mc "Urgh, I know those kinds of people..."
    mc "Honestly, it takes a lot of effort to find friends who don't judge, much less friends who are also into it..."
    mc "I'm already kind of a loser, so I guess I gravitated toward the other losers over time."
    mc "But it's probably harder for someone like you..."
    hide n_cg1_exp3
    n "Hm."
    n "Yeah, that's pretty accurate."
    "{i}...Wait, which part??{/i}"
    $ style.say_dialogue = style.normal
    n "I mean, I feel like I can't even keep it in my own room..."

    $ style.say_dialogue = style.edited
    n "My dad would beat the shit out of me if he found this."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "I don't even know what my dad would do if he found this."
    n "At least it's safe here in the clubroom."
    show n_cg1_exp3 at cgfade
    n "'Cept Monika's kind of a jerk about it..."
    n "Ugh! I just can't win, can I?"
    mc "Well, it paid off in the end, didn't it?"
    mc "I mean, here I am, reading it."
    n "Well, it's not like that solves any of my problems."
    mc "Maybe..."
    mc "But at least you're enjoying yourself, right?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "...So?"
    mc "Ahaha."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Jeez, that's enough!"
    n "Are you gonna keep reading, or what?"
    mc "Yeah, yeah..."
    "I flip the page."
    show black with dissolve_cg
    "..."
    "..."
    "....."
    "......."
    "........."
    "Time passes."
    hide n_cg1_exp3
    show n_cg1_exp4 at cgfade behind black
    "Natsuki is strangely quiet now."
    "I glance over at her."
    hide black with dissolve_cg
    "It looks like she's started to fall asleep."
    mc "Hey, Natsuki..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "Y-Yeah...?"
    "Suddenly, Natsuki collapses straight into me."
    play sound fall
    $ style.say_dialogue = style.normal
    mc "H-Hey--"
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
    m "Oh jeez..."
    m 1d "Natsuki, are you okay?"
    show monika at t21 zorder 2
    show natsuki 12b at f22 zorder 3
    n "..."
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m 1a "Here..."
    show monika at t21 zorder 2
    "Monika reaches into her bag and pulls out some kind of protein bar."
    "She throws it in Natsuki's direction."
    "Natsuki's eyes suddenly light up again."
    "She snatches the bar from the floor and immediately tears off the wrapper."
    show natsuki at f22 zorder 3
    n 1s "I told you not to give mmph..."
    show natsuki at t22 zorder 2
    "She doesn't even finish her sentence before stuffing it into her mouth."
    show natsuki at thide zorder 1
    hide natsuki
    show monika 3b at t11 zorder 2
    m "Don't worry, [player]."
    m "She's fine."
    m "It just happens every now and then."
    m 1a "That's why I always keep a snack in my bag for her."
    m 5a "Anyway...!"
    m "Why don't we all share poems now?"
    scene black
    show monika at thide zorder 2
    hide monika
    jump natcrush

return