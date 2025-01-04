from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def main():
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)

    url = "https://www.dofuspourlesnoobs.com"
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a'):
        print(link.text.strip(), "-", link.get('href'))

    driver.quit()

if __name__ == "__main__":
    main()
