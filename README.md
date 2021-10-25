# email-cleaner
This script is in development. Right now it can get the top number of senders in a users gmail inbox.
## Setup
This script requires you to [create a Google Cloud Platform Project and enable the Gmail api](https://developers.google.com/workspace/guides/create-project). The credentials must be saved in a credentials.json file in the project directory.
Create a virtual environment for the project using python 3.9 `python -m venv venv`
Activate the virtual environment and install dependencies by using `pip install -r requirements.txt` with your virtual environment.
## Usage
Example: Get amount of times each unique sender appears in your last 1000 emails printed in a senders.json.
>python email_parser.py -n 1000
```
python email_parser.py -n 4000
get_num_messages():63: INFO: Successfully retrieved 4000 messages
100% (4000 of 4000) |############################################################################| Elapsed Time: 0:12:47 Time:  0:12:47 
get_ordered_senders():108: INFO: Got 739 senders from 4000 messages
get_ordered_senders():110: INFO: Your top 10 email senders in your last 4000 emails are:
[   'Capital One <capitalone@notification.capitalone.com>',    
    'Patch <noreply@patch.com>',
    'Peloton <peloton@s.onepeloton.com>',
    'Micro Center <microcenter@microcenterinsider.com>',
    'PlayStation <email@email.playstation.com>',
    'Mint <team@mint.com>',
    'Real Python <info@realpython.com>',
    'Coinbase <no-reply@coinbase.com>',
    'Withings <community@email.withings.com>',
    'Discover Card <discover@services.discover.com>']
```

If n is not provided the default is 100 emails.

## Thanks
- [aiofiles](https://pypi.org/project/aiofiles/) by Tin Tvrtkovic
- [async-timeout](https://pypi.org/project/async-timeout/) by Andrew Svetlov
- [asynctest](https://pypi.org/project/asynctest/) by Martin Richard
- [attrs](https://pypi.org/project/attrs/) by Hynek Schlawack
- [cachetools](https://pypi.org/project/cachetools/) by Thomas Kemmer
- [certifi](https://pypi.org/project/certifi/) by Kenneth Reitz
- [chardet](https://pypi.org/project/chardet/) by Mark Pilgrim
- [charset-normalizer](https://pypi.org/project/charset-normalizer/) by Ahmed TAHRI @Ousret
- [click](https://pypi.org/project/click/) by Armin Ronacher
- [colorama](https://pypi.org/project/colorama/) by Jonathan Hartley
- [google-api-core](https://pypi.org/project/google-api-core/) by Google LLC
- [protobuf](https://pypi.org/project/protobuf/) by
- [setuptools](https://pypi.org/project/setuptools/) by Python Packaging Authority
- [google-api-python-client](https://pypi.org/project/google-api-python-client/) by Google LLC
- [uritemplate](https://pypi.org/project/uritemplate/) by Ian Stapleton Cordasco
- [google-auth](https://pypi.org/project/google-auth/) by Google Cloud Platform
- [cachetools](https://pypi.org/project/cachetools/) by Thomas Kemmer
- [rsa](https://pypi.org/project/rsa/) by Sybren A. Stuvel
- [pyasn](https://pypi.org/project/pyasn/) by
- [setuptools](https://pypi.org/project/setuptools/) by Python Packaging Authority
- [google-auth-oauthlib](https://pypi.org/project/google-auth-oauthlib/) by Google Cloud Platform
- [google-auth](https://pypi.org/project/google-auth/) by Google Cloud Platform
- [cachetools](https://pypi.org/project/cachetools/) by Thomas Kemmer
- [rsa](https://pypi.org/project/rsa/) by Sybren A. Stuvel
- [pyasn](https://pypi.org/project/pyasn/) by
- [setuptools](https://pypi.org/project/setuptools/) by Python Packaging Authority
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) by Kenneth Reitz
- [googleapis-common-protos](https://pypi.org/project/googleapis-common-protos/) by Google LLC
- [protobuf](https://pypi.org/project/protobuf/) by
- [idna](https://pypi.org/project/idna/) by Kim Davies
- [multidict](https://pypi.org/project/multidict/) by Andrew Svetlov
- [oauthlib](https://pypi.org/project/oauthlib/) by The OAuthlib Community
- [progressbar](https://pypi.org/project/progressbar/) by Nilton Volpato
- [protobuf](https://pypi.org/project/protobuf/) by
- [pyasn](https://pypi.org/project/pyasn/) by
- [pyparsing](https://pypi.org/project/pyparsing/) by Paul McGuire
- [python-utils](https://pypi.org/project/python-utils/) by Rick van Hattem
- [requests](https://pypi.org/project/requests/) by Kenneth Reitz
- [certifi](https://pypi.org/project/certifi/) by Kenneth Reitz
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) by Kenneth Reitz
- [rsa](https://pypi.org/project/rsa/) by Sybren A. Stuvel
- [pyasn](https://pypi.org/project/pyasn/) by
- [six](https://pypi.org/project/six/) by Benjamin Peterson
- [thanker](https://pypi.org/project/thanker/) by WardPearce
- [aiohttp](https://pypi.org/project/aiohttp/) by Nikolay Kim
- [attrs](https://pypi.org/project/attrs/) by Hynek Schlawack
- [chardet](https://pypi.org/project/chardet/) by Mark Pilgrim
- [multidict](https://pypi.org/project/multidict/) by Andrew Svetlov
- [async-timeout](https://pypi.org/project/async-timeout/) by Andrew Svetlov
- [yarl](https://pypi.org/project/yarl/) by Andrew Svetlov
- [idna](https://pypi.org/project/idna/) by Kim Davies
- [typing-extensions](https://pypi.org/project/typing-extensions/) by Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee
- [click](https://pypi.org/project/click/) by Armin Ronacher
- [asynctest](https://pypi.org/project/asynctest/) by Martin Richard
- [aiofiles](https://pypi.org/project/aiofiles/) by Tin Tvrtkovic
- [typing-extensions](https://pypi.org/project/typing-extensions/) by Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee
- [uritemplate](https://pypi.org/project/uritemplate/) by Ian Stapleton Cordasco
- [yarl](https://pypi.org/project/yarl/) by Andrew Svetlov
- [multidict](https://pypi.org/project/multidict/) by Andrew Svetlov
- [idna](https://pypi.org/project/idna/) by Kim Davies
