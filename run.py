import eel
import requests
from telebot import TeleBot                                     # Project created with love by zafros #
from time import sleep
from PIL import ImageGrab

from configparser import ConfigParser  # CONFIG
config = ConfigParser()
config.read('config.ini')

cancel_status = 0

try: # Checking for the existence of a file
	with open('config.ini', 'r') as f:
		pass
except FileNotFoundError:
	with open('config.ini', 'w') as f:
		pass

@eel.expose
def on_load_js(): # Start after javascript is loaded
	try:
		r_id = config.get('web', 'reddit')
		channel_id = config.get('web', 'channel')
		token = config.get('web', 'token')
		amount = config.get('web', 'amount')
		cooldown = config.get('web', 'cooldown')
		image = config.get('web', 'image')
		copyright = config.get('web', 'copyright')
		eel.set_params(r_id, channel_id, token, amount, cooldown, image, copyright)   # <- Inserts the last entered data
	except Exception as ex: # if this first start
		print('creating config')

@eel.expose
def cancel():  #   <- TO DO
	global cancel_status
	cancel_status = 1
	print('canceled')

@eel.expose
def get_data(r_id, channel_id, amount, token, image, copyright, cooldown=1000):
	global cancel_status
	print(r_id + ' - ' + channel_id + ' - ' + amount + ' - ' + token + ' - ' + str(image) + ' - ' + str(copyright) + ' - ' + str(cooldown))
	progress_count = 1
	if r_id != '' and channel_id != '' and amount != '' and token != '':

		bot = TeleBot(token, parse_mode='Markdown')

		try:
			r_id = r_id.replace('r/', '') # delete r/ if it exiting
		except Exception as ex:
			pass

		with open('config.ini', 'w') as f:
			try:
				config.add_section('web')
			except Exception as ex:
				print('not need section')
			config.set('web', 'reddit', r_id)
			config.set('web', 'channel', channel_id)
			config.set('web', 'token', token)
			config.set('web', 'amount', amount)       # Project created with love by zafros #
			config.set('web', 'cooldown', cooldown)
			config.set('web', 'image', str(image))
			config.set('web', 'copyright', str(copyright))
			config.write(f)
		amount = int(amount) # fix one bug

		url = f'https://www.reddit.com/r/{r_id}/hot/.json?limit={amount}' # get link to json of page
		HEADERS = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
		}

		response = requests.get(url, headers = HEADERS)
		answer = response.json()

		for i in range(2, amount+2): # amount +2 because first 2 posts is not what we need. 
									 # Example: if you choose the number of 3 posts, then 5 posts will be given out.
			if cancel_status == 0:
				txt = answer['data']['children'][i]['data']['title'] # get text
				print(txt)
				try:
					link = answer['data']['children'][i]['data']['preview']['images'][0]['source']['url'].replace('amp;', '')
					print(link)    # get image
					img=True
					if link == 'preview': # if perm link != link on photo
						img=False
				except Exception as ex: #if no img
					print(ex)
					img=False

				if copyright == 1:
					copyright_text = 'https://www.reddit.com' + answer['data']['children'][i]['data']['permalink'] # copyright link
					txt = txt + f'[\n © Reddit]({copyright_text})'
				try:
					if img:
						bot.send_photo(channel_id, photo=link, caption=txt)
					elif image == 0:
						bot.send_message(channel_id, txt, disable_web_page_preview = True)
					sleep(int(cooldown)/1000) # to no spam report from telegram

					pixel = round(742 / (amount/(i-1)))
					if pixel < 10:
						pixel = 10                     # progress bar editing
					eel.set_progres(str(pixel)+'px', str(progress_count)+'/'+str(amount))
					progress_count += 1

				except Exception as ex:
					print(ex)
					sleep(5)
				print('\n')
			else:
				cancel_status = 0
				break
		eel.Done(str(amount))
	else:
		print('НЕ ВСЕ ПОЛЯ ЗАПОЛНЕНЫ')

                                                          # Project created with love by zafros #

##########################################
img = ImageGrab.grab()
w, h = img.size
h = round(w/2-813/2)  # middle of the screen
w = round(h/2-548/2)  # middle of the screen
eel.init('web') # init folder
eel.start('index.html', size=(813+15, 548+40), position=(h, w)) # start chrome #+15 +40