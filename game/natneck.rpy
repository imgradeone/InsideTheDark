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

        "Which section do you want?"

        "EXPERIENCE":
            jump natneck_act
        "EXPERIENCE (Peace ver.)":
            jump natneck_peace
#        "Inside the Code (TODO)":
#            jump natneck
        "Alt Version by imgradeone":
            jump natneck_alt
        "Back to select menu":
            jump natsuki

return

label natneck_act:

    "OK, let's play with Natsuki."
    scene bg club_day
    with dissolve_scene_full
    show natsuki 1g at t11 zorder 3
    $ style.say_dialogue = style.edited
    n "[player]..."
    n "Why didn't you come read with me today?"
    n 1m "I was waiting for you."
    n "I was waiting for a long time."
    n "It was the only thing I had to look forward to today."
    n "Why did you ruin it?"
    n "Do you like Yuri more?"
    n 1k "I think you're better off not associating with her."
    n "Are you listening to me?"
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
    n ghost1 "Yuri is a sick freak."
    n "That should be obvious by now."
    n "So just play with me instead."
    n "Okay?"
    n "You don't hate me, [player], do you?"
    n "Do you hate me?"
    show natsuki_ghost_blood zorder 3
    n "Do you want to make me go home crying?"
    n "The club is the only place I feel safe."
    n "Don't ruin that for me."
    n "Don't ruin it."
    n "Please."
    n "Just stop talking to Yuri."
    n "Play with me instead."
    n "It's all I have..."
    n "Play with me."
    stop music
    hide n_rects_ghost3
    n ghost2 "PLAY WITH ME!!!"
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
    "This is a still work-in-progress peace ver."
    scene bg club_day
    with dissolve_scene_full
    show natsuki 1g at t11 zorder 3
    $ style.say_dialogue = style.edited
    n "[player]..."
    n "Why didn't you come read with me today?"
    n 1m "I was waiting for you."
    n "I was waiting for a long time."
    n "It was the only thing I had to look forward to today."
    n "Why did you ruin it?"
    n "Do you like Yuri more?"
    n 1k "I think you're better off not associating with her."
    n "Are you listening to me?"
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    n ghost1 "Yuri is a sick freak."
    n "That should be obvious by now."
    n "So just play with me instead."
    n "Okay?"
    n "You don't hate me, [player], do you?"
    n "Do you hate me?"
    n "Do you want to make me go home crying?"
    n "The club is the only place I feel safe."
    n "Don't ruin that for me."
    n "Don't ruin it."
    n "Please."
    n "Just stop talking to Yuri."
    n "Play with me instead."
    n "It's all I have..."
    n "Play with me."
    stop music
    n ghost2 "PLAY WITH ME!!!"
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
    "Yep, this is my own made version, but very suk."

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