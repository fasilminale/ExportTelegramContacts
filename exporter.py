from telethon.sync import TelegramClient
from telethon import functions, types
from telethon import errors
import csv

api_id = 0000
api_hash = "absfdefefe"
name = "session_name"

with TelegramClient(name, api_id, api_hash) as client:
    try:
        with client.takeout(contacts=True) as takeout:
            result = takeout(functions.contacts.GetSavedRequest())
            with open('contacts.csv', 'w') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',')
                column = ["Name", "Given Name", "Additional Name", "Family Name", "Yomi Name", "Given Name Yomi", "Additional Name Yomi", "Family Name Yomi", "Name Prefix", "Name Suffix", "Initials", "Nickname", "Short Name", "Maiden Name", "Birthday", "Gender", "Location", "Billing Information", "Directory Server",
                          "Mileage", "Occupation", "Hobby", "Sensitivity", "Priority", "Subject", "Notes", "Language", "Photo", "Group Membership", "E-mail 1 - Type", "E-mail 1 - Value", "IM 1 - Type", "IM 1 - Service", "IM 1 - Value", "Phone 1 - Type", "Phone 1 - Value", "Website 1 - Type", "Website 1 - Value"]
                filewriter.writerow(column)
                for k, x in enumerate(result):
                    row = [f"{x.first_name} { x.last_name if x.last_name else '' }", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                           None, None, None, None, None, None, None, None, "* myContacts", None, None, None, None, None, "Mobile", f'+{x.phone}', None, ]
                    filewriter.writerow(row)

    except errors.TakeoutInitDelayError as e:
        print('Must wait', e.seconds, 'before takeout')
