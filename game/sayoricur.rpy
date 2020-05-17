label sayoricur:
    
    menu:

        "这是一个定制项设置。你可以启用或禁用 Sayori 的特殊光标。启用后将持续保留该光标，直到你手动禁用。退出游戏后，光标将失效，需要重新启用。"

        "启用特殊光标":
            $ config.mouse = {"default": [
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head.png", 0, 0),
                            ("gui/mouse/s_head.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head2.png", 0, 0),
                            ("gui/mouse/s_head.png", 0, 0),
                            ]}
            jump sayori
        "恢复系统光标":
            $ config.mouse = None
            jump sayori  

return