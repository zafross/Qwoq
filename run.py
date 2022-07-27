import eel
import requests
import telebot
from telebot import types
from time import sleep
from win32api import GetSystemMetrics # in order to get screen size

from configparser import ConfigParser  # CONFIG
config = ConfigParser()
config.read('config.ini')

try: # Checking for the existence of a file
	with open('config.ini', 'r') as f:
		pass
except FileNotFoundError:
	with open('config.ini', 'w') as f:
		tkn = str(input('Input telegram bot token: '))  # NEED TO TRANSFER THIS TO WEB
		config.add_section('bot')
		config.set('bot', 'token', tkn)
		config.write(f)

@eel.expose
def on_load_js(): # Start after javascript is loaded
	try:
		r_id = config.get('web', 'reddit')
		channel_id = config.get('web', 'channel')
		eel.set_params(r_id, channel_id)   # <- Inserts the last entered data
	except: # if this first start
		pass

bot = telebot.TeleBot(config.get('bot', 'token'), parse_mode='Markdown') # Do not install MarkdownV2 because there are a lot of errors

@eel.expose
def cancel():  #   <- TO DO
	print('canceled')

@eel.expose
def get_data(r_id, channel_id, amount):
	if r_id != '' and channel_id != '' and amount != '':
		try:
			config.get('web', 'reddit')
		except:
			config.add_section('web')
		with open('config.ini', 'w') as f:
			config.set('web', 'reddit', r_id)
			config.set('web', 'channel', channel_id)
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

			copyright = 'https://www.reddit.com' + answer['data']['children'][i]['data']['permalink'] # copyright link
			txt = txt + f'[\n © Reddit]({copyright})'
			try:
				if img:
					bot.send_photo(channel_id, photo=link, caption=txt)
				else:
					bot.send_message(channel_id, txt, disable_web_page_preview = True)
				sleep(1) # to no spam report from telegram

				pixel = round(226 / (amount/(i-1)))
				if pixel < 20:
					pixel = 20                     # progress bar editing
				eel.set_progres(str(pixel)+'px')

			except Exception as ex:
				print(ex)
				sleep(5)
			print('\n')
	else:
		print('НЕ ВСЕ ПОЛЯ ЗАПОЛНЕНЫ')



##########################################
h = round(GetSystemMetrics(0)/2-243)  # middle of the screen
w = round(GetSystemMetrics(1)/2-130)  # middle of the screen
eel.init('web') # init folder
eel.start('index.html', size=(502, 170), position=(h, w)) # start chrome