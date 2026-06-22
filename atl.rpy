image wide_bg = "images/bgs/file_0120.cbg.png"

transform pan_right_stop:
    xalign 0.0 yalign 0.5  # Начинаем с левого края, центрируем по высоте
    linear 20.0 xalign 1.0 # Плавно едем к правому краю ровно 10 секунд
    # После этого команда linear заканчивается, и картинка просто замирает.

