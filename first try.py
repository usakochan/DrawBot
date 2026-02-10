size(500, 500)

print("w:", width())
print("h:", height())

rect(200, 100, 100, 300)
oval(50, 350, 100, 100)
polygon((375, 475), (400, 450), (400, 350), (350, 400), close=False)

# create path
newPath()

moveTo((350, 20))
lineTo((380, 30))
curveTo((400, 80), (450, 150), (400, 230))
lineTo((330, 180))

# close the path
closePath()
# draw the path
drawPath()



newPage(900, 900)

font('Fredoka', 100)
text('He is smiling!', (000, 50))