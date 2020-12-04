<div align="center">
 <img src="https://raw.githubusercontent.com/SecondThundeR/DokiDoki-RenPy/your-reality/readme_files/logos/ddlc_logo.png" width="256px" height="256px" alt="DDLC-Logo">
 <h1>Decompiled Doki Doki Literature Club (For Ren'Py Launcher use)</h1>
 <blockquote><b>Warning! These files contain many spoilers <i>(obviously)</i>. <br>If you haven't played DDLC yet for some reasons, I recommend you play this game first to get true emotions from walkthrough <i>(Believe me, it's worth it)</i></b></blockquote>
</div>

This repository contains the decompiled sources of the latest version of the Doki Doki Literature Club (1.1.1) for using in Ren'Py Launcher *(e.g. making mods for DDLC)*

Decompiled sources are provided only for personal use, file analysis in order to gain experience in creating games on Ren'Py and creating modifications for DDLC. Creating standalone projects using DDLC sources is prohibited by Team Salvato [*(See "Fan Games" section in Team Salvato IP Guidelines)*](http://teamsalvato.com/ip-guidelines/)

**To view README in Russian, follow [this link](https://github.com/SecondThundeR/DokiDoki-RenPy/blob/your-reality/README_RU.md)**

## How to use sources

1. In Ren'Py Launcher, create a new project with any name
2. Open the project folder and delete all files in it
3. Move files from `ddlc-renpy-project` folder to the project folder
4. Run the project in the launcher
5. Make sure that the game starts without warnings or errors.
6. Decompiled DDLC is now ready to use

## How to enable developer tools

To enable developer tools, go to the file `definitions.rpy` in the `game` folder and change the value of `config.developer` from `False` to `True` *(Don't forget to change this back to `False` before compiling the finished project)*

## What is each folder responsible for

### Repository folder

- `characters` - folder of characters files *(Moved out from `game` folder so the game can see this files and manipulate them)*
- `game` - main folder of Ren'Py project *(and compiled game too)*

### game folder

- `bgm`, `sfx`, `gui/sfx` - folders with music, SFX and ambient sounds
- `gui` - images for UI *(Contains lot of pictures that not suitable for people who are easily disturbed. Pictures with spoilers are also present)*
- `images` - images of game *(Contains lot of pictures that not suitable for people who are easily disturbed. Pictures with spoilers are also present)*
- `python-packages` - folder of Python libraries and packages *(Contains `singleton` library that game rely on)*

## How to compile the mod and apply it in the original DDLC

1. In Ren'Py Launcher, go to `"Build Distributions"`
2. Choose the OS on which you want to build the modification
3. Wait for the compilation to finish
4. After compilation, unzip the archive and open `game` folder
5. Copy all files with the extension .rpa from your mod to DDLC files and accept all file changes
6. Open the game and check the compatibility of your changes in the source

## DDLC Mod Distribution Information

According to [Team Salvato IP Guidelines](http://teamsalvato.com/ip-guidelines/), modifications should be distributed as files with the extension .rpa and contain files that are necessary for installing the modification *(In most cases, this is just a scripts.rpa file or other files (if you replaced the graphics/fonts/audio in the game)*. Any modifications must **NOT** be distributed as a complete or standalone game and should only be installed on the existing official DDLC game installed on the user's computer

## Screenshots

<div align="center">
 <img src="https://raw.githubusercontent.com/SecondThundeR/DokiDoki-RenPy/your-reality/readme_files/screenshots/main_menu.png" alt="DDLC with edited name">
 <img src="https://raw.githubusercontent.com/SecondThundeR/DokiDoki-RenPy/your-reality/readme_files/screenshots/dev_menu.png" alt="Developer Tools Screenshot">
 <img src="https://raw.githubusercontent.com/SecondThundeR/DokiDoki-RenPy/your-reality/readme_files/screenshots/image_loc_picker.png" alt="Image Location Picker Screenshot">
</div>

## License

This decomplied sources is licensed under [MIT License](https://github.com/SecondThundeR/DokiDoki-RenPy/blob/your-reality/LICENSE) and it is provided "AS IS" without any warranties.

All rights reserved by Team Salvato, which created DDLC

Also thanks [Ren`Py](https://github.com/renpy/renpy), [unrpa](https://github.com/Lattyware/unrpa), [unrpyc](https://github.com/CensoredUsername/unrpyc) authors for great tools
