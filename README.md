**ARCHIVED:** Anilinkz itself is no more 😢 so this scraper is useless.

Anime Scrape
==============

Automatically download anime episodes from http://anilinkz.tv/

All you have to do is enter name of the anime, and start - end episode which you want to download

Installation
=============

Copy `anime_scrape.py` to the folder where you want to download videos to

or cd into the repository folder, and execute

    ln -s anime_scrape.py anime_scrape

Now move the `anime_scrape` soft link file to `/usr/local/bin` or `~/.local/bin` to use `anime_scrape.py` from anywhere

Usage
======

    $ ./anime_scrape.py
    Enter Anime Name :  Naruto
    Staring Episode: 1
    Ending Episode: 30

This will start download of episodes 1 to 30.

To download single episode, put starting and ending as same number.

To download dubbed episodes, append "dubbed" to the name

***Note : ***

Some anime names may not work. Entering `Attack on Titan` wont work, you will have to enter `Attack on Titan Shingeki No Kyojin`
This is because the URL format of http://anilinkz.tv/ is not exactly constant for each anime.
For the exact format, open any one episode of the anime you wanna download and see the URL.
Example : Attack on Titan episode 1 link is : `http://anilinkz.tv/attack-on-titan-shingeki-no-kyojin-episode-1`

So for this series, remove *episode-[n]* from the end, and put [space] instead of [-] to get the anime name to enter.
"Attack on Titan Shingeki no Kyojin" is the name to use for Attack on Titan.
Captilization of letters don't matter
