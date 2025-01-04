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

    # Extraer los datos de la página
    misiones = soup.find_all('a')  # Ajusta según el HTML del sitio

    # Guardar los datos en un archivo .txt
    with open('outputs/misiones.txt', 'w', encoding='utf-8') as file:
        for mision in misiones:
            nombre = mision.text.strip()
            enlace = mision.get('href')
            if nombre and enlace:  # Evita líneas vacías
                file.write(f"{nombre} - {enlace}\n")

    driver.quit()
    print("Datos guardados en outputs/misiones.txt")

if __name__ == "__main__":
    main()
