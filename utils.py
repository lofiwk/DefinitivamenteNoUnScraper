from bs4 import BeautifulSoup

def parse_html(html):
    """Procesa el HTML y devuelve el contenido relevante."""
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('a')
