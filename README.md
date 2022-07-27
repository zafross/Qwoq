<h1 align=center>👽 Qwoq - Auto reddit to telegram parser.</h1>
<p align=center>Receives posts from the selected section on reddit and sends them to the telegram channel of your choice.</p>

## How to use it:
#### FIRST SETUP
1. Clone or download repository.
2. Open cmd(terminal) in the repository folder on your PC and write:
`pip install -r requirements.txt`
3. Create a telegram bot with [@BotFather](https://t.me/BotFather) and copy bot token.
4. Add the created bot to your channel as admin. [(help)](https://stackoverflow.com/a/33497769/19632709)
5. Run `run.py` and paste the previously copied bot token into the console.
6. Done!

#### START
1. Run `run.py`
2. In the first field, enter the name of the reddit community (For example: `Minecraft`)
3. In the field on the right, enter the number of posts you want to send (For example: `15`)
4. Enter the channel ID in the last field. (Example: `@reddit_minecraft`)
5. Press the green start button.


## Code
Some txt here...

## To Do
_😋 I will be glad for your help_
- [ ] Redesign web for more settings
  - [ ] Choose "hot", "new" or "top" in web (reddit marks)
  - [ ] Choose what type to parse in web (img, video or just text)
  - [ ] Toggle copyright in web
  - [ ] Bot token in web
- [ ] The number on the progress bar (Example: 53/250)
- [ ] Parse a video too
- [ ] Do not send similar messages 
- [ ] A working cancel button (Not functioning now)
- [ ] Info buttons (Not functioning now)
- [X] Save settings (config.ini)
- [ ] Send completed message and turn buttons when progress is done.
- [X] Translate into English
