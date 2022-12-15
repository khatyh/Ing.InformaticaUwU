import requests #Estoy importando la libreria requests que me sirve para comunicarme con la api
from skimage import io
api_key="live_DHPHw5H2c54o4EmTM88MKSxoWb121gkyW0ugTo4yjYt6rtk4GdItFk15CNWhpnui"
r = requests.get('https://api.thecatapi.com/v1/images/search') 

datos = r.json()

gato=datos[0]["url"]
print(gato)

imagen=io.imread(gato)
io.imshow(imagen)
io.show()
