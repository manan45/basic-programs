def draw_line(tick_length, tick_label= ""):
	line = '-' * tick_length
	if tick_label:
		line += ' ' + tick_label
	print(line)
	return None

def draw(center_length):
	if center_length > 0:
		draw(center_length-1)
		draw_line(center_length)
		draw(center_length-1)
	return None

def draw_ruler(num_inches, major_length):
	draw_line(major_length, '0' ) # draw inch 0 line
	for j in range(1, 1 + num_inches):
		draw(major_length - 1) # draw interior ticks for inch
		draw_line(major_length, str(j))
	return None


draw_ruler(15,2)