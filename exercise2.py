import requests #instalar librerias request Beautifulsoup
from bs4 import BeautifulSoup

# Elejir palabra a buscar
palabra_clave = input("\n🔍 Ingresa una palabra clave para buscar en MercadoLibre: ")
# Mercado libre en este caso
url = f"https://listado.mercadolibre.com.co/{palabra_clave}"

# HTTP 
headers = {
    "User-Agent": "Mozilla/5.0"
}
respuesta = requests.get(url, headers=headers)

# Verificar la solicitud 
if respuesta.status_code == 200:
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    productos = sopa.find_all("li", class_="ui-search-layout__item", limit=5)

    print(f"\n Resultados para: '{palabra_clave}'\n")

    for i, producto in enumerate(productos, 1):
        titulo = producto.find("h3").text.strip() if producto.find("h3") else "Sin título"#Sino sale intentar usar h2 a veces las clases de paginas externas actualizan el tamaño
        precio = producto.find("span", class_="andes-money-amount__fraction")
        precio = precio.text if precio else "Sin precio"#valor
        print(f"{i}. {titulo} - ${precio}")
else:
    print("Error al acceder a Mercado Libre.")
