import requests
from bs4 import BeautifulSoup
import re
import csv
import time

# Starting index for the pagination parameter in the URL
start = 2970
# Amount to decrement 'start' on each iteration
decremento = 15
# Name of the CSV file where data will be saved
archivo_csv = "DECEMBER.csv"
# Counter used to construct individual earthquake detail URLs
contador = 22683

# Loop until 'start' is less than the stopping value (inclusive)
while start >= 2760:
    # Construct the URL for the list of recent earthquakes
    url = f"https://rsn.ucr.ac.cr/actividad-sismica/ultimos-sismos?start={start}"
    # Send a GET request to fetch the page content
    response = requests.get(url)
    response.raise_for_status()  # Raise error if the request fails
    soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML

    # Find all rows (earthquakes) in the table
    sismos = soup.find_all("tr")[0:]
    datos = []  # List to store extracted earthquake data

    # Iterate over each row in the table
    for i, sismo in enumerate(sismos):
        cols = sismo.find_all("td")  # Extract table columns
        contenido = cols[0].text.strip() if len(cols) > 0 else "No"  # Get the text content

        # Use regex to find earthquake description and magnitude
        match = re.search(r"SISMO, (.*), Mag: ([\d,.]+) Mw", contenido)
        if match:
            # Clean and transform the text to create a valid URL
            texto_transformado = contenido.lower().replace(",", "").replace(".", "").replace(":", "-").replace(" ","-").replace("mag-", "mw").replace("mag", "")
            partes = texto_transformado.rsplit("-", 1)  # Split to extract the last parts

            # Construct URL for the detailed page of the earthquake
            url_sismo = f"https://rsn.ucr.ac.cr/actividad-sismica/ultimos-sismos/{contador}-{partes[0][:-2]}{partes[0][-2]},{partes[0][-1]}."
            response_sismo = requests.get(url_sismo)  # Fetch detailed page
            soup_sismo = BeautifulSoup(response_sismo.content, "html.parser")

            # Find the section containing the earthquake details
            article_body = soup_sismo.find(itemprop="articleBody")
            if article_body:
                localizacion, origen = "", ""  # Initialize detail variables
                for p in article_body.find_all("p"):
                    # Look for 'Localización:' and 'Origen:' in the text
                    if "Localización:" in p.text:
                        localizacion = p.text.split("Localización:")[1].strip()
                    elif "Origen:" in p.text:
                        origen = p.text.split("Origen:")[1].strip()

                # If both details were found, save them
                if localizacion and origen:
                    datos.append({"localización": localizacion,"origen": origen})

            contador += 1  # Increment the ID counter for the next detail page

    # Write the extracted data to the CSV file
    with open(archivo_csv, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["localización", "origen"])
        writer.writerows(datos)

    # Print the data to the console
    for dato in datos:
        print(dato)

    # Decrease the starting index to move to the previous page
    start -= decremento
    time.sleep(1)  # Sleep for 1 second to avoid overloading the server
