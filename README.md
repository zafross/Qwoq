<h1 align=center>👽 Qwoq - Auto reddit to telegram parser.</h1>
<p align=center>Receives posts from the selected section on reddit and sends them to the telegram channel of your choice.</p>
  
<div align=center>
  <img src="https://img.shields.io/badge/Based%20on-eel-blueviolet" alt=""></img>
  <img src="https://img.shields.io/github/license/zafross/qwoq" alt=""></img>
  <img src="https://img.shields.io/github/commit-activity/m/zafross/qwoq" alt=""></img>
  <img src="https://img.shields.io/github/v/release/zafross/qwoq?display_name=tag&include_prereleases" alt="version"></img>
  <img src="https://img.shields.io/tokei/lines/github/zafross/Qwoq" alt="">
  <a href="https://lgtm.com/projects/g/zafross/Qwoq/context:javascript"><img alt="Language grade: JavaScript" src="https://img.shields.io/lgtm/grade/javascript/g/zafross/Qwoq.svg?logo=lgtm&logoWidth=18"/></a>
</div>

<div align=center>
  <img src="https://i.imgur.com/NGyslv9.gif" alt=""></img>
</div>

## ⚙️ FIRST SETUP:

#### 1️⃣ Method 1 - WITH INSTALLED PYTHON:
1. [Download latest release source code (.zip)](https://github.com/zafross/Qwoq/releases/tag/v0.2-beta)
2. Open cmd in the repository folder on your PC and write: `pip install -r requirements.txt`
3. Done!

#### 2️⃣ Method 2 - WITHOUT INSTALLED PYTHON:
1. [Download latest release installer (.exe)](https://github.com/zafross/Qwoq/releases/tag/v0.2-beta)
2. Run and install `Qwoq 0.2 setup.exe`
3. Done!

## ❓ How to use it:
###Important: you need installed chrome
1. Create a telegram bot with [@BotFather](https://t.me/BotFather) and copy bot token.
2. Add the created bot to your channel as admin. [(help)](https://stackoverflow.com/a/33497769/19632709)
3. Run `run.py` or `Qwoq.exe` (Depending on which method you choose).
4. In the first field, enter the telegram id of the channel (Example: `@reddit_minecraft`)
5. In the second field, enter the name of the community on reddit (For example: `Minecraft`)
6. Paste the copied token into the token field.
7. Choose if you only want posts with photos and if you want to send copyright. (So far, if you select only with photo posts, there will be less than the selected number)
8. In the last 2 fields, specify the delay between sending messages in milliseconds (recommended 1000) and amount of these messages.
9. Press `START` button.


## ⚡ Code
  The program is written using the eel library which links html, css, js with python. Web design was immediately done in [Figma](https://www.figma.com/file/7ZyhO41tvhen7h9H1s7JkC/Untitled). I've recently changed the design and added more settings, but there's a lot more I want to do.
  
  In fact, I am making a program only to train my skills, and it was in this program that I decided to try eel. I will be glad if you help with the development of this repository. 💜

## 💡 To Do
_😋 I will be glad for your help_
- [X] Redesign web for more settings
  - [ ] Choose "hot", "new" or "top" in web (reddit marks)
  - [X] +- Choose what type to parse in web (img, video or just text) 
  - [X] Toggle copyright in web
  - [X] Bot token in web
  - [X] Change the delay between messages in web
- [ ] The number on the progress bar (Example: 53/250)
- [ ] Parse a video too
- [ ] Do not send similar messages 
- [ ] A working cancel button (Not functioning now)
- [ ] Info buttons (Not functioning now)
- [X] Save settings (config.ini)
- [X] Send completed message and turn buttons when progress is done.
- [X] Translate into English
