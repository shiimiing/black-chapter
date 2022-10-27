# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = ("hoàn")
define b = ("Minh leader")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #image launch = Movie(play="vid12.mp4", pos=(10, 10), anchor=(0, 0))
    $ renpy.movie_cutscene("Cu (1).webm")


    scene screen :
        size(1920,1080)
    pause

    play music 'audio/mưa.mp3'

    a "Xin chào các bạn đến với dụ án SSg114"
    show model22 at left :
        size(1070,800)
    "..."
    scene leader :
        size(1280,720)
    b "mày chạy dl nhanh lên không tao trừ điểm"
    scene hoan :
        size(1280,720)
    menu :
        a "Để tui suy nghĩ"
        "Đồng ý":
            jump dongy
        "Từ chối":
            jump tuchoi
label dongy:
    scene leader
    b "Giỏi lắm con trai"
    return
label tuchoi:
    scene hoan
    a"Ahhhh~ khó quá chuồn thui hihi"
    scene leader
    b"mày chết với tao!!!"
    return


    return
