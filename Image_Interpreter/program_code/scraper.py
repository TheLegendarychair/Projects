import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from interpreter import interpret
from text_to_speech_converter import text_to_speech

def scrape():
    file = open('site_url.txt', 'r')
    url = file.readline()
    valid_file_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.svg','.webp')

    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    driver = webdriver.Edge(options=edge_options)

    driver.get(url)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    image_links = soup.find_all('img')




    output_directory = 'image_downloads'
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    for image_link in image_links:
        image_url = image_link['src']

        # check if current img has valid extension that can be downloaded
        if any(image_url.endswith(file_extension) for file_extension in valid_file_extensions):

            image_url_absolute = urljoin(url, image_url)
            image_name = os.path.join(output_directory, os.path.basename(image_url_absolute))
            image_content = requests.get(image_url_absolute).content
            alt_text = image_link.get('alt', 'no alt text')
            if (alt_text == '' or alt_text == ' '):
                alt_text = 'no alt text'

            with open(image_name, 'wb') as file:
                file.write(image_content)

            image_discription = interpret(image_name)
            image_link.replace_with(image_discription)

            #print(f"Image downloaded: {image_name}")
            #print(f"Alternative text: {alt_text}")
    site_text = soup.getText()
    text_to_speech(site_text)
    print(site_text)
