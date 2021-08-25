import requests
import os
import fnmatch

#### This piece of code will upload multiple files from current folder to zendesk ticket system using zendesk API with certain Criterias
#### Used to automate report handling.

username = input('Zendesk Username: ')
password = input('Zendesk Password: ')

response = requests.get('https://XXXX.zendesk.com/api/v2/users.json', auth=(username, password))
if response.ok == True:
    print('Login succesful')

print('Listing files on folder...')

for file in os.listdir('.'):
    print(file)

print('Uploading files...')

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*XXXXX_Hankintaraportti*'):
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://XXXXX.zendesk.com/api/v2/help_center/fi/articles/360003071039/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*XXXX_Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://XXXXXXX.zendesk.com/api/v2/help_center/fi/articles/115001443144/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*XXXX_Minerals*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://XXXXX.zendesk.com/api/v2/help_center/fi/articles/115001339230/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*XXXXXX_Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://XXXXX.zendesk.com/api/v2/help_center/fi/articles/360001231604/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*XXXX Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://XXXXX.zendesk.com/api/v2/help_center/fi/articles/360000254924/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*XXXXXX_Purchase_Report*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://XXXXXX.zendesk.com/api/v2/help_center/fi/articles/115001184310/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*XXXXX_Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://XXXXX.zendesk.com/api/v2/help_center/fi/articles/115001339250/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*XXXX_Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://XXXXXX.zendesk.com/api/v2/help_center/fi/articles/360006331919/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    else:
        print(file, 'Did not match any customer purchase report. Skipped this file')







