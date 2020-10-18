<p align="center">
    <img src="https://raw.githubusercontent.com/SecondThundeR/DokiDoki-RenPy/your-reality/ddlc_logo.png?token=AIXISSPEQVF3G4MZ3T6QU227SWGII" width="256px" height="256px" alt="DDLC-Logo">
</p>

# Decompiled Doki Doki Literature Club (For Ren'Py Launcher use)

> **Warning! These files contain many spoilers *(obviously)*. If you haven't played DDLC yet for some reasons, I recommend you play this game first to get true emotions from walkthrough *(Believe me, it's worth it)***

This repository contains the decompiled sources of the latest version of the Doki Doki Literature Club (1.1.1) for using in Ren'Py Launcher *(e.g. making mods for DDLC)*

Decompiled sources are provided only for personal use, file analysis in order to gain experience in creating games on Ren'Py and creating modifications for DDLC. Creating standalone projects using DDLC sources is prohibited by Team Salvato [*(See "Fan Games" section in Team Salvato IP Guidelines)*](http://teamsalvato.com/ip-guidelines/)

**To view README in Russian, follow [this link](https://github.com/SecondThundeR/DokiDoki-RenPy/blob/your-reality/README_RU.md)**

## How to use sources

1. Open Ren'Py Launcher
2. Create a new project with any name
3. Open the project folder and delete all files in it
4. Move files from `ddlc-renpy-project` folder to the project folder
5. Run the project in the launcher
6. Make sure that the game starts without warnings or errors.
7. Decompiled DDLC is now ready to use

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

1. Open Ren'Py Launcher
2. Press `"Build Distributions"` button
3. Choose the OS on which you want to build the modification
4. Wait for the compilation to finish
5. After the folder with the archive of the game opens, unzip the archive and go to the `game` folder
6. Copy all files with the extension .rpa from your mod to DDLC files and accept all file changes
7. Open the game and check the compatibility of your changes in the source

## DDLC Mod Distribution Information

In accordance with [Team Salvato IP Guidelines](http://teamsalvato.com/ip-guidelines/), modifications should be distributed as files with the extension .rpa and contain only those files that are necessary for installing the modification *(In most cases, this is just a scripts.rpa file or other files (if you replaced the graphics/fonts/audio in the game)*. Any modifications must **NOT** be distributed as a complete or standalone game and should only be installed on the existing official DDLC game installed on the user's computer

## Screenshots

<p align="center">
    <img src="https://raw.githubusercontent.com/SecondThundeR/DokiDoki-RenPy/your-reality/readme_screenshots/screenshot1.png?token=AIXISSKNI27DT32MFTEGPBS7SWGL6" alt="DDLC with edited name">
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/SecondThundeR/DokiDoki-RenPy/your-reality/readme_screenshots/screenshot2.png?token=AIXISSOCY4EUZZYORZMQNIK7SWGMA" alt="Developer Tools Screenshot">
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/SecondThundeR/DokiDoki-RenPy/your-reality/readme_screenshots/screenshot3.png?token=AIXISSN557XEIKENO54IVOC7SWGME" alt="Image Location Picker Screenshot">
</p>

## License

This decomplied sources is licensed under [MIT License](https://github.com/SecondThundeR/DokiDoki-RenPy/blob/your-reality/LICENSE) and it is provided "AS IS" without any warranties.

All rights reserved by Team Salvato, which created DDLC

Also thanks [Ren`Py](https://github.com/renpy/renpy), [unrpa](https://github.com/Lattyware/unrpa), [unrpyc](https://github.com/CensoredUsername/unrpyc) for great tools
