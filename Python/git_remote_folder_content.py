#!/usr/bin/env python3

import requests
import json

resp = requests.get(
        'https://api.github.com/repos/Thewessen/dotfiles/contents/.zsh_functions?ref=work',
        headers={ 'Accept': 'application/vnd.github.v3+json' }
        )

content = json.loads(resp.content)
for f in content:
    print(f['download_url'])
    r = requests.get(f['download_url'])
    with open('/home/sthewessen/.zsh_functions/' + f['name'], 'w') as target:
        target.write(r.text)
