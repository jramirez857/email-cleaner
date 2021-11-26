[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# email-cleaner
This script is in development. Right now it can get the top number of senders in a users gmail inbox.
## Setup
This script requires you to [create a Google Cloud Platform Project and enable the Gmail api](https://developers.google.com/workspace/guides/create-project). The credentials must be saved in a credentials.json file in the project directory.
Create a virtual environment for the project using python 3.9 `python -m venv venv`
Activate the virtual environment and install dependencies by using `pip install -r requirements.txt` with your virtual environment.
## Usage
Example: Group last 100 emails by top senders and decide which ones to move to trash (not a permanent deletion).
>python cleanup.py 100
```
Fetching 100 emails 100 at a time...
  0% (0 of 4) |                                                                                                                                  | Elapsed Time: 0:00:00 ETA:  --:--:--View more info on 14 emails from Dan at Real Python <info@realpython.com>? (y/n)y
subject: last call: Learn Python Effectively
subject: In love, war, and open-source—never give up
subject: Your Roadmap to Clean & Pythonic Code
subject: Real Python Membership Q&A
subject: [🐍PyTricks]: Python's namedtuples can be a great alternative to defining a class manually
subject: No crane kicks at the Python gym
subject: [🐍PyTricks]: The get() method on Python dicts and its "default" arg
subject: how to stay current as a Python developer
subject: [🐍PyTricks]: picking up the basics of Python was the easy part?
subject: Python 4.0
subject: [🐍PyTricks]: How to sort a Python dict by value
subject: [🐍PyTricks]: Different ways to test multiple flags at once in Python
subject: [🐍PyTricks]: Merging two dicts in Python 3.5+ with a single expression
subject: Welcome to the Real Python community!
Delete all 14 emails from Dan at Real Python <info@realpython.com>? (y/n)n
View more info on 12 emails from "IsThereAnyDeal.com" <waitlist@isthereanydeal.com>? (y/n)y
subject: Waitlist: STAR WARS Jedi: Fallen Order $13
subject: Waitlist: Red Dead Redemption 2 $27
subject: Waitlist x3: Mass Effect Legendary Edition $35, Red Dead Redemption 2 $30, STAR WARS Jedi: Fallen Order $13
subject: Waitlist: STAR WARS Jedi: Fallen Order $13
subject: Waitlist: Red Dead Redemption 2 $27
subject: Waitlist x3: Mass Effect Legendary Edition $29, Red Dead Redemption 2 $27, STAR WARS Jedi: Fallen Order $15
subject: Waitlist: Red Dead Redemption 2 $30
subject: Waitlist: Red Dead Redemption 2 $27
subject: Waitlist: Red Dead Redemption 2 $27
subject: Waitlist x2: Marvel's Avengers $16, Red Dead Redemption 2 $28
subject: Waitlist x2: Mass Effect Legendary Edition $30, STAR WARS Jedi: Fallen Order $13
subject: Waitlist x4: Marvel's Avengers $16, Mass Effect Legendary Edition $31, Red Dead Redemption 2 $27
Delete all 12 emails from "IsThereAnyDeal.com" <waitlist@isthereanydeal.com>? (y/n)n
View more info on 2 emails from no-reply@geeksforgeeks.org? (y/n)y
subject: GeeksforGeeks - Please Confirm Registration
subject: Welcome to GeeksforGeeks!
Delete all 2 emails from no-reply@geeksforgeeks.org? (y/n)y
```


## Thanks
- [aiofiles](https://pypi.org/project/aiofiles/) by Tin Tvrtkovic
- [async-timeout](https://pypi.org/project/async-timeout/) by Andrew Svetlov <andrew.svetlov@gmail.com>
- [asynctest](https://pypi.org/project/asynctest/) by Martin Richard
- [attrs](https://pypi.org/project/attrs/) by Hynek Schlawack
- [cachetools](https://pypi.org/project/cachetools/) by Thomas Kemmer
- [certifi](https://pypi.org/project/certifi/) by Kenneth Reitz
- [cfgv](https://pypi.org/project/cfgv/) by Anthony Sottile
- [chardet](https://pypi.org/project/chardet/) by Mark Pilgrim
- [charset-normalizer](https://pypi.org/project/charset-normalizer/) by Ahmed TAHRI @Ousret
- [click](https://pypi.org/project/click/) by Armin Ronacher
- [colorama](https://pypi.org/project/colorama/) by Jonathan Hartley
- [distlib](https://pypi.org/project/distlib/) by Vinay Sajip
- [filelock](https://pypi.org/project/filelock/) by Benedikt Schmitt
- [google-api-core](https://pypi.org/project/google-api-core/) by Google LLC
- [google-api-python-client](https://pypi.org/project/google-api-python-client/) by Google LLC
- [google-auth](https://pypi.org/project/google-auth/) by Google Cloud Platform
- [google-auth-oauthlib](https://pypi.org/project/google-auth-oauthlib/) by Google Cloud Platform
- [googleapis-common-protos](https://pypi.org/project/googleapis-common-protos/) by Google LLC
- [identify](https://pypi.org/project/identify/) by Chris Kuehl
- [idna](https://pypi.org/project/idna/) by Kim Davies
- [multidict](https://pypi.org/project/multidict/) by Andrew Svetlov
- [mypy-extensions](https://pypi.org/project/mypy-extensions/) by The mypy developers
- [nodeenv](https://pypi.org/project/nodeenv/) by Eugene Kalinin
- [oauthlib](https://pypi.org/project/oauthlib/) by The OAuthlib Community
- [packaging](https://pypi.org/project/packaging/) by Donald Stufft and individual contributors
- [pathspec](https://pypi.org/project/pathspec/) by Caleb P. Burns
- [pip-check-reqs](https://pypi.org/project/pip-check-reqs/) by Richard Jones
- [platformdirs](https://pypi.org/project/platformdirs/) by
- [pre-commit](https://pypi.org/project/pre-commit/) by Anthony Sottile
- [progressbar](https://pypi.org/project/progressbar/) by Nilton Volpato
- [protobuf](https://pypi.org/project/protobuf/) by
- [pyasn](https://pypi.org/project/pyasn/) by
- [pydantic](https://pypi.org/project/pydantic/) by Samuel Colvin
- [pyparsing](https://pypi.org/project/pyparsing/) by Paul McGuire
- [python-utils](https://pypi.org/project/python-utils/) by Rick van Hattem
- [PyYAML](https://pypi.org/project/PyYAML/) by Kirill Simonov
- [regex](https://pypi.org/project/regex/) by Matthew Barnett
- [requests](https://pypi.org/project/requests/) by Kenneth Reitz
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) by Kenneth Reitz
- [rsa](https://pypi.org/project/rsa/) by Sybren A. Stüvel
- [six](https://pypi.org/project/six/) by Benjamin Peterson
- [thanker](https://pypi.org/project/thanker/) by WardPearce
- [toml](https://pypi.org/project/toml/) by William Pearson
- [tomli](https://pypi.org/project/tomli/) by
- [typer](https://pypi.org/project/typer/) by Sebastián Ramírez
- [typing-extensions](https://pypi.org/project/typing-extensions/) by
- [uritemplate](https://pypi.org/project/uritemplate/) by Ian Stapleton Cordasco
- [virtualenv](https://pypi.org/project/virtualenv/) by Bernat Gabor
- [yarl](https://pypi.org/project/yarl/) by Andrew Svetlov
