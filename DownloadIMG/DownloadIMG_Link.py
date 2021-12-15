# MODULES
import urllib.request

# IDEAL PARA BAIXAR IMAGENS DE GALERIAS DA INTERNET

def url_to_png(i, url, FILE_PATH):
    """
        :param i: number of image
        :param url: Link of an image
        :param file_path: where to save the image
        :return: None
    """

    filename = f"img_{i}.png"
    full_path = f"{FILE_PATH}{filename}"
    print(full_path)
    urllib.request.urlretrieve(url, full_path)

    print(f"{filename} saved.")

    return None

# Set Constants
FILE_PATH = 'images/'
NUMBER_PAGES = 50 # NÚMERO DE PÁGINAS

for i in range(1, NUMBER_PAGES+1):
    link = "/.../" + f"{i}" # LINK PADRÃO PARA IMAGENS
    print(link)
    url_to_png(i, link, FILE_PATH)