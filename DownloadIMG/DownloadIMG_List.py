# MODULES
import pandas as pd
import urllib.request

# IDEAL PARA BAIXAR LISTA DE IMAGENS DIVERSAS DA INTERNET

def url_to_png(i, url, file_path):
    """
    :param i: number of image
    :param url: Link of an image
    :param file_path: where to save the image
    :return: None
    """

    filename = f"image-{i}.png"
    full_path = f"{file_path}{filename}"
    urllib.request.urlretrieve(url, full_path)

    print(f"{filename} saved.")

    return None

# Set Constants
filename = 'imgs_urls.csv'
file_path = 'images/'

# Read List of URLs as Pandas DataFrame
urls = pd.read_csv(filename)

for i, url in enumerate(urls.values):
    url_to_png(i, url, file_path)