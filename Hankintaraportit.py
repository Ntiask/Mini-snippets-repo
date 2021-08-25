import requests
import os
import fnmatch

#### Author: Niko Tiaskorpi ,  Tämä ohjelmisto on tehty lataamaan hankinta raportit zendeskiin juuri siitä kansiosta missä olet.
#### Se lataa tiedostot sen asiakkaan zendesk artikkeliin kun tiedoston nimessä lukee.  joten nimeä tiedostot OIKEIN!
#### Käytä omalla vastuulla ja vain jos tiedät mitä teet!

username = input('Zendesk Username: ')
password = input('Zendesk Password: ')

response = requests.get('https://crayonfi.zendesk.com/api/v2/users.json', auth=(username, password))
if response.ok == True:
    print('Login succesful')

print('Listing files on folder...')

for file in os.listdir('.'):
    print(file)

print('Uploading files...')

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*Atria_Hankintaraportti*'):
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://crayonfi.zendesk.com/api/v2/help_center/fi/articles/360003071039/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*ELO_Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://crayonfi.zendesk.com/api/v2/help_center/fi/articles/115001443144/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*Metso_Minerals*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://crayonfi.zendesk.com/api/v2/help_center/fi/articles/115001339230/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*Patria_Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://crayonfi.zendesk.com/api/v2/help_center/fi/articles/360001231604/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*Solita Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://crayonfi.zendesk.com/api/v2/help_center/fi/articles/360000254924/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*St1_Purchase_Report*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://crayonfi.zendesk.com/api/v2/help_center/fi/articles/115001184310/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*Tyollisyysrahasto_Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://crayonfi.zendesk.com/api/v2/help_center/fi/articles/115001339250/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    elif fnmatch.fnmatch(file, '*VR_Hankintaraportti*'):
        
        tiedosto = file
        files = {
            'inline': (None, 'false'),
            'file': (tiedosto, open(tiedosto, 'rb')),
        }

        response = requests.post('https://crayonfi.zendesk.com/api/v2/help_center/fi/articles/360006331919/attachments.json', files=files, auth=(username, password))

        if response.ok == True:
            print(file, 'Uploaded Succesfully')

    else:
        print(file, 'Did not match any customer purchase report. Skipped this file')







