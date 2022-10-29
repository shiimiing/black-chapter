# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define main = ("Vương Tú Trà Vy")
define class = ('')
define classmate = ('Bạn học')




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #image launch = Movie(play="vid12.mp4", pos=(10, 10), anchor=(0, 0))
    $ renpy.movie_cutscene("Cu (1).webm")


    play music 'audio/mưa.mp3'
    stop music fadeout 10.0
label lam_quen:
    $ player = renpy.input('Nhập tên nhân vật: ', exclude='1234567890!@#$%^&*()_+-=[];,./\{}|:"<>?"')
    scene school:
        size(1920,1080)
    with fade
    'Vì lí do công tác của bố mẹ nên [player] đã phải chuyển trường khá nhiều lần, và lần này cũng vậy.'
    'Bạn chuyển đến một ngôi trường mới, với lớp mới và bạn mới.'
    scene classroom
    with dissolve
    play music 'audio/lop (online-audio-converter.com).mp3'

    player 'Xin chào mọi người, mình là [player], mong được mọi người giúp đỡ'

    play sound 'audio/clapping (online-audio-converter.com).mp3'
    'Cả lớp vỗ tay, chào đón [player]'
    show classmate1 at right with moveinright
    show classmate2 at left with moveinleft
    'classmate2' 'ui bn dep try the, cho minh lam quen voi'
    'Trong lớp ai ai cũng thân thiện và hòa đồng.'
    scene classroom_main:
        size(1902,1080)
    stop music
    with fade
    'Bạn nhìn xuống góc lớp và thấy 1 cô gái đang ngồi 1 mình'
    'Bạn quyết định bắt truyện với cô gái ấy'
    show main
    player 'Xin chào!'
    '???' 'ừ chào cậu'
    player 'Cậu tên là gì thế'
    '???' 'Mình tên là...'
    hide main
    show classmate1
    classmate '[player] đi thôi'
    hide classmate1
    player 'Ừm RA NGAY ĐÂY'
    player 'Tí chúng ta nói chuyện sau nhé'
    scene hanhlang:
        size(1920,1080)
    with dissolve
    show classmate1 at right
    show classmate2 at left
    'classmate1' 'Cậu bắt chuyện với nó làm gì, cái đứa lập dị đó'
    player 'Lập dị?'
    'classmate2' 'Nó suốt ngày chỉ im lặng ngồi 1 góc, chả thèm nói chuyện với ai, xong thỉnh thoảng cứ làm cái gì ấy'
    player 'Vậy hả...'
    'classmate2' 'Nghe bảo tính nó cũng không tốt nên bạn bè trước của nó cũng không chơi nổi với nó.'
    'classmate 2' 'Lúc nãy cậu bắt chuyện với nó nó còn không thèm trả lời. Chảnh.'
    player '...'
    'classmate1' 'Đúng rồi, hồi trước nó toàn bắt H trả tiền hộ nó. Xong còn nói xấu hoa khôi lớp mình.'
    scene black
    with dissolve
    '[player] vừa đi vừa ngẫm...'
    'Một lúc sau, trống vào tiết vang lên,[player] cùng đám đến nhà thể chất học thể dục'
    scene theduc:
        size(1920,1080)
    with fade
    'Tiết thể dục, [main] vẫn như mọi khi, ngồi 1 mình, còn [player] thì được bao quanh bởi bạn bè mới'
    menu:
        'Đến chỗ A đang ngồi và bắt chuyện':
            jump noi
        'Tiếp tục nói chuyện với bạn':
            jump ko_noi
label ko_noi:
    '[player] nhìn lướt qua [main] rồi lại tiếp tục nói chuyện với đám bạn'
    jump het_tiet
label noi:
    call variable
    $ chance+=1
    '[player] quyết định ra chỗ [main] xem sao'
    player 'Tớ ra chỗ [main] tí nhé'
    show classmate
    'classmate1' 'Cậu ra đấy làm gì?'
    player 'Thì tớ thấy cậu ấy trông hơi cô đơn'
    'classmate2' 'Bọn tớ khuyên cậu là không nên đi. Đừng dây vào nó'
    player 'Ahihi, tớ đi tí thôi'
    hide classmate
    'Mặc kệ lời kêu của đám bạn, [player] vẫn quyết định đến bắt chuyện với A'
    player '...'
    main '...'
    player '...'
    jump het_tiet
    #lời dẫn đến hết giờ
