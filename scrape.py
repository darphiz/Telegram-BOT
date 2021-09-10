from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('../tele_scrape/') 
load_dotenv(os.path.join(project_folder, '.env'))

api_id = os.getenv("API_ID") 
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE")
client = TelegramClient(phone, api_id, api_hash)
# authorize the user
client.connect()
print('Authenticating.....')
if not client.is_user_authorized():
    print("Permission required!, Enter the OTP code sent to your telegram to continue")
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
    print("Authentication successful!")
else:
    print("Authentication successful!")

scraping = True
while scraping:
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]

    result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))

    chats.extend(result.chats)
    x = 'Getting groups.'
    for chat in chats:
        try:
            if chat.megagroup== True:
                x+='.'
                groups.append(chat)
                print(x)
        except:
            x+='.'
            print(x)
            continue
    ## Ask user to select group to scrape members from
    error = True
    print('Choose a group to scrape members from: \nBelow are groups based on your recent chats')
    while error:
        try:
            i=0
            for g in groups:
                print(str(i) + ' - ' + g.title)
                i+=1
            g_index = input("Enter Group Number: ")
            target_group=groups[int(g_index)]
            error = False
        except:
            print('Invalid Input, Try again...')
    print(f'Bot is Fetching Members of \'{target_group.title}\'...')
    all_participants = []
    try:
        all_participants = client.get_participants(target_group, aggressive=True)
        print('Reading.....')
        print('Saving In file...')
        with open(f"{target_group.title}.csv","w",encoding='UTF-8') as f:
            writer = csv.writer(f,delimiter=",",lineterminator="\n")
            writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
            for user in all_participants:
                if user.username:
                    username= user.username
                else:
                    username= "No Username"
                if user.first_name:
                    first_name= user.first_name
                else:
                    first_name= "No First Name"
                if user.last_name:
                    last_name= user.last_name
                else:
                    last_name= "No Last Name"
                name= (first_name + ' ' + last_name).strip()
                writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])      
        print('Members scraped successfully!!!')
        print('Loyal to my emperor')
        print('Should We Do This Again?')
        consent = input('Type yes to scrape another group >>')
        if consent.lower() == "yes":
            scraping = True
        else:
            scraping = False

    except:
        print('An error occurred')
        print('Could not fetch data because group is probably private or you were banned from it')
        print('Should We Do This Again?')
        consent = input('Type yes to scrape another group >>')
        if consent.lower() == "yes":
            scraping = True
        else:
            scraping = False




