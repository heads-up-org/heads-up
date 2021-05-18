from playsound import playsound
import time
from pynput import keyboard
from pynput import mouse
import os


def headsup(soundname='Bsmith44.wav', loop=False):
	'''
	This method simply plays a soundfile when called. Why? I'll tell you why.
	Your code is training a model, or processing data. You do not know when it will finish and this feeling eats you inside.
	You want to enjoy Netflix on your couch but something in your mind tells you to check the code. 
	No more... From now on, you are in control here!  Just call this method at the end of your code, turn on the speaker volume, and be sure that you will be notified.
	
	Inputs
	========================
	<optional> soundname: The full path to your sound file, or the name of a file in the sounds folder.
	<optional> loop: If set to True, your sound file will keep playing until you somehow interact with your computer via keyboard or mouse.
	
	Returns=================
	peace of mind.
	'''
	peace_of_mind = True
	if "/" in soundname or "\\" in soundname:
		path = ''
	else:
		path = os.path.dirname(os.path.abspath(__file__)) + "/sounds/"
	
	try:
		if loop:
			global keyboard_listener 
			global mouse_listener 
			keyboard_listener = keyboard.Listener(on_press=on_press)
			mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
			keyboard_listener.start()
			mouse_listener.start()
			while keyboard_listener.is_alive() and mouse_listener.is_alive():    
				playsound(path + soundname)
				time.sleep(5)
		else:
			#print(path + soundname)
			playsound(path + soundname)
	except Exception as ex:
		print(ex)
	return peace_of_mind



############ User Activity Detection Methods.
def mouseAction():
	#print('mouse_action')
	#mouse.Listener.stop
	stopListeners()
	return False

def on_move(x, y):
	#print('mouse_move')
	#mouse.Listener.stop
	stopListeners()
	return False

def on_click(x, y, button, pressed):
	#print('mouse_click')
	#mouse.Listener.stop
	stopListeners()
	return False
	if not pressed:
		# Stop listener
		return False

def on_scroll(x, y, dx, dy):
	#print('mouse_scroll')
	#mouse.Listener.stop
	stopListeners()
	return False

def on_press(key):
	try:
		#print('alphanumeric key {0} pressed'.format(key.char))
		pass
	except AttributeError:
		#print('special key {0} pressed'.format(key))
		pass
	#keyboard.Listener.stop
	stopListeners()
	return False

def on_release(key):
	#print('{0} released'.format(key))
	if key == keyboard.Key.esc:
		# Stop listener
		return False
	#keyboard.Listener.stop
	stopListeners()
	return False 

def stopListeners():
	#print('stopping') 
	keyboard_listener.stop()
	mouse_listener.stop()