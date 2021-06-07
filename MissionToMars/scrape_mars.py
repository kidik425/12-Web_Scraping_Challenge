# Dependencies
import pandas as pd

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # browser = init_browser()
    htmlMarsTable = './assets/pages/table.html'

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    listings = {}


    ##############################################
    ######## GET MARS NEWS
    urlRPS = 'https://redplanetscience.com'
    browser.visit(urlRPS)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Identify and return news title
    newsT = soup.find('div', class_='content_title').text
    # Identify and return news paragraph
    newsP = soup.find('div',class_='article_teaser_body').text
    # Identify and return news date
    newsD = soup.find('div',class_='list_date').text


    ##############################################
    ######## GET MARS SPACE IMAGE
    urlSIM = 'https://spaceimages-mars.com'
    browser.visit(urlSIM)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Capture image URL 
    featureImageUrl = f"{urlSIM}/{featureImageSrc}"


    ##############################################
    ######## GET MARS FACTS
    urlGF = 'https://galaxyfacts-mars.com'

    # Load URL into pandas
    tables = pd.read_html(urlGF)

    df = tables[0]

    # convert df to html
    df.to_html(htmlMarsTable)


    ##############################################
    ######## 
    urlMH = 'https://marshemispheres.com'
    browser.visit(urlMH)

    # User BSoup to go to URL and get elements
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Create variable to hold the list of links
    items = soup.find_all('div', class_='item')
    #items #sanity check

    # Capture list of URLS for the pictures 
    # by looping through tags
    urlList = []

    for item in items:
        picDict = {} # going to pass in both the title and URL into dict
        
        picUrl = item.find('a')['href'] #the URL
        
        picTitle = item.find('h3').text
        picTitle = picTitle.replace(' Enhanced','') #removed unneeded syntax
        
        picDict[picTitle]=f"{urlMH}/{picUrl}"
        urlList.append(picDict)  #combines the parent URL to pic URL


    # Quit the browser
    browser.quit()

    # create return dict
    marsData = {
        "newsTitle": newsT,
        "newsParagraph": newsP,
        "featureImageURL": featureImageUrl,
        "marsTable": htmlMarsTable
    }


    return marsData
