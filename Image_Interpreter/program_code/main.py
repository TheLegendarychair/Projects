from interpreter import interpret
from scraper import scrape


print('1 - Change website\n'
      '2 - Scrape images\n'
      '3 - Change Google application credentials\n')
func_input = input('Enter your choice: ')
if func_input == '1':
    site_url = input('Enter website url: ')
    file = open('site_url.txt', 'w+')
    file.write(site_url)
    file.close()
elif func_input == '2':
    scrape()
elif func_input == '3':
    application_credentials = input('Enter Google application credentials: ')
    file = open('application_credentials.txt', 'w+')
    file.write(application_credentials)
    file.close()










#add multiple driver support








