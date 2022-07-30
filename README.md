<h1 align=center>👽 Qwoq - Auto reddit to telegram parser.</h1>
<p align=center>Receives posts from the selected section on reddit and sends them to the telegram channel of your choice.</p>
  
<div align=center>
  <img src="https://img.shields.io/github/downloads/zafross/qwoq/total" alt=""></img>
  <img src="https://img.shields.io/github/license/zafross/qwoq" alt=""></img>
  <img src="https://img.shields.io/github/commit-activity/m/zafross/qwoq" alt=""></img>
  <img src="https://img.shields.io/github/v/release/zafross/qwoq?display_name=tag&include_prereleases" alt=""></img>
  <img src="https://img.shields.io/tokei/lines/github/zafross/Qwoq" alt="">
</div>

<div align=center>
  <img src="https://i.imgur.com/3ppnvhD.gif" alt=""></img>
</div>

## ⚙️ FIRST SETUP:

#### 1️⃣ Method 1 - WITH INSTALLED PYTHON:
1. [Download latest release source code (.zip)](https://github.com/zafross/Qwoq/releases/v0.1-alpha)
2. Open cmd in the repository folder on your PC and write: `pip install -r requirements.txt`
3. Done!

#### 2️⃣ Method 2 - WITHOUT INSTALLED PYTHON:
1. [Download latest release installer (.exe)](https://github.com/zafross/Qwoq/releases/v0.1-alpha)
2. Run and install `Qwoq setup.exe`
3. Done!

## ❓ How to use it:
1. Create a telegram bot with [@BotFather](https://t.me/BotFather) and copy bot token.
2. Add the created bot to your channel as admin. [(help)](https://stackoverflow.com/a/33497769/19632709)
3. Run `run.py` or `Qwoq.exe` (Depending on which method you choose) and paste the previously copied bot token into the console.
4. In the first field, enter the name of the reddit community (For example: `Minecraft`)
5. In the field on the right, enter the number of posts you want to send (For example: `15`)
6. Enter the channel ID in the last field. (Example: `@reddit_minecraft`)
7. Press `START` button.


## ⚡ Code
  The program is written using the eel library which links html, css, js with python. Web design was immediately done in [Figma](https://www.figma.com/file/7ZyhO41tvhen7h9H1s7JkC/Untitled). 
In the next updates, I want to rework it a lot because in the current version the window is too small,
ugly and there are very few settings + the bot token is entered through the console (this is terrible).
  
  In fact, I am making a program only to train my skills, and it was in this program that I decided to try eel. I will be glad if you help with the development of this repository. 💜

## 💡 To Do
_😋 I will be glad for your help_
- [ ] Redesign web for more settings
  - [ ] Choose "hot", "new" or "top" in web (reddit marks)
  - [ ] Choose what type to parse in web (img, video or just text)
  - [ ] Toggle copyright in web
  - [ ] Bot token in web
  - [ ] Change the delay between messages in web
- [ ] The number on the progress bar (Example: 53/250)
- [ ] Parse a video too
- [ ] Do not send similar messages 
- [ ] A working cancel button (Not functioning now)
- [ ] Info buttons (Not functioning now)
- [X] Save settings (config.ini)
- [ ] Send completed message and turn buttons when progress is done.
- [X] Translate into English
