import time

# CSV file where the extracted earthquake data will be saved
archivo_csv = "f_m_ENERO.csv"

# Starting index for pagination
start = 5475
# Amount to decrease 'start' by after each iteration
decremento = 15

# Continue looping until we reach the last desired page
while start >= 2760:
    # Construct the URL for the current page of earthquake listings
    url = f"https://rsn.ucr.ac.cr/actividad-sismica/ultimos-sismos?start={start}"
    
    # Send GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request fails

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all table rows (skip the first one, which is likely the header)
    sismos = soup.find_all("tr")[1:]

    # List to store earthquake data from this page
    datos_sismos = []

    # Loop through each row (each earthquake record)
    for sismo in sismos:
        cols = sismo.find_all("td")  # Get all columns in the row
        contenido = cols[0].text.strip() if len(cols) > 0 else "Sin datos"  # Extract text

        # Use regex to find the earthquake date/time and magnitude
        match = re.search(r"SISMO, (.*), Mag: ([\d,.]+) Mw", contenido)
        if match:
            fecha_hora = match.group(1).strip()  # Extract date and time
            magnitud = match.group(2).strip().replace(",", ".")  # Extract and format magnitude
            datos_sismos.append({"fecha_hora": fecha_hora, "magnitud": magnitud})

    # Reverse the order of the data so it’s in chronological order
    datos_sismos.reverse()

    # Open the CSV file and append the extracted data
    with open(archivo_csv, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["fecha_hora", "magnitud"])
        writer.writerows(datos_sismos)  # Write all data to the file

    # Print each entry to the console for verification
    for dato in datos_sismos:
        print(dato)

    # Move to the previous page
    start -= decremento
    time.sleep(1)  # Pause to avoid overwhelming the server

    start -= decremento
    time.sleep(1)
