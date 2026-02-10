#size(300, 300)
#size(300, 300)のままだとサイズがちっさかったな！png/jpgだとひどい出来上がりだ...
scale_factor = 4
newPage(300 * scale_factor, 300 * scale_factor)
scale(scale_factor)

#選好の幅
fill(1)
stroke(0)
strokeWidth(5)
line((50, 250), (250, 250))
line((100, 190), (250, 190))
line((100, 130), (200, 130))
line((150, 70), (200, 70))

#各フォント
fill(0)
strokeWidth(1)#上のwidth5が生きているので囲いをなしにしたい
##生き残り君たち
oval(90, 240, 20, 20)
oval(140, 240, 20, 20)
oval(190, 240, 20, 20)
oval(240, 240, 20, 20)

oval(90, 180, 20, 20)
oval(140, 180, 20, 20)
oval(190, 180, 20, 20)

oval(140, 120, 20, 20)
oval(190, 120, 20, 20)

##脱落ちゃんたち
fill(.6)
oval(40, 240, 20, 20)
oval(240, 180, 20, 20)
oval(90, 120, 20, 20)
oval(190, 60, 20, 20)

##決定さま
fill(0)
stroke(1, 0, 1)
oval(140, 60, 20, 20)

#まるばつ
##まる
strokeWidth(1)
stroke(0)#ピンクより黒の方が見やすかったですわ
fill(1)
#ピンクfillが生きているので白に設定
oval(245, 265, 10, 10)
oval(95, 205, 10, 10)
oval(195, 145, 10, 10)
oval(195, 145, 10, 10)
oval(145, 85, 10, 10)

##ばつ
strokeWidth(2)
stroke(.45)#以外と.6だと薄かったので少し濃く
line((45, 265), (55, 275))
line((45, 275), (55, 265))

line((245, 205), (255, 215))
line((245, 215), (255, 205))

line((95, 145), (105, 155))
line((95, 155), (105, 145))

line((95, 145), (105, 155))
line((95, 155), (105, 145))

line((195, 85), (205, 95))
line((195, 95), (205, 85))


#数値
font("fredoka", 20)
stroke(0.3)
strokeWidth(1)
text('1', (20, 245))
text("2", (20, 185))
text('3', (20, 125))
text("4", (20, 65))

font("Zen Maru Gothic")
fill(1, 0, 1)
strokeWidth(0)
textBox("決定", (125, 5, 50,50), align="center")

saveImage('~/Pictures/logic.jpg')