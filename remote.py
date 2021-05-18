import os
import requests
import qrcode
from matplotlib.pyplot import imshow
import numpy as np
import configparser

def watch(QR=False, QRInline=False):
	'''
	Requests a watch code from the server and provides it to the user (ahem, I mean the developer). 
	
	Inputs
	=================
	<optional> QR: If set to True, the watch code is combined with the URL of the Heads-up server and provided as a QR code. 
	               The QR code can be used to directly navigate to the Heads-up watch page and automatically start watching the provided code.
	<optional> QRInline: If you intend to display the QR code on a notebook (with the magic command inline) you should set this to True. 
	                     Make sure you execute watch on the previous notebook cell, before starting your actual code execution. 
						 Otherwise, the QR code will be displayed only after your code finishes execution. I know, it sucks... 	               
				
	Returns
	=================
	peace of mind
	'''
	watch_code = ""
	path = os.path.dirname(os.path.abspath(__file__))
	try: 
		config = configparser.ConfigParser()
		config.read(path + '/config.txt')

		url = config.get('server', 'remote')
		url_watch = config.get('server', 'remote_watch')
		response = requests.post(url, json={"room":"","status":"", "namespace":"n_a_m_e"})
		#print(url)
		if response.status_code == 200:
			if len(response.text) > 0:
				if QR: 
					qr = url_watch + "/" + response.text
					q = qrcode.make(qr)
					if QRInline:
						#%matplotlib inline
						print('inline')
						imshow(np.asarray(q))
					else: 
						q.show()
				print("Visit the Heads-up server and use the following identifier to start watching your code: ")
				print(response.text)
				print("Or just follow the following URL: \n" + url_watch + "/" + response.text)
				
				watch_code = response.text
			else:
				print("Heads-up server did not return a code. Something is not right...")
				watch_code = ''
		else:
			print("Heads-up server is unreachable. Please try again later. If that also fails, curse the administrator.")
			watch_code = ''
	except Exception as ex:
		print("Something went wrong. But what? Look: ", ex)
		pass
	return watch_code

def notify(watch_code, message):
	'''
	Sends a custom message to the Heads-up server for a specific watch code. This code can be acquired by using the "watch" method.
	
	Inputs
	=================
	watch_code: The identifier to input on the Heads-up server to start watching the status of your code execution. 
	            This code can be acquired by using the "watch" method.
				
	Returns
	=================
	peace of mind
	'''
	peace_of_mind = True
	try: 
		path = os.path.dirname(os.path.abspath(__file__))
		config = configparser.ConfigParser()
		config.read(path + '/config.txt')
		url = config.get('server', 'remote')
		response = requests.post(url, json={"room":watch_code,"status":message, "namespace":"n_a_m_e"})
		if response.status_code == 200:
			print('Heads-up server successfully notified. All watchers should receive a headsup!')
		else:
			print('Something went wrong. See if you can make up something from the response status code: ', response.status_code)
	except Exception as ex:
		print("Something went wrong. But what? Look: ", ex)
		pass
	return peace_of_mind