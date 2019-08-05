# ExportTelegramContacts

    Export Telegram Contacts To Google CSV file

# How to use

    1- First you have to register at https://my.telegram.org/auth

    2- Then you have to register an application for your phone at https://my.telegram.org/apps

    3- Enter the retrieved 'api_id' and 'api_hash' in exporter.py

```python
    6. api_id = 1234
    7. api_hash = "abcdefghigk"
```

    4- Install the necessary dependencies and run it

```
    $ pip install requirements.txt
    $ python exporter.py
```

    5- Now you will get message from telegram team to confirm contact request, just press the Allow button at the bottom of the message.

    6- Rerun exporter.py after 24hrs

    7- Now you have contacts.csv file, import it at contacts.google.com

cheers!!
