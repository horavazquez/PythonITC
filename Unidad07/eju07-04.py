from urllib import request
from urllib.error import URLError
url = 'https://www.gutenberg.org/files/2000/2000-0.txt'
try:
    f = request.urlopen(url)
except URLError:
    print('¡La url ' + url + ' no existe!')
else:
    contenido = f.read()
    print(len(contenido.split()))