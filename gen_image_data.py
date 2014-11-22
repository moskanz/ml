from PIL import Image, ImageDraw, ImageFont
import string, os, random
size = (50,50)
f = open('data/workfile.dat', 'w')
for back_color in range(0,255):	
	for font_color in range(0,255):
		if font_color == back_color:
			continue
		for font_file in os.listdir("fonts"):
			print font_file
			for char in string.ascii_lowercase:
				print char
				for angle in range(-45,45):
					im = Image.new('RGB', size, color = (back_color,back_color,back_color)) # create the image
					draw = ImageDraw.Draw(im)
					red = (font_color,font_color,font_color)    # color of our text
					text_pos = (5,5) # top-left position of our text
					text = char # text to draw
					font = ImageFont.truetype("fonts/%s" % font_file, 40)
					# Now, we'll do the drawing: 
					draw.text(text_pos, text, fill=red, font=font)
					im = im.rotate(angle)
					#file_name = 'data/test_f%s_c%s_a%d.png' % (font_file,char,angle)
					example = char
					for i in range(0,50):
						for j in range(0,50):
							example += ' ' + str(int(round(sum(im.getpixel((i, j))) / 3)))
							#example += ' ' + ' '.join(map(str,im.getpixel((i, j))))
					#print example
					f.write(example + '\n')
					#im.save(file_name, 'PNG')