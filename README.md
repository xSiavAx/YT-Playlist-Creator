# YT-Playlist-Creator
Simple script that creates playlist with all songs from your library on YouTube Music Service.

# How to (Mac OS)

## Preparing (once per PC)
### Setup `ytmusicapi` [python lib](https://ytmusicapi.readthedocs.io/en/latest/index.html)
Install lib:
> pip3 install ytmusicapi

If no pip installed, do:
> brew install python

If case troubles with brew, run:
> brew doctor

### Acquiring credentials
Usually, aquired token is valid for 2 years or till sessions is valid.
Also these instructions available at `ytmusicapi` [lib page](https://ytmusicapi.readthedocs.io/en/latest/setup.html)

* Go to "https://music.youtube.com".
* Login (if u aren't logged in).
* Click on "Library".
* Open "Dev Instruments->Network"
* Find request started with "browse"
* If no such request, just click on "Library" once more
* Click on request
* In openned window look for "Request Headers" section
* Copy evruthing started from "accept: */*" and to the end of section.
* Save to some temporary file (to avoid losing this data)

Your file should looks like this:
```
accept: */*
accept-encoding: gzip, deflate, br
accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6
authorization: SAPISIDHASH 1601116790_a85c84524ec50eb648ca3f8e3ce1a24a8edd5794
content-length: 1569
......
x-youtube-page-cl: 332844418
x-youtube-page-label: youtube.music.web.client_20200921_00_RC01
x-youtube-time-zone: Europe/Kiev
x-youtube-utc-offset: 180
```

### Generating credentials json file
Go to directory with 'main.py'
> cd "path/to/Youtube\ Music\ Playlist\ Creator/main.py/directory"

Run python
> python3

Import lib and run
> `>>>` from ytmusicapi import YTMusic

Run setup
> `>>>` YTMusic.setup(filepath="headers_auth.json")

You will see instructions like "Please paste the request headers from Firefox and press Ctrl-D to continue:". So follow them – paste data copied on previous step and pres "Cntrl-D".
This operations creates json file 'headers_auth.json'. Put it to same directory as 'main.py' (usually it is already there).

## Usage
Run script:
> python3 main.py

PROFIT!!!!

Scipt creates playlist named with current date and time. U will able rename playlist as u wish from Youtube Music i-face.
If you want to setup your own playlist name – edit `main.py`.

# FAQ
Q: Why there are so many TYPOs and Grammar misstackes.

A: London is the capital of Great Britain.

Q: Why there are instructions only for Mac OS?

A: Cuz i am lazy. Instructions will be the same for other OS, except the first part (Install the python lib). Sure, u could get it on your own.

Q: a) It doesn't work! b) I got an error! c) README is too complex or disorienting, I cant understand how to make it works.

A: Write [me](mailto:mail@siava.pp.ua) and i will try to help u (in case i will have time for it).