label het_tiet:
    call variable
    scene classroom_afternoon
    'Tan học, [main],[player] và một số bạn nữa được phân công ở lại trực nhật'
    show classmate
    'classmate' '[player] ơi, làm hộ bọn tớ hôm nay được không, bọn tớ có tí việc'
    player 'Được thôi, nhưng chỉ hôm nay thôi nhé'
    'classmate' 'Ok ok, cảm ơn nha'
    hide classmate
    'Sau khi đám bạn về hết, trong lớp chỉ còn [main] với [player]...'
    '...'
    if chance<1:
        'Trong lớp giờ chỉ còn [main] và [player]'
        'Hai người không ai nói chuyện với ai, chỉ còn tiếng quét dọn của chổi quét'
        'Làm xong, 2 người ai về nhà nấy, không nói 1 câu'
        scene black with dissolve
        'Và sau đó, cuộc sống vẫn diễn ra bình thường'
        'G có vẻ đã trở thành một phần không thể thiếu trong nhóm bạn'
        'A thì vẫn vậy, vẫn là một người lập dị ở trong lớp'
        jump dream
    else:
        show main
        main 'Chúng nó không phải bọn tốt lành gì đâu'
        player 'Hả, là sao?'
        main '...'
        hide main
        'Sau đó [main] im lặng, tiếp tục quét lớp như chưa có chuyện gì xảy ra'
        '[player] vẫn đang chìm trong câu nói của [main]'
        player '{i}Không tốt lành? Ai không tốt lành cơ? Mấy đứa kia á? Tại sao?'
        '[main] tiếp tục im lặng cho đến khi về'
label dream:
    'Cứ như vậy cho đến một ngày…'
    scene classroom_rain:
        size(1920,1080)
    play music 'audio/mưa.mp3'
    with dissolve
    'Đó là một ngày hơi âm u, dự báo trời sẽ rét lạnh và mưa phùn'
    'G như mọi khi, đến lớp và gia nhập vào nhóm bạn của mình'
    'Trống vào tiết, GVCN bước từng bước nặng nề đi vào lớp, không gian ồn ào trở nên im lặng.'
    'Không hiểu sao [player] lại quay sang nhìn chiếc bàn trống kia, đó là chỗ của [main]'
    player 'Hôm nay cậu ấy không đi học…'
    'Ngoài trời bắt đầu lớt phớt đổ mưa, từng cơn gió thổi mang theo tiếng rít gào đập vào cửa sổ'
    'Tổng thể tạo nên một không gian lớp học vô cùng quỷ dị'
    '[player] bỗng thấy ớn lạnh, da gà nổi hết cả lên, một dự cảm không lành trào tới'
    show GVCN
    'gvcn' 'Hôm nay cô muốn thông báo với lớp mình 1 tin buồn'

    play music 'audio/eheheee (1).mp3'

    'gvcn' 'Đó là tối qua, bạn [main] được phát hiện đã qua đời trong chính phòng ngủ của mình'
    'gvcn' 'Nguyên nhân hiện chưa xác đinh được.'
    'gvcn' 'Sáng mai 9h sẽ tổ chức đưa hoa tiễn, lớp mình nhớ mặc đồ đen, đến đúng giờ.'
    hide GVCN with dissolve
    'Nhìn tấm di ảnh, [player] bỗng thấy khó chịu, bức bối đến lạ, không vì một lí do nào cả, chỉ cảm thấy có một thứ gì đó rất khó nói thành lời'
    'Nó cứ nghẹn ở trong lòng cậu, bức bối đến lạ thường'

    stop music
    scene black with irisin
    'Đột nhiên, không gian xung quanh cậu bị bao trùm bởi màu đen'
    player 'CHUYỆN GÌ ĐANG XẢY RA VẬY???'
    '[player] hoảng loạn nhìn xung quanh, cậu tiến về phía trước, cậu thử quơ tay xung quanh'
    player 'Không có gì cả...'
    'Bỗng cơ thể cậu chạy về phía trước, cứ chạy cứ chạy mà không có mục đích gì'
    '[player] muốn dừng lại, nhưng không sao dừng được. Cơ thể cậu như thuộc về người khác. Nó không thể theo sự điều khiển của cậu.'
    'Sự căng thẳng, sợ hãi, hoảng loạn ngày càng dồn dập...'
    stop music fadeout 10.0
    scene tunnel:
        size(1920,1080)
    with fade
    'Chợt 1 chùm sáng lóe lên, nó ở ngay phía trước, và cơ thể [player] đang chạy về phía đó'
    'Sáng dần, sáng dần, sáng dần. Nó nuốt chửng cậu'
    scene white:
        size(1920,1080)
    with irisout
    '???' 'Này đợi tớ với'
    '[player] giật mình sau tiếng gọi'
    'Còn đang chưa hiểu gì thì [player] bỗng thấy 1 khuôn mặt quen thuộc'
    'Bạn' 'Nhanh lên đi'
    main 'Đây đây, xong rồi đây'
    'Bạn' 'Cậu lâu quá đấy'
    main 'Xin lỗi xin lỗi'

label variable:
    $ i=1
    $ chance=0
    return
