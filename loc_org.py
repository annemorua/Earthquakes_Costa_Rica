import time

archivo_csv = "f_m_ENERO.csv"
start = 5475
decremento = 15
while start >= 2760:
    url = f"https://rsn.ucr.ac.cr/actividad-sismica/ultimos-sismos?start={start}"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    sismos = soup.find_all("tr")[1:]
    datos_sismos = []
    for sismo in sismos:
        cols = sismo.find_all("td")
        contenido = cols[0].text.strip() if len(cols) > 0 else "Sin datos"
        match = re.search(r"SISMO, (.*), Mag: ([\d,.]+) Mw", contenido)
        if match:
            fecha_hora = match.group(1).strip()
            magnitud = match.group(2).strip().replace(",", ".")
            datos_sismos.append({"fecha_hora": fecha_hora, "magnitud": magnitud})

    datos_sismos.reverse()

    with open(archivo_csv, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["fecha_hora", "magnitud"])
        writer.writerows(datos_sismos)

    for dato in datos_sismos:
        print(dato)

    start -= decremento
    time.sleep(1)
