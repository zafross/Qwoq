import eel
import requests
from telebot import TeleBot                                     # Project created with love by zafros #
from time import sleep
from PIL import ImageGrab
from pystyle import Colorate, Colors, Write
from configparser import ConfigParser  # CONFIG
config = ConfigParser()
config.read('config.ini')

def log(text, level='info'):
	if level == 'info':
		print(Colors.gray + "[ INFO ] " + str(text))
	elif level == 'except':
		print(Colors.orange + "[ EXCEPTION ] " + str(text))
	elif level == 'err':
		print(Colors.red + "[ ERROR ] " + str(text) + '\n')
	elif level == 'success':
		print(Colors.green + "[ SUCCESS ] " + str(text))

def check_update():
	eel.sleep(1.0)
	log('Checking new updates...')
	response = requests.get("https://api.github.com/repos/zafross/Qwoq/releases/latest")
	ver_new = str(response.json()["name"])
	ver_now = str(eel.get_version()().replace('version: ', ''))
	if ver_now != ver_new:
		log(f'New update available ({ver_now} -> {ver_new})', 'success')
		eel.notify('New update available', f'Your version is {ver_now}, the new version is {ver_new}. Click on version if you want to update')
	else:
		log('You have the latest version.', 'success')

try: # Checking for the existence of a file
	log('Checking config file...')
	with open('config.ini', 'r') as f:
		pass
	log('Config file found.\n', 'success')
except FileNotFoundError:
	with open('config.ini', 'w') as f:
		pass
	log('Config file not found. Created a new one.\n', 'success')

@eel.expose
def on_load_js(): # Start after javascript is loaded
	eel.spawn(check_update)
	log('The web interface has been launched successfully.\n', 'success')
	try:
		log('Finding settings in the config file....')
		r_id = config.get('web', 'reddit')
		channel_id = config.get('web', 'channel')
		token = config.get('web', 'token')
		amount = config.get('web', 'amount')
		cooldown = config.get('web', 'cooldown')
		image = config.get('web', 'image')
		copyright = config.get('web', 'copyright')
		eel.set_params(r_id, channel_id, token, amount, cooldown, image, copyright)   # <- Inserts the last entered data
		log('The settings in the config are found.\n', 'success')
	except Exception as ex: # if this first start
		log('No settings found in config.\n', 'success')

@eel.expose
def get_data(r_id, channel_id, amount, token, image, copyright, cooldown=1000):
	log('Successfully receive data.', 'success')
	log('Start working...\n')
	progress_count = 1
	bot = TeleBot(token, parse_mode='Markdown')

	try:
		r_id = r_id.replace('r/', '') # delete r/ if it exiting
	except Exception as ex:
		pass

	with open('config.ini', 'w') as f:
		try:
			config.add_section('web')
		except Exception as ex:
			pass
		config.set('web', 'reddit', r_id)
		config.set('web', 'channel', channel_id)
		config.set('web', 'token', token)
		config.set('web', 'amount', amount)       # Project created with love by zafros #
		config.set('web', 'cooldown', cooldown)
		config.set('web', 'image', str(image))
		config.set('web', 'copyright', str(copyright))
		config.write(f)
	amount = int(amount)
	log('Data written to config.\n', 'success')
	log('Sending a request to the reddit server...')

						#       |   #
	                    # TODO \/   # Because reddit max limit is 100 ;(
	url = f'https://www.reddit.com/r/{r_id}/hot/.json?limit={amount*4}' # get link to json of page
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
	}

	response = requests.get(url, headers = HEADERS)
	answer = response.json()

	i = 2
	amount_while = amount+2
	log('Data received.', 'success')
	log('Start sending:\n')
	while i != amount_while and i != len(answer['data']['children']):
	 # amount +2 because first 2 posts is not what we need. 
	 # Example: if you choose the number of 3 posts, then 5 posts will be given out.
			
		if eel.give_cancel_status()() == 0:
			try:
				txt = answer['data']['children'][i]['data']['title'] # get text
			except:
				eel.notify('Invalid subreddit name', 'The name of the subreddit should look something like this: r/Minecraft or like this: Minecraft.')
				eel.Cancel()
				eel.give_cancel_status()()
				return
			try:
				if answer['data']['children'][i]['data']['is_video']:
					link = answer['data']['children'][i]['data']['media']['reddit_video']['fallback_url'].replace('?source=fallback', '')
					is_video = True
				else:
					link = answer['data']['children'][i]['data']['preview']['images'][0]['source']['url'].replace('amp;', '')
					is_video = False
				log('(' + txt[:10]+'...) | Video: ' + str(is_video))
				valid=True
				if link == 'preview': # if perm link != link on photo
					valid=False
			except Exception as ex: #if no img
				if 'preview' in str(ex):
					amount_while+=1
					log('There is no media in the post, skipped.\n', 'except')
					valid=False
				else:
					log(ex, 'err')

			if copyright == 1:
				copyright_text = 'https://www.reddit.com' + answer['data']['children'][i]['data']['permalink'] # copyright link
				txt = txt + f'[\n © Reddit]({copyright_text})'
			try:
				if valid:
					try:
						if is_video and str(image) == '1':
							bot.send_video(channel_id, video=link, caption=txt)
						else:
							bot.send_photo(channel_id, photo=link, caption=txt)

						pixel = round(742 / (amount/progress_count))
						if pixel < 10:
							pixel = 10                     # progress bar editing
						eel.set_progres(str(pixel)+'px', str(progress_count)+'/'+str(amount))
						progress_count += 1
						log('Sent successfully!\n', 'success')

					except Exception as ex:
						amount_while+=1
						if 'Too Many Requests' in str(ex):
							log('Too many requests to telegram api.\n', 'except')
							eel.notify('Too many requests', 'Telegram says you are sending messages too fast. Please increase the cooldown.')
							sleep(6)
						elif 'chat not found' in str(ex):
							log('Invalid telegram channel id\n', 'except')
							eel.notify('Invalid telegram channel id', 'The "@" character must be at the beginning. The bot must be an administrator in this channel.')
							eel.Cancel()
							eel.give_cancel_status()()
							return
						elif 'Unauthorized' in str(ex):
							log('Invalid telegram bot token\n', 'except')
							eel.notify('Invalid telegram bot token', 'Get a bot token from @BotFather. Click on a version to read the documentation.')
							eel.Cancel()
							eel.give_cancel_status()()
							return
						elif 'wrong file identifier' in str(ex) or 'failed to get HTTP URL content' in str(ex):
							log('Telegram was unable to receive media\n', 'except')
						else:
							log(ex, 'err')
							sleep(2)
				sleep(int(cooldown)/1000) # to no spam report from telegram
			except Exception as ex:
				log(ex, 'err')
			i+=1
		else:
			log('Canceled')
			return
	log('Process completed successfully. Messages sent: '+str(progress_count-1)+'/'+str(amount)+'.\n', 'success')
	eel.Done(str(amount))

                                                          # Project created with love by zafros #

##########################################
img = ImageGrab.grab()
h, w = img.size
h = round(h/2-812/2)  # middle of the screen
w = round(w/2-600/2)  # middle of the screen
log('Starting web interface...')
eel.init('web') # init folder
eel.start('index.html', size=(813+15, 548+40), position=(h, w), shutdown_delay=0, port=0) # start chrome #+15 +40