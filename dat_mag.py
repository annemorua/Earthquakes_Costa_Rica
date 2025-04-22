import requests
from bs4 import BeautifulSoup
import re
import csv
import time

start = 2970
decremento = 15
archivo_csv = "l_o_DICIEMBRE.csv"
contador = 22683
while start >= 2760:
    url = f"https://rsn.ucr.ac.cr/actividad-sismica/ultimos-sismos?start={start}"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    sismos = soup.find_all("tr")[0:]
    datos = []
    for i, sismo in enumerate(sismos):
        cols = sismo.find_all("td")
        contenido = cols[0].text.strip() if len(cols) > 0 else "No"
        match = re.search(r"SISMO, (.*), Mag: ([\d,.]+) Mw", contenido)
        if match:
            texto_transformado = contenido.lower().replace(",", "").replace(".", "").replace(":", "-").replace(" ","-").replace("mag-", "mw").replace("mag", "")
            partes = texto_transformado.rsplit("-", 1)
            url_sismo = f"https://rsn.ucr.ac.cr/actividad-sismica/ultimos-sismos/{contador}-{partes[0][:-2]}{partes[0][-2]},{partes[0][-1]}."
            response_sismo = requests.get(url_sismo)
            soup_sismo = BeautifulSoup(response_sismo.content, "html.parser")
            article_body = soup_sismo.find(itemprop="articleBody")
            if article_body:
                localizacion, origen = "", ""
                for p in article_body.find_all("p"):
                    if "Localización:" in p.text:
                        localizacion = p.text.split("Localización:")[1].strip()
                    elif "Origen:" in p.text:
                        origen = p.text.split("Origen:")[1].strip()
                if localizacion and origen:
                    datos.append({"localización": localizacion,"origen": origen})
            contador += 1

    with open(archivo_csv, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["localización", "origen"])
        writer.writerows(datos)

    for dato in datos:
        print(dato)

    start -= decremento
    time.sleep(1)
