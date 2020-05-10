label sayoricur:
    
    menu:

        "This is a customizable setting. You can enable or disable Sayori's special cursor. This will be kept until you disable it, and will be reset to Disable when you exit the mod."

        "Enable":
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
        "Disable":
            $ config.mouse = None
            jump sayori  

return