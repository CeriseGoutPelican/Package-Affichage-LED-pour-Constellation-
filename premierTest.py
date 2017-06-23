from PIL import ImageFont, ImageDraw, Image

text = "Cerise Gout Pelican"
tiny_font = ImageFont.truetype("fonts/PX437_FONT.ttf", 5)
w,h  = tiny_font.getsize(text)

image = Image.new("1", (w, h), "black")
draw = ImageDraw.Draw(image)

draw.text((0, 0), text, fill="white", font=tiny_font)

image.show()

pixels = image.load()
print 'const char pixels[] = {'
w, h = image.size 

for y in range(h):
	print '\t',
	for x in range(w):
		print pixels[x,y], ',',
	print
print '};'
