# handlez with a z
## aka simple-bsky-handle-maker
a simple python script to help make bluesky handles via the command line or whatever

inspired by [SlickDomique/open-handles](https://github.com/SlickDomique/open-handles), 'cept in python and with hetzner because i'm too dumb to fork their work lol 

### to use: 

clone the repo (aka, run `git clone https://github.com/lumpenfreude/simple-bsky-handle-maker`)

run `source bin/activate`

run `pip install -r requirements.txt`

get your hetzner DNS API key and export it to bash by doin `export HETZNER_DNS_TOKEN=yourapitoken`

run `python handlez.py` 

if any of that stuff fails, you probably don't have python, or python-pip installed. i don't know how to help you if that is the case. 

### roadmap:

gonna flask it up and make it an interactive webpage, i guess. 
