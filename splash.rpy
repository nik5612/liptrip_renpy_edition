image studio_logo = "gui/presplash/file_0586.cbg.png"
image warning = "gui/presplash/file_0582.cbg.png"

label splashscreen:
    scene black

    show warning
    with fade
    pause 5.0

    scene studio_logo
    with fade
    play sound "audio/file_0183.ogg"
    pause 5.0

    return

label before_main_menu:
    play sound "audio/file_0659.ogg"
    return
