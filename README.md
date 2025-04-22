# 📡 Scraper de Sismos RSN-UCR / RSN-UCR Earthquake Scraper

Este script en Python extrae información de sismos publicada por la **Red Sismológica Nacional de Costa Rica (RSN-UCR)** desde su sitio web oficial.

This Python script extracts earthquake information published by the **National Seismological Network of Costa Rica (RSN-UCR)** from its official website.

---

## 📋 ¿Qué hace el script? / What does the script do?

- Navega automáticamente por las páginas de listados de sismos.
- Extrae la **fecha y hora** del sismo, así como su **magnitud (Mw)**.
- Guarda esta información en un archivo `.csv`.

- Automatically navigates earthquake listing pages.
- Extracts each earthquake’s **date and time** as well as its **magnitude (Mw)**.
- Saves the information into a `.csv` file.

---

## 📦 Requisitos / Requirements

Asegúrate de tener Python 3 instalado. Instala las dependencias con:

Make sure Python 3 is installed. Then install the required packages:

```bash
pip install requests beautifulsoup4
