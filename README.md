# Telegram-BOT
This BOT automatically scrapes groups you specify and add them to your own specified group
## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage) 
- [References](#references)
- [Contact Information](#contact-information)

## Installation
- Fist, you have to install the dependencies by running `pip install -r requirements.txt`
- Create a `.env` file.
-  Add the following to the `.env` file 
```
API_ID = 'Your app id'
API_HASH = 'Your API hash'
PHONE = 'Your phone number with country code'
```
- Click [here](https://my.telegram.org/apps) to create your app_id and app_hash
## Usage
There are two scripts in this project, namely `scrape.py` and `add_member.py`.
- First, run scrape.py, by running `python scrape.py` in your bash console.
- Follow the prompts to select the groups you want to scrape its members.
- the details of members will be saved in a .csv file with the name as the group id
- Finally, run `python add_member.py <file_name.csv>` 
- You will be prompted to select the group to add the scraped members.
- Make sure you have the permission to add member to this group

## Contribution
If you would like to contribute to this project reach out to me. Contact Information can be found below or by clicking on the 'Contact-Information' link provided in the Table of Contents.

## Licenses

<a href="https://img.shields.io/badge/License-MIT-brightgreen"><img alt="M.I.T. License use" src="https://img.shields.io/badge/License-MIT-brightgreen"></a>

## References 
This BOT is built on the [Telethon](https://docs.telethon.dev/en/latest/) Library.
The files contains an improvement on [python.gotrained.com](https://python.gotrained.com/scraping-telegram-group-members-python-telethon/)'s tutorial. 

## Contact Information
Email Address: daramolaafeez123@gmail.com
[Github Profile](https://github.com/darphiz)

[Github Repo](https://github.com/darphiz/Telegram-BOT)


